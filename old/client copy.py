import socket
import ssl
import configparser

SERVER_ADDR = "localhost"  # Server address
PORT = 44445  # Server port
MAX_BUFFER = 1024  # Maximum buffer size for receiving data
CONFIG_FILE = 'config.ini'  # Configuration file name

# Function to load configuration from a file
def load_config(config_file):
    """
    Loads the configuration from a specified INI file.

    Args:
        config_file (str): The path to the configuration file.

    Returns:
        dict: A dictionary with configuration parameters.
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    config_dict = {
        'use_ssl': config['DEFAULT'].getboolean('USE_SSL', False),
        'certfile': config['DEFAULT'].get('CERTFILE', ''),
        'keyfile': config['DEFAULT'].get('KEYFILE', '')
    }
    return config_dict

# Function to send a query to the server and get a response
def req_search(query, use_ssl, certfile, keyfile):
    """
    Sends a search query to the server and retrieves the response.

    Args:
        query (str): The search query string.
        use_ssl (bool): Flag to use SSL for the connection.
        certfile (str): Path to the SSL certificate file.
        keyfile (str): Path to the SSL key file.

    Returns:
        str: The response from the server.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        if use_ssl:
            context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            client_sock = context.wrap_socket(client_sock, server_hostname=SERVER_ADDR)
        
        client_sock.connect((SERVER_ADDR, PORT))  # Connect to the server
        client_sock.sendall(query.encode())  # Send the query
        response = client_sock.recv(MAX_BUFFER).decode()  # Receive the response
    return response

# Main function to load config, get query input, and print the server response
def main():
    """
    The main function that loads the configuration, takes user input, sends the query to the server, and prints the response.
    """
    config = load_config(CONFIG_FILE)  # Load the configuration
    query = input("Enter a string to search:")  # Get query input from the user
    response = req_search(query, config['use_ssl'], config['certfile'], config['keyfile'])  # Get the response from the server
    print(response)  # Print the response

if __name__ == "__main__":  # Ensure the script runs only if it's the main module
    main()
