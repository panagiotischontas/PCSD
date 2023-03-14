import socket
import time

# define the host and port to use
HOST = 'localhost'
PORT = 1235

# calculate time
start_time = 0
end_time = 0

# define the size of the buffer used to send data
BUFFER_SIZE = 32767  # use a larger buffer size for faster communication

# define the message size in bytes
MESSAGE_SIZE = 1000 * 1024 * 1024  # 1 GB

# create a TCP socket object and connect it to the server's IP address and port
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# generate data
buffer = b'0' * MESSAGE_SIZE

start_time = time.time()
sent_bytes = 0
num_messages = 0
while sent_bytes < MESSAGE_SIZE:
    bytes_to_send = min(BUFFER_SIZE, MESSAGE_SIZE - sent_bytes)
    client_socket.sendall(buffer[sent_bytes:sent_bytes+bytes_to_send])
    sent_bytes += bytes_to_send
    num_messages += 1
end_time = time.time()
print(f"Time: {end_time - start_time}, Messages sent: {num_messages}, Bytes sent: {sent_bytes}")
# close the socket
client_socket.close()
