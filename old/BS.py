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
        'linuxpath':config['DEFAULT'].get('linuxpath',''),
        'reread':config['DEFAULT'].getboolean('REREAD_ON_QUERY',False)
    }
    return config_dict

def boyer_moore_search(text, pattern):
    """ Boyer-Moore string search algorithm """
    m = len(pattern)
    n = len(text)
    if m == 0:
        return False
    skip = []
    for _ in range(256):  # Initialize skip array for character comparison
        skip.append(m)
    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)

    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return True  # Pattern found
        k += skip[ord(text[k])]
    return False  # Pattern not found

from bisect import bisect_left

def query_search(filepath, search_string, reread):
    if reread:
        with open(filepath, 'r') as file:
            lines = sorted(line.strip() for line in file)
            index = bisect_left(lines, search_string)
            if index != len(lines) and lines[index] == search_string:
                return "STRING EXISTS\n"
    else:
        global text_content
        if text_content is None:
            with open(filepath, 'r') as file:
                text_content = sorted(line.strip() for line in file)
        index = bisect_left(text_content, search_string)
        if index != len(text_content) and text_content[index] == search_string:
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
            execution_time = (end_time - start_time)* 1000
            logs(f"Client IP: {client_addr[0]}, Query: '{data}', Execution time: {execution_time:.9f} ms")
           
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
