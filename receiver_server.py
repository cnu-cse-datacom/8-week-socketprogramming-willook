import socket
BUFFER_SIZE = 1024
port = 8123

save_dir = "./data/"

# Open Server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', port))

# Wait for client, client will send file name
file_name, addr = server_socket.recvfrom(BUFFER_SIZE)
file_size, addr = server_socket.recvfrom(BUFFER_SIZE)

# Print file data received from client
print("file recv start from", addr[0])
print(file_name)
print("File Name :",file_name.decode())
print("File Size :",file_size.decode())
file_size = int(file_size.decode())

# Open file for write
f = open(save_dir+file_name.decode(), 'wb')

# Receive file
current_size = 0
while current_size < file_size:

    # Receive buffer and Write
    data, addr = server_socket.recvfrom(BUFFER_SIZE)
    current_size = min(current_size+BUFFER_SIZE,file_size)
    f.write(data)
    
    # Print state
    print("current_size / total_size = ",current_size,"/",file_size,", ",
          current_size/file_size*100,"%", sep = "")

# Close
f.close()
server_socket.close()
print("ok")
print("file_recv_end")
