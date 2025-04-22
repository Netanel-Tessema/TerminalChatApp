# chat_client.py
import socket
import threading

# Create a connection to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'  # Server IP address
server_port = 12345  # Server port
client_socket.connect((server_ip, server_port))

# Get username from the user
username = input("Enter your username: ")
client_socket.send(username.encode())

# Receive chat history from the server
chat_history = client_socket.recv(1024).decode()

if chat_history.strip():
    print("\n--- Chat History ---")
    print(chat_history)

print("You can send messages now.")

def receive_messages():
    """Function to receive messages from the server"""
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                if not message.startswith("--- Chat History ---"):
                    print(message)
        except:
            print("Error receiving message.")
            client_socket.close()
            break

def send_messages():
    """Function to send messages to the server"""
    while True:
        message = input("")
        if message.lower() == "exit":
            client_socket.close()
            break
        client_socket.send(message.encode())

# Create threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)
receive_thread.start()
send_thread.start()








