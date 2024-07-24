import socket
import ssl
import configparser

SERVER_ADDR = "localhost"
PORT = 44445
MAX_BUFFER = 1024
CONFIG_FILE = 'config.ini'

def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    config_dict = {
        'use_ssl': config['DEFAULT'].getboolean('USE_SSL', False),
        'certfile': config['DEFAULT'].get('CERTFILE', ''),
        'keyfile': config['DEFAULT'].get('KEYFILE', '')
    }
    return config_dict

def req_search(query, use_ssl, certfile, keyfile):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        if use_ssl:
            context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            client_sock = context.wrap_socket(client_sock, server_hostname=SERVER_ADDR)
        
        client_sock.connect((SERVER_ADDR, PORT))
        client_sock.sendall(query.encode())
        response = client_sock.recv(MAX_BUFFER).decode()
    return response

def main():
    config = load_config(CONFIG_FILE)
    query = input("Enter a string to search:")
    response = req_search(query, config['use_ssl'], config['certfile'], config['keyfile'])
    print("Server response:", response)

if __name__ == "__main__": # pragma: no cover
    main()
