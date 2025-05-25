# Simple Python Client-Server Example

This project demonstrates a basic TCP client-server communication in Python using sockets.

## Files

- `server.py`: Starts a TCP server that listens for incoming connections, receives a message, converts it to uppercase, and sends it back to the client.
- `client.py`: Connects to the server, sends a user-provided message, and prints the server's response.

## How It Works

1. **Server**

   - Listens on `127.0.0.1:12345`.
   - Accepts a single client connection.
   - For each message received, replies with the message in uppercase.

2. **Client**
   - Connects to the server at `127.0.0.1:12345`.
   - Prompts the user for a message, sends it to the server, and prints the response.

## Usage

### 1. Start the Server

Open a terminal and run:

```bash
python3 server.py
```

You should see:

```bash
Server is listening on 127.0.0.1:12345
```

### 2. Run the Client

Open another terminal and run:

```bash
python3 client.py
```

Enter a message when prompted. The client will display the server's response.

Example
Client:

```bash
Enter the message:hello world
Server responded:HELLO WORLD
```

Server:

```bash
Server is listening on 127.0.0.1:12345
Connected with the client: ('127.0.0.1', 12345)
Received: hello world
Replied: HELLO WORLD
```

Notes

- The server handles one client connection at a time.
- Both client and server must be run on the same machine (localhost).
