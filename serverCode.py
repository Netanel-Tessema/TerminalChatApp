# chat_server.py
import socket
import threading
import json
import os

clients = {}  # Dictionary to store connected clients
history_file = "chat_history.json"

# Load chat history if it exists
if os.path.exists(history_file):
    with open(history_file, "r") as file:
        chat_history = json.load(file)
else:
    chat_history = []

def broadcast_message(message, sender_socket=None):
    global chat_history
    chat_history.append(message)

    with open(history_file, "w") as file:
        json.dump(chat_history, file)

    for client_name, client_socket in clients.items():
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode())
            except Exception as e:
                print(f"Failed to send message to {client_name}: {e}")

def handle_client(client_socket, client_address):
    try:
        client_name = client_socket.recv(1024).decode()

        if client_name in clients:
            client_socket.send("This name is already in use. Please try another name.".encode())
            client_socket.close()
            return

        clients[client_name] = client_socket
        print(f"{client_name} connected from {client_address}.")
        client_socket.send("Connected to the server successfully.".encode())

        if chat_history:
            client_socket.send("\n--- Chat History ---\n".encode())
            for message in chat_history:
                client_socket.send((message + "\n").encode())

        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    break

                if message.lower() == "exit":
                    break

                if message.startswith("@"):  # Private message
                    target_name, private_message = message[1:].split(" ", 1)
                    if target_name in clients:
                        clients[target_name].send(f"[Private from {client_name}] {private_message}".encode())
                    else:
                        client_socket.send("Target user not found.".encode())
                else:
                    broadcast_message(f"{client_name}: {message}", sender_socket=client_socket)
            except Exception as e:
                print(f"Error handling message from {client_name}: {e}")
                break
    finally:
        if client_name in clients:
            del clients[client_name]
            print(f"{client_name} disconnected.")
            broadcast_message(f"{client_name} has left the chat.")

def start_server():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f"Server is listening on {server_ip}:{server_port}...")

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"New connection from {client_address}.")

            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
        except Exception as e:
            print(f"Error accepting new connections: {e}")

if __name__ == "__main__":
    start_server()
