import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

while True:
    print(f"Connexion à {HOST_IP}:{HOST_PORT}")
    try:
        s = socket.socket()  # A chaque reconnexion on doit initialiser le socket
        s.connect((HOST_IP, HOST_PORT))
    except socket.error as e:
        print(f"{e} ! Reconnexion...")

        time.sleep(4)
    else:
        print("Connexion réussie!")
        break

while True:
    datas_recues = s.recv(MAX_DATA_SIZE)
    if datas_recues:
        print("Message: ", datas_recues.decode())
        msg_send = input("Vous: ")
        s.sendall(msg_send.encode())
    else:
        break

s.close()
