import socket

HOST = 'localhost'  # Replace with the IP address of your server
PORT = 12345  # Replace with a free port number on your server

BUFFER_SIZE = 32753  # Replace with the size of the buffer you want to use

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Server started on {HOST}:{PORT}")

received_bytes = 0
num_messages = 0
while True:
    data, client_address = server_socket.recvfrom(BUFFER_SIZE)
    received_bytes += len(data)
    num_messages += 1

    # Send an acknowledgement
    server_socket.sendto(b"OK", client_address)

    if not data:
        break
print(
    f"Protocol: UDP - StopWait, Messages received: {num_messages}, Bytes received: {received_bytes}")
# close the server socket
server_socket.close()
