import socket
from os.path import getsize
BUFFER_SIZE = 1024
port = 8123
ip_addr = "127.0.0.1"
addr = (ip_addr, port)
END_CODE = 'done'

# Open client socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send client to file name and size
file_name = input("Input your file name : ")
file_size = str(getsize(file_name))
socket.sendto(file_name.encode(), addr)
socket.sendto(file_size.encode(), addr)
file_size = int(file_size)

# Open file for read
f = open(file_name, 'rb')

# Start file transmit
print("File transmit start...")
current_size = 0
while current_size < file_size:

    # Read buffer and Send
    data = f.read(BUFFER_SIZE)
    socket.sendto(data, addr)
    current_size = min(current_size+BUFFER_SIZE,file_size)

    # Print state
    print("current_size / total_size = ",current_size,"/",file_size,", ",
          current_size/file_size*100,"%", sep = "")
    
# Close
socket.close()
f.close()
print("ok")
print("file_send_end")


                
