# Devony Powell
# March 9, 2018
# Project 1
# Project Description: create a client to accept and display response from a webserver
# Sources: 
#          Skeleton code (inside of folder submitted): Programming Assignment 1_reference_Python.pdf
#          Textbook: Computer Networking: A Top-Down Approach (6th Edition)
#          External Source:   https://pymotw.com/2/threading/ , http://www.pythonforbeginners.com/system/python-sys-argv

from socket import *    # used for socket configurations 
import sys              # used to get arguments on command line
import time             # used to find current time

# Function Description: given server name and port, send header infomation to client
# Function Name: sendHeader
# Arguments: serverName, severPort 
# Return: void
def sendHeader(serverName, serverPort):
    serverInfo = "\nHost Name: " + serverName
    clientSocket.send(serverInfo.encode())
    serverPortNumber = "\nServer Port Number: " + str(serverPort)
    clientSocket.send(serverPortNumber.encode())
    peerName = "\nPeer Name: " + str(clientSocket.getpeername())
    clientSocket.send(peerName.encode())
    socketFamily = "\nSocket Family: AF_INET" 
    clientSocket.send(socketFamily.encode())
    socketType = "\nType: SOCK_STREAM"
    clientSocket.send(socketType.encode())
    protocol = "\nProtocol: IPPROTO_IP\n"
    clientSocket.send(protocol.encode())
    timeout = "Timeout: 120 seconds\n"
    clientSocket.send(timeout.encode())

# default parameters
defaultFile = "index.htm"   # use this file when it is not provided
defaultPort = 8080          # use this port when it is not provided
serverPort = defaultPort
serverName = "localhost"
requestedFile = defaultFile

if len(sys.argv) > 4:
    print("Too many argument on command line") 
    sys.exit()

if len(sys.argv) == 4:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])
    requestedFile = str(sys.argv[3])

if len(sys.argv) == 3:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])

if len(sys.argv) == 2:
    serverName = sys.argv[1]

if len(sys.argv) == 1:
    print("Client has default values...\n")

clientSocket = socket(AF_INET, SOCK_STREAM)  # AF_INET = IPv4, SOCK_STREAM = TCP socket
clientSocket.connect((serverName, serverPort)) # connects the client and the server together 
# now that we have the client and the server connected, we can then send and receive messages
statusLine =  "GET /" + requestedFile + " HTTP/1.1"
sentTime = time.time()  # time stamp when the first packet was sent out
clientSocket.send(statusLine.encode()) # waits here until server respond
sendHeader(serverName, serverPort)     # send header lines to server

responseData = clientSocket.recv(1024) # recieve the bytes from the server
receivedTime = sentTime = time.time()  # record the time when the client received a respond
RTT = round(receivedTime - sentTime,3) # roundtrip time for packet to send to the server and back to the client 
print("RTT: ", RTT)
responseData = responseData.decode()   # data is in bytes, so decode so that it can be used

while responseData:
    print(responseData, end = '')
    responseData = clientSocket.recv(1024)
    responseData = responseData.decode()
clientSocket.close()  # close the socket since we are done using it
