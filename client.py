
import socket
import time

PORT = 5050
SERVER = "localhost" 
# if you want to use this chat room over the internet then replace the localhost with the public ip address of the machine 
# socket.gethostbyname(socket.gethostname()) this will give the local ip address of the machine which is running the code 
ADDR  = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "[!] DISCONNECTED!"

def connect():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def send(client,msg):
    message=msg.encode(FORMAT)
    client.send(message)

def start():
    answer = input('Would you like to connect (yes/no)?')
    if answer.lower() != 'yes':
        return 
    connection=connect()
    while True:
        msg = input("Message (Press q to quit): ")
        if msg.lower() == 'q':
            break
        send(connection,msg)

    send(connection,DISCONNECT_MESSAGE)
    time.sleep(1)
    print('[!] DISCONNECTED...')

start()
