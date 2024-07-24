import socket

SERVER_ADDR = "localhost"
PORT = 44445
MAX_BUFFER = 1024

def req_search(query):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        client_sock.connect((SERVER_ADDR, PORT))
        client_sock.sendall(query.encode())
        response = client_sock.recv(MAX_BUFFER).decode()
    return response


def main():
    query = input("Enter a string to search:")
    response = req_search(query)
    print(response)


if __name__ == "__main__":
    main()
