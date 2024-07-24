import unittest
from unittest.mock import patch, MagicMock
import socket
import ssl
import configparser
import sys
import os

# Add the main directory to sys.path so we can import client and server modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import client as client

class TestClient(unittest.TestCase):

    @patch('configparser.ConfigParser')
    def test_load_config(self, mock_config_parser):
        mock_config_parser_instance = MagicMock()
        mock_config_parser.return_value = mock_config_parser_instance
        mock_config_parser_instance.read.return_value = None
        mock_config_parser_instance['DEFAULT'].getboolean.side_effect = [True]
        mock_config_parser_instance['DEFAULT'].get.side_effect = ['../server.crt', '../server.key']

        config = client.load_config('config.ini')
        self.assertEqual(config['use_ssl'], True)
        self.assertEqual(config['certfile'], '../server.crt')
        self.assertEqual(config['keyfile'], '../server.key')

    @patch('ssl.create_default_context')
    @patch('socket.socket')
    def test_req_search_with_ssl(self, mock_socket, mock_ssl_context):
        mock_socket_instance = mock_socket.return_value.__enter__.return_value
        mock_ssl_context_instance = mock_ssl_context.return_value
        mock_ssl_socket = MagicMock()
        mock_ssl_context_instance.wrap_socket.return_value = mock_ssl_socket

        mock_ssl_socket.recv.return_value = b'SERVER RESPONSE'
        mock_ssl_socket.connect.return_value = None

        response = client.req_search('test query', True, '../server.crt', '../server.key')
        self.assertEqual(response, 'SERVER RESPONSE')

        mock_ssl_context.assert_called_once_with(ssl.Purpose.SERVER_AUTH)
        mock_ssl_context_instance.wrap_socket.assert_called_once()
        mock_ssl_socket.connect.assert_called_once_with((client.SERVER_ADDR, client.PORT))
        mock_ssl_socket.sendall.assert_called_once_with(b'test query')
        mock_ssl_socket.recv.assert_called_once_with(client.MAX_BUFFER)

    @patch('client.socket.socket')
    def test_req_search_without_ssl(self, mock_socket):
        mock_socket_instance = mock_socket.return_value.__enter__.return_value
        mock_socket_instance.recv.return_value = b'SERVER RESPONSE'
        mock_socket_instance.connect.return_value = None

        response = client.req_search('test query', False, '', '')
        self.assertEqual(response, 'SERVER RESPONSE')

        mock_socket_instance.connect.assert_called_once_with((client.SERVER_ADDR, client.PORT))
        mock_socket_instance.sendall.assert_called_once_with(b'test query')
        mock_socket_instance.recv.assert_called_once_with(client.MAX_BUFFER)
    
    @patch('builtins.input', return_value='test query')
    @patch('builtins.print')
    @patch('client.req_search', return_value='SERVER RESPONSE')
    @patch('client.load_config', return_value={'use_ssl': True, 'certfile': 'path/to/certfile.crt', 'keyfile': 'path/to/keyfile.key'})
    def test_main(self, mock_load_config, mock_req_search, mock_print, mock_input):
        with patch('sys.argv', ['client.py']):
            client.main()

        mock_load_config.assert_called_once_with(client.CONFIG_FILE)
        mock_input.assert_called_once_with("Enter a string to search:")
        mock_req_search.assert_called_once_with('test query', True, 'path/to/certfile.crt', 'path/to/keyfile.key')
        mock_print.assert_called_once_with("Server response:", 'SERVER RESPONSE')



if __name__ == '__main__':
    unittest.main()
