import socket
import time

# define the host and port to use
HOST = 'localhost'
PORT = 1235

# calculate time
start_time = 0
end_time = 0

# define the buffer size
BUFFER_SIZE = 32767

# define the message size to send (in bytes)
MESSAGE_SIZE = 2000 * 1024 * 1024  # 2 GB

# Generate some test data
buffer = b'0' * MESSAGE_SIZE
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

start_time = time.time()
sent_bytes = 0
num_messages = 0
for i in range(0, len(buffer), BUFFER_SIZE):
    chunk = buffer[i:i+BUFFER_SIZE]
    while True:
        client_socket.sendto(chunk, (HOST, PORT))
        sent_bytes += len(chunk)
        num_messages += 1
        response, server_address = client_socket.recvfrom(BUFFER_SIZE)
        if response == b"OK":
            break

elapsed_time = time.time() - start_time
print(
    f"Time: {elapsed_time}, Messages sent: {num_messages}, Bytes sent: {sent_bytes}")
# close the socket
client_socket.close()
