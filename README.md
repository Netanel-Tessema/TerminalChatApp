# Chat Application

A simple terminal-based chat system built with Python's `socket` and `threading` libraries. This project includes both server and client implementations and supports multiple users, message broadcasting, private messages, and persistent chat history.

## Features

- Real-time chat between multiple clients
- Chat history persistence using JSON
- Private messaging with @username syntax
- User-friendly terminal interface
- Multithreaded server-client communication

## How to Run

### Requirements
- Python 3.x

### 1. Clone the repository
```bash
git clone https://github.com/your-username/chat-application.git
cd chat-application
```

### 2. Start the Server
```bash
python chat_server.py
```

### 3. Start the Client (in a separate terminal)
```bash
python chat_client.py
```

You can open multiple terminals to simulate multiple users.

### 4. To exit the chat
Type `exit` and press Enter.

## Files
- `chat_server.py`: The server code that handles incoming connections and message routing.
- `chat_client.py`: The client interface for sending and receiving messages.
- `chat_history.json`: File used to persist chat history between sessions.

## License
This project is open source and free to use for educational purposes.
