import socket
import threading
nickname = input("Choose your nickname:")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("10.26.203.103", 55555))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "Nick:":
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("Error!")
            client.close()
            break

def write():
    while True:
        message = "{}: {}".format(nickname, input(''))
        client.send(message.encode("ascii"))
        
recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()