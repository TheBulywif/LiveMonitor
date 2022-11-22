import time
import socket


def heartbeat(x=0):
    server_name = socket.gethostname()
    buffer = ('-' * 80)
    ClientMultiSocket = socket.socket()
    host = '127.0.0.1'
    port = 45826
    print(f'Attempting to connect to server {host}:{port}...')
    try:
        ClientMultiSocket.connect((host, port))
        res = ClientMultiSocket.recv(1024)
        print(f"Connection to {host}:{port} successful...")
        while True:
            message = f'{server_name} | HEARTBEAT'
            ClientMultiSocket.send(str.encode(message))
            res = ClientMultiSocket.recv(1024)
            print(res.decode('utf-8'))
            time.sleep(5)
    except socket.error as e:
        # print(str(e))
        print(f"Connection failed...")
        time.sleep(5)
        heartbeat()
    finally:
        print(f"Finally caught...closing connection...")
        ClientMultiSocket.shutdown(socket.SHUT_WR)
        ClientMultiSocket.close()


if __name__ == '__main__':
    heartbeat()
