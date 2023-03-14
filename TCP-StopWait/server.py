import socket

# define the host and port to use
HOST = 'localhost'
PORT = 1235

# define the buffer size
BUFFER_SIZE = 32767

# create a TCP socket and bind it to the host and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# listen for incoming connections
server_socket.listen()

print(f'Server listening on {HOST}:{PORT}')

# wait for a client to connect
client_socket, client_address = server_socket.accept()
print(f"Client connected from {client_address}")

received_bytes = 0
num_messages = 0
while True:
    data = client_socket.recv(BUFFER_SIZE)
    received_bytes += len(data)
    num_messages += 1

    # send an acknowledgement to the client
    client_socket.send(b'OK')

    if not data:
        break
print(
    f"Protocol: TCP - Stop-Wait, Messages received: {num_messages}, Bytes received: {received_bytes}")
# close the server socket
server_socket.close()
