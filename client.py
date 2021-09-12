
import socket

connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_serveur.connect(('localhost',12800))
print(f"connection etablie avec le serveur")
msg_to_send= b""
while msg_to_send != b"fin" :
    msg_to_send =input(">")
    msg_to_send =msg_to_send.encode()
    connexion_serveur.send(msg_to_send)
    msg_recu = connexion_serveur.recv(1024)
    print(msg_recu.decode())
print("fermeture client")

connexion_serveur.close()
