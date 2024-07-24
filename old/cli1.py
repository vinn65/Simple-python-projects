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
        'psk': config['DEFAULT'].get('PSK', '')
    }
    return config_dict

def req_search(query, use_ssl, psk):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        if use_ssl:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.set_ciphers('PSK')
            context.set_psk_client_callback(lambda conn, identity_hint: psk.encode())
            client_sock = context.wrap_socket(client_sock, server_hostname='localhost')
        
        client_sock.connect((SERVER_ADDR, PORT))
        client_sock.sendall(query.encode())
        response = client_sock.recv(MAX_BUFFER).decode()
    return response

def main():
    config = load_config(CONFIG_FILE)
    query = input("Enter a string to search:")
    response = req_search(query, config['use_ssl'], config['psk'])
    print("Server response:", response)

if __name__ == "__main__":
    main()
