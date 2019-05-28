#DAns first horrible TCP/UDP client
import socket

#Define variables 
print "Enter a host:",
response_1 = raw_input()
print "Enter a port:",
response_2 = raw_input()
print "enter a request",
response_3 = raw_input()
print "Please select your input method 1.TCP 2.UDP",
response_4 = raw_input()

target_host = str(response_1)
target_port = int(response_2)
request = str(response_3)
conn_method = int(response_4)

if conn_method == "1":
  # create a socket object in TCP we select socket type as SOCK_STREAM
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # connect the client in TCP we first establish a session by connecting to the server using connect
  client.connect((target_host,target_port))
  # send some data in TCP we select to send data uing send
  client.send(request)
  # receive some data
  response = client.recv(4096)
  print response
  
if conn_method == "2":
  # create a socket object in UDP we select socket type as SOCK_DGRAM
  client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  # send some data in UDP we use sendto rather than connect as UDP is a connectionless protocol and include both the payload and destination IP/port
  client.sendto(request,(target_host,target_port))
  #receive some data 
  data, addr = client.recvfrom(4096)
  print data
