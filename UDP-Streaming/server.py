import socket

# define the host and port to use
HOST = 'localhost'
PORT = 1235

# define the buffer size
BUFFER_SIZE = 32767

# create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to a specific address and port
server_address = (HOST, PORT)
sock.bind(server_address)


received_bytes = 0
num_messages = 0
while True:
    data, address = sock.recvfrom(BUFFER_SIZE)
    received_bytes += len(data)
    num_messages += 1
    if not data:
        break
print(
    f"Protocol: UDP - Streaming, Messages received: {num_messages}, Bytes received: {received_bytes}")
# close the socket
sock.close()
