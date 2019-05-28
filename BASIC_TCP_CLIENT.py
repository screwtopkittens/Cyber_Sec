#DAns first horrible TCP client
import socket


#Define variables 
print "Enter a host:",
response_1 = raw_input()
print "Enter a port:",
response_2 = raw_input()
print "enter a request",
response_3 = raw_input()

target_host = str(response_1)
target_port = int(response_2)
request = str(response_3)

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client
client.connect((target_host,target_port))
# send some data
client.send(request)
# receive some data
response = client.recv(4096)
print response
