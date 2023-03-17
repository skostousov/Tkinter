from queue import Queue
import socket
import threading

target = "10.26.202.76"
#target = "127.0.0.1"
#target = "10.26.202.225"
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
    
for port in range(1, 1024):
            queue.put(port)
            
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)
        else:
            print("Port {} is closed!".format(port))
            
def run_scanner(threads):
    thread_list = []
    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)
        
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
        
    print("Open ports are:", open_ports)
    

run_scanner(100)