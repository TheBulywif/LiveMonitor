import socket
from _thread import *
import datetime

current_time = datetime.datetime.now()
ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 45826
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)


def filter_name(data):
    data = data.decode('utf-8')
    name = data.split("|", 1)
    print(f"Name: {name[0]}")
    return name


def msg_type_check(data):
    if data.decode.__contains__("Heartbeat"):
        response = "Heartbeat received..."
    else:
        response = "Unknown data...ignoring..."
    return response


def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        print(data)
        if not data:
            break
    connection.close()


try:
    while True:
        Client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(multi_threaded_client, (Client,))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
finally:
    ServerSideSocket.close()
