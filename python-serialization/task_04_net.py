#!/usr/bin/python3
"""
Client-server application demonstrating serialization over a network.
"""

import socket
import json


def start_server(host="127.0.0.1", port=65432):
    """
    Starts a server that receives serialized JSON data,
    deserializes it, and prints the dictionary.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        as server_socket:
            server_socket.bind((host, port))
            server_socket.listen(1)
            print("Server listening on {}:{}".format(host, port))

            conn, addr = server_socket.accept()
            with conn:
                print("Connected by", addr)

                data = conn.recv(4096)
                if not data:
                    return

                # Deserialize JSON data
                received_dict = json.loads(data.decode("utf-8"))
                print("Received dictionary:\n{}".format(received_dict))

    except Exception as e:
        print("Server error:", e)


def send_data(data, host="127.0.0.1", port=65432):
    """
    Acts as a client that serializes a dictionary
    and sends it to the server.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        as client_socket:
            client_socket.connect((host, port))

            # Serialize dictionary
            serialized_data = json.dumps(data)

            # Send data
            client_socket.sendall(serialized_data.encode("utf-8"))

    except Exception as e:
        print("Client error:", e)
