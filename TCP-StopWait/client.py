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

# create a TCP socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


buffer = b'0' * MESSAGE_SIZE

start_time = time.time()
sent_bytes = 0
num_messages = 0
while sent_bytes < MESSAGE_SIZE:
    bytes_to_send = min(BUFFER_SIZE, MESSAGE_SIZE - sent_bytes)
    client_socket.send(buffer[sent_bytes:sent_bytes+bytes_to_send])
    sent_bytes += bytes_to_send
    num_messages += 1

    # wait for an acknowledgement from the server
    response = client_socket.recv(BUFFER_SIZE)

    # if the acknowledgement is not received, re-send the previous chunk
    while response != b'OK':
        client_socket.send(buffer[sent_bytes-bytes_to_send:sent_bytes])
        response = client_socket.recv(BUFFER_SIZE)
        num_messages += 1

end_time = time.time()
print(f"Time: {end_time - start_time}, Messages sent: {num_messages}, Bytes sent: {sent_bytes}")
# close the socket
client_socket.close()
