import socket
import threading
import configparser
import time
from datetime import datetime

CONFIG_FILE = 'config.ini'
MAX_BUFFER = 1024
PORT = 44445 

def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    config_dict = {
        'linuxpath': config['DEFAULT'].get('linuxpath', ''),
        'reread': config['DEFAULT'].getboolean('REREAD_ON_QUERY', False)
    }
    return config_dict

def rabin_karp(text, pattern, q=101):
    d = 256
    m = len(pattern)
    n = len(text)
    
    if n < m:  # Check to prevent IndexError
        return False

    p = 0
    t = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return True
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return False

import ahocorasick

def query_search(filepath, search_string, reread):
    A = ahocorasick.Automaton()
    A.add_word(search_string, search_string)
    A.make_automaton()

    if reread:
        with open(filepath, 'r') as file:
            for line in file:
                for end_index, found_word in A.iter(line.strip()):
                    if found_word == search_string:
                        return "STRING EXISTS\n"
    else:
        global text_content
        if text_content is None:
            with open(filepath, 'r') as file:
                text_content = file.readlines()
        for line in text_content:
            for end_index, found_word in A.iter(line.strip()):
                if found_word == search_string:
                    return "STRING EXISTS\n"
    return "STRING NOT FOUND\n"

def logs(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"DEBUG: [{timestamp}] {message}")

def handle_requests(client_sock, client_addr, config):
    try:
        while True:
            data = client_sock.recv(MAX_BUFFER).decode().strip('\x00')
            if not data:
                break
            start_time = time.time()
            response = query_search(config['linuxpath'], data, config['reread'])
            end_time = time.time()
            execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
            logs(f"Client IP: {client_addr[0]}, Query: '{data}', Execution time: {execution_time_ms:.6f} ms")
            client_sock.sendall(response.encode())
    finally:
        client_sock.close()

def run_server():
    config = load_config(CONFIG_FILE)
    global text_content
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
