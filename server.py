import socket

HOST = "127.0.0.1"
PORT = 12345


def process_message(msg: str) -> str:
    return msg.upper()


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server is listening on {HOST}:{PORT}")
        conn, addr = s.accept()

        with conn:
            print(f"Connected with the client: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                text = data.decode("utf-8")
                print(f"Received: {text}")
                response = process_message(text)
                conn.sendall(response.encode("utf-8"))
                print(f"Replied: {response}")


run_server()
