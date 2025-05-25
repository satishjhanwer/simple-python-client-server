import socket

HOST = "127.0.0.1"
PORT = 12345


def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = input("Enter the message:")
        s.sendall(message.encode("utf-8"))
        data = s.recv(1024)
        text = data.decode("utf8")
        print(f"Server responded:{text}")


run_client()
