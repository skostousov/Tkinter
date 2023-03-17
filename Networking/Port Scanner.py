from queue import Queue
import socket
import threading

target = "127.0.0.1"
#target = "10.26.202.225"
queue = Queue
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
    
def get_ports(mode):
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 50, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode ==4:
        ports = input("Enter yout ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(ports)
            
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.put(port)
        else:
            print("Port {} is closed!".format(port))
            
def run_scanner(threads, mode):
    get_ports(mode)
    thread_list = []
    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.put(thread)
        
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
        
    print("Open ports are:", open_ports)
    

run_scanner(2, 1)