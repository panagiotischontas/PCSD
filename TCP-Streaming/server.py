import socket

# define the host IP and port number
HOST = 'localhost'
PORT = 1235

# define the size of the buffer used to receive data
BUFFER_SIZE = 32767  # use a larger buffer size for faster communication

# create a TCP socket object and bind it to the host IP and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# set the socket to listen for incoming client connections
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}...")

# accept a client connection request and create a new socket for the client
client_socket, client_address = server_socket.accept()
print(f"Client connected from {client_address}")

received_bytes = 0
num_messages = 0
while True:
    data = client_socket.recv(BUFFER_SIZE)
    received_bytes += len(data)
    num_messages += 1
    if not data:
        break
print(
    f"Protocol: TCP - Streaming, Messages received: {num_messages}, Bytes received: {received_bytes}")
# close the sockets
server_socket.close()
