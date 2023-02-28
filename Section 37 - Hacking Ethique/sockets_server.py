import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Permet de réutiliser l'adresse du socket

s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Attente de connexion sur {HOST_IP}, port {HOST_PORT}...")
connection_socket, client_adress = s.accept()

print(f"Connexion établie avec le client {client_adress}")

while True:
    txt_send = input("Vous: ")
    connection_socket.sendall(txt_send.encode())
    datas_recues = connection_socket.recv(MAX_DATA_SIZE)

    if datas_recues:
        print("Message: ", datas_recues.decode())
    else:
        break
    
s.close()
connection_socket.close()