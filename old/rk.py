import socket
import threading
import configparser
import time
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Union

# Constants for configuration and server
CONFIG_FILE = 'config.ini'
MAX_BUFFER = 1024
PORT = 44445

# Global variable for file content
text_content: Optional[List[str]] = None

def load_config(config_file: str) -> Dict[str, Union[str, bool]]:
    """Load configuration from the config file."""
    config = configparser.ConfigParser()
    config.read(config_file)
    config_dict: Dict[str, Union[str, bool]] = {
        'linuxpath': config['DEFAULT'].get('linuxpath', ''),
        'reread': config['DEFAULT'].getboolean('REREAD_ON_QUERY', False)
    }
    return config_dict

def query_search(filepath: str, search_string: str, reread: bool) -> str:
    """Search for a string in the file, re-read file based on config."""
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

def logs(message: str) -> None:
    """Log messages with a timestamp."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"DEBUG: [{timestamp}] {message}")

def handle_requests(client_sock: socket.socket, client_addr: Tuple[str, int], config: Dict[str, Union[str, bool]]) -> None:
    """Handle incoming client requests."""
    try:
        while True:
            data = client_sock.recv(MAX_BUFFER).decode().strip('\x00')
            if not data:
                break
            start_time = time.time()
            linuxpath = config['linuxpath']
            reread = config['reread']
            assert isinstance(linuxpath, str)  # Ensure linuxpath is a string
            assert isinstance(reread, bool)  # Ensure reread is a boolean
            response = query_search(linuxpath, data, reread)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            logs(f"Client IP: {client_addr[0]}, Query: '{data}', Execution time: {execution_time:.9f} ms")
            client_sock.sendall(response.encode())
    finally:
        client_sock.close()

def run_server() -> None:
    """Run the TCP server."""
    global text_content
    config = load_config(CONFIG_FILE)
    text_content = None if config['reread'] else []

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('', PORT))
    server_sock.listen()

    print("waiting clients...")

    while True:
        client_sock, client_addr = server_sock.accept()
        client_handling = threading.Thread(target=handle_requests, args=(client_sock, client_addr, config))
        client_handling.start()

if __name__ == "__main__":
    run_server()
