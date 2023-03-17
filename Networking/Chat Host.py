import socket
import threading

#Connection data
host = "10.26.203.103"
port = 55555

#Starting server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET: internet socket, #SOCK_STREAM: TCP protocol
server.bind((host, port))
server.listen()

clients = []
nicknames = []

#Send message to all connected clients
def broadcast(message, clientele):
    for client in clients:
        if not clientele:
            client.send(message)
        
#Handle messages from clients
def handle(client):
    while True:
        try:
            #Broadcasting Messages
            message = client.recv(1024)
            broadcast(message, client)
        except:
            #Removing and closing clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast("{} left!".format(nickname).encode("ascii"))
            nicknames.remove(nickname)
            break

def recieve():
    while True:
        #Accept connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        
        #Request and store nickname
        client.send("Nick:".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)
        
        #Print and broadcast nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode("ascii"))
        client.send("Connected to server!".encode("ascii"))
        
        #Start Handling Thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        
recieve()