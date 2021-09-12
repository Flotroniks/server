# Définition d'un serveur réseau rudimentaire
# Ce serveur attend la connexion d'un client
 
import socket

host = ""
port = 12800

connexion_principale =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((host, port))
connexion_principale.listen(5)
print(f'Le serveur ecoute sur le port {port}')

connexion_client, infos_connexion = connexion_principale.accept()
msg_recu =b""
while msg_recu != b"fin" :
    msg_recu = connexion_client.recv(1024)
    print(msg_recu.decode())
    connexion_client.send(b"5 / 5")
print("fermeture de la connexion")
connexion_client.close()
connexion_principale.close
