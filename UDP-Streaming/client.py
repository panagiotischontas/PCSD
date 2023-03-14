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

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generate a fixed amount of random data to send
data_to_send = b'0' * MESSAGE_SIZE

start_time = time.time()
packets_sent = 0
sent_bytes = 0
while sent_bytes < MESSAGE_SIZE:
    bytes_to_send = min(BUFFER_SIZE, MESSAGE_SIZE - sent_bytes)
    client_socket.sendto(
        data_to_send[sent_bytes:sent_bytes+bytes_to_send], (HOST, PORT))
    sent_bytes += bytes_to_send
    packets_sent += 1
end_time = time.time()
print(f"Time: {end_time - start_time}, Messages sent: {packets_sent}, Bytes sent: {sent_bytes}")
# close the socket
client_socket.close()
