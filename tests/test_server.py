import unittest
from unittest.mock import patch, MagicMock, mock_open
import socket
import unittest
from unittest.mock import patch, MagicMock, mock_open
import socket
import threading
import ssl
import configparser
from io import StringIO
import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from server import load_config, query_search, handle_requests, run_server

class TestServer(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='line1\nline2\nline3\n')
    def test_query_search_reread_true_found(self, mock_open):
        config = {'linuxpath': '/path/to/file', 'reread': True}
        response = query_search(config['linuxpath'], 'line2', config['reread'])
        self.assertEqual(response, "STRING EXISTS\n")

    @patch('builtins.open', new_callable=mock_open, read_data='line1\nline2\nline3\n')
    def test_query_search_reread_true_not_found(self, mock_open):
        config = {'linuxpath': '/path/to/file', 'reread': True}
        response = query_search(config['linuxpath'], 'line4', config['reread'])
        self.assertEqual(response, "STRING NOT FOUND\n")

    @patch('builtins.open', new_callable=mock_open, read_data='line1\nline2\nline3\n')
    def test_query_search_reread_false_found(self, mock_open):
        config = {'linuxpath': '/path/to/file', 'reread': False}
        response = query_search(config['linuxpath'], 'line2', config['reread'])
        self.assertEqual(response, "STRING EXISTS\n")

    @patch('builtins.open', new_callable=mock_open, read_data='line1\nline2\nline3\n')
    def test_query_search_reread_false_not_found(self, mock_open):
        config = {'linuxpath': '/path/to/file', 'reread': False}
        response = query_search(config['linuxpath'], 'line4', config['reread'])
        self.assertEqual(response, "STRING NOT FOUND\n")


    @patch('server.load_config', return_value={
        'linuxpath': '/path/to/file',
        'reread': False,
        'use_ssl': False,
        'certfile': '',
        'keyfile': ''
    })
    @patch('socket.socket')
    @patch('threading.Thread')  # Mock threading.Thread to run server in the same thread
    def test_run_server_no_ssl(self, mock_thread, mock_socket, mock_load_config):
        # Mock server socket operations
        mock_server_sock = MagicMock()
        mock_socket.return_value = mock_server_sock

        # Mock server socket accept method to simulate client connection
        mock_client_sock = MagicMock()
        mock_server_sock.accept.return_value = (mock_client_sock, ('127.0.0.1', 12345))

        # Create an event to stop the server
        stop_event = threading.Event()

        def run_server_and_stop():
            run_server()
            stop_event.set()

        # Start the server in a separate thread
        server_thread = threading.Thread(target=run_server_and_stop)
        server_thread.start()

        # Wait for the server to start (optional)
        time.sleep(0.1)

        # Assert server-related calls (if applicable)
        mock_load_config.assert_called_once_with('config.ini')
        mock_socket.return_value.bind.assert_called_once_with(('', 44445))
        mock_socket.return_value.listen.assert_called_once()

        # Optionally, simulate handling of client requests
        mock_client_sock.recv.return_value = b'test_data'  # Simulate client request
        # Add assertions for handling client request and sending response
        # Example:
        mock_client_sock.sendall.assert_called_once_with(b'SOME_RESPONSE')

        # Stop the server by closing the socket
        mock_server_sock.close()

        # Signal the stop event
        stop_event.set()

        # Join the server thread to wait for it to complete
        server_thread.join()





    # @patch('cli.load_config', return_value={'use_ssl': True, 'certfile': '/path/to/certfile.crt', 'keyfile': '/path/to/keyfile.key'})
    # @patch('socket.socket')
    # @patch('ssl.SSLContext')
    # @patch('threading.Thread')
    # def test_run_server_with_ssl(self, mock_thread, mock_ssl_context, mock_socket, mock_load_config):
    #     mock_server_sock = MagicMock()
    #     mock_socket.return_value = mock_server_sock
    #     mock_thread_instance = MagicMock()
    #     mock_thread.return_value = mock_thread_instance

    #     mock_server_sock.accept.side_effect = [(MagicMock(), ('127.0.0.1', 12345))]

    #     # Start the server in a separate thread
    #     server_thread = threading.Thread(target=run_server)
    #     server_thread.start()

    #     # Wait for a short time to let the server start
    #     time.sleep(0.1)

    #     # Stop the server
    #     mock_server_sock.shutdown.return_value = None
    #     mock_server_sock.close.return_value = None

    #     # Join the server thread to wait for it to complete
    #     server_thread.join()

    #     mock_load_config.assert_called_once_with('config.ini')
    #     mock_server_sock.bind.assert_called_once_with(('', 44445))
    #     mock_server_sock.listen.assert_called_once()
    #     mock_ssl_context_instance = mock_ssl_context.return_value
    #     mock_ssl_context_instance.load_cert_chain.assert_called_once_with('/path/to/certfile.crt', '/path/to/keyfile.key')
    #     mock_server_sock = mock_ssl_context_instance.wrap_socket.return_value
    #     mock_server_sock.accept.assert_called_once()
    #     mock_thread.assert_called_once_with(target=handle_requests, args=(mock_server_sock.accept.return_value[0], ('127.0.0.1', 12345), {'use_ssl': True, 'certfile': '/path/to/certfile.crt', 'keyfile': '/path/to/keyfile.key'}))

if __name__ == '__main__':
    unittest.main()
