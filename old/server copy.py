import socket
import threading
import configparser
import time
from datetime import datetime
import ssl
from typing import Dict, Union

# Constants for configuration
CONFIG_FILE = 'config.ini'
MAX_BUFFER = 1024
PORT = 44445

# Global variable for file content
text_content = None

# Function to load configuration from a file
def load_config(config_file: str) -> Dict[str, Union[str, bool]]:
    """
    The load_config function loads a specified INI file.
    Takes the config_file as an argument of type string.

    Returns:
    A dictionary with the configuration parameters including the path to the file,
    whether to reread on each query, SSL usage, and paths to the certificate and key files.
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    config_dict = {
        'linuxpath': config['DEFAULT'].get('linuxpath', ''),
        'reread': config['DEFAULT'].getboolean('REREAD_ON_QUERY', False),
        'use_ssl': config['DEFAULT'].getboolean('USE_SSL', False),
        'certfile': config['DEFAULT'].get('CERTFILE', ''),
        'keyfile': config['DEFAULT'].get('KEYFILE', '')
    }
    return config_dict

# Function to search for a string in a file
def query_search(filepath: str, search_string: str, reread: bool) -> str:
    """
    The query_search function searches for a specific string in a file.
    Takes filepath, search_string, and reread as arguments.

    Returns:
    A response string indicating whether the search string exists in the file.
    """
    global text_content
    if reread:
        with open(filepath, 'r') as file:
            for line in file:
                if search_string in line:
                    return "STRING EXISTS\n"
    else:
        if text_content is None:
            with open(filepath, 'r') as file:
                text_content = file.readlines()
        for line in text_content:
            if search_string in line:
                return "STRING EXISTS\n"
    return "STRING NOT FOUND\n"

# Function to log messages with timestamps
def logs(message: str) -> None:
    """
    The logs function logs a message with a timestamp.
    Takes message as an argument of type string.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"DEBUG: [{timestamp}] {message}")

# Function to handle incoming client requests
def handle_requests(client_sock: socket.socket, client_addr: tuple, config: Dict[str, Union[str, bool]]) -> None:
    """
    The handle_requests function handles incoming client requests.
    Takes client_sock, client_addr, and config as arguments.

    It reads data from the client, performs the search, logs the execution time,
    and sends the response back to the client.
    """
    try:
        while True:
            data = client_sock.recv(MAX_BUFFER).decode().strip('\x00')
            if not data:
                break
            start_time = time.time()
            response = query_search(config['linuxpath'], data, config['reread'])
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            logs(f"Client IP: {client_addr[0]}, Query: '{data}', Execution time: {execution_time:.9f} ms")
            client_sock.sendall(response.encode())
    finally:
        client_sock.close()

# Main function to run the server
def run_server() -> None:
    """
    The run_server function initializes and runs the server.
    It loads the configuration, sets up the server socket, and handles incoming connections.
    """
    config = load_config(CONFIG_FILE)
    global text_content
    text_content = None if config['reread'] else []

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('', PORT))
    server_sock.listen()

    if config['use_ssl']:
        # Wrap socket with SSL if enabled in the configuration
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=config['certfile'], keyfile=config['keyfile'])
        server_sock = context.wrap_socket(server_sock, server_side=True)
    
    print("Waiting for clients...")

    while True:
        client_sock, client_addr = server_sock.accept()
        client_handling = threading.Thread(target=handle_requests, args=(client_sock, client_addr, config))
        client_handling.start()

if __name__ == "__main__":
    run_server()
