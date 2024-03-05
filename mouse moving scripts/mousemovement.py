import time
import sys
import socket
import threading

from mouse_instruct import MouseInstruct, DeviceNotFoundError

def handle_client_connection(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message:
            if ',' in message:
                x, y = map(int, message.split(','))
                m.move(x, y)
            elif message == "1" or message == "0":
                click = int(message)
                if click == 1:
                    m.press()
                elif click == 0:
                    m.release()
        else:
            break
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(30)

def getMouse():
    try:
        mouse = MouseInstruct.getMouse()
        print("[+] Mouse device found!")
    except DeviceNotFoundError as e:
        print(e)
        sys.exit()
    return mouse

def main():
    global m
    m = getMouse()
    while True:
        client_sock, address = server.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(
            target=handle_client_connection,
            args=(client_sock,)
        )
        client_handler.start()

if __name__ == "__main__":
    main()