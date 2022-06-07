import socket
from threading import Thread

HOST_IP = '10.10.20.51'    # 내가 접속할 서버의 ip주소
PORT = 9010                 # 서버의 포트 번호 (서로 같아야 연결 가능)

def rcvMsg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            pass

def runChat():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST_IP, PORT))
        t = Thread(target=rcvMsg, args=(sock,))
        t.daemon = True
        t.start()

        while True:
            msg = input()
            if msg == '/quit':
                sock.send(msg.encode())
                break

            sock.send(msg.encode())

runChat()