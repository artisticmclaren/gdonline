import socket
import threading
from colorama import Back,Fore,Style

port=6000

header=64

server=socket.gethostbyname(socket.gethostname())
addr=(server,port)

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addr)

def handle_client(conn,addr):
    msg=""
    print(f"{Fore.GREEN}[INFO]{Fore.WHITE} New connection: {addr}.")
    pid=addr[1]
    connected=True
    while connected:
        msglength=conn.recv(header).decode('utf-8')
        if msglength:
            msglength=int(msglength)
            msg=conn.recv(msglength).decode('utf-8')
            if msg=="disc":
                connected=False
                break
        if connected:
            print(f"{Fore.CYAN}[CONN {addr}]{Fore.WHITE} {msg}")
            server.sendall(msg)
    conn.close()


def start():
    server.listen()
    print(f"{Fore.LIGHTGREEN_EX}[INFO]{Fore.WHITE} Listening on {socket.gethostname()}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"{Fore.LIGHTGREEN_EX}[INFO]{Fore.WHITE} Active connections: {threading.activeCount() - 1}")
        if input("")=='-shutdown':
            server.close()
            quit()

print(f"{Fore.LIGHTGREEN_EX}[INFO]{Fore.WHITE} Server starting...")
start()