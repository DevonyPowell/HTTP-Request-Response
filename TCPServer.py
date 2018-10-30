# Devony Powell
# March 9, 2018
# Project 1
# Project Description: create a multithreaded webserver that can 
#                      accept request from many different client
# Sources: 
#          Skeleton code (inside of folder submitted): Programming Assignment 1_reference_Python.pdf
#          Textbook: Computer Networking: A Top-Down Approach (6th Edition)
#          External Source:   https://pymotw.com/2/threading/ , http://www.pythonforbeginners.com/system/python-sys-argv

# import modules
from socket import *   # used for socket configurations 
import sys             # used to get arguments on command line 
import threading       # used to create threads for clients

# Function Description: given a file path, find the filename and return it
# Function Name: findFilename
# Argument: filepath 
# Return: filename
def findFilename(filepath):
    paths = filepath.split("/")             # separate the file paths and store it into a list
    index = len(paths)                      # use as an index to find the file in the list
    filename = "/" + str(paths[index-1])    # "/" is needed because of the design of the code
    return filename

# Function Description: given server name and port, send header infomation to client
# Function Name: sendHeader
# Arguments: serverName, severPort 
# Return: void
def sendHeader(serverName, severPort):
    connectionSocket.send(b"HTTP/1.1 200 OK")
    contentType = "\nContent-Type: text/html"
    connectionSocket.send(contentType.encode())
    serverInfo = "\nHost Name: " + serverName
    connectionSocket.send(serverInfo.encode())
    serverPortNumber = "\nServer Port Number: " + str(serverPort)
    connectionSocket.send(serverPortNumber.encode())
    peerName = "\nPeer Name: " + str(connectionSocket.getpeername())
    connectionSocket.send(peerName.encode())
    socketFamily = "\nSocket Family: AF_INET" 
    connectionSocket.send(socketFamily.encode())
    socketType = "\nType: SOCK_STREAM"
    connectionSocket.send(socketType.encode())
    protocol = "\nProtocol: IPPROTO_IP"
    connectionSocket.send(protocol.encode())
    timeout = "\nTimeout: 120 seconds"
    connectionSocket.send(timeout.encode())
    receivedFile = "\nSuccessfully receieved the file\n\n"
    connectionSocket.send(receivedFile.encode())

# Function Description: given the server connection object, find the file requested and send it back to the client 
# Function Name: webserver
# Arguments: connectionSocket 
# Return: true (1) if connection succeed, and false(0) if connection failed
def webserver(connectionSocket):
    while True:
        try:
            message =  connectionSocket.recv(1024)   # recieve message that the client sent
            message = message.decode()               # decode message because the data is coming as a bytes
            print(message)   
            filename = message.split()[1]            # extract the filename from the message sent by client
                
            if filename == '/':                      # if user did not specific a page, display default page (index.htm)
                filename = "/index.htm"
            filename = findFilename(filename)        # find file if there is a path to the file          
            f = open(filename[1:])
            outputdata = f.read()                    # read all the data from the file
                   
            sendHeader(serverName, serverPort)       # send all the header information to the client
              
            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.close() # close client socket
            return 1
        except IOError:
            # Send response message for file not found
            connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")  
            # needed to display in web browser
            browserError = b"<!DOCTYPE html><html><body><h1>HTTP/1.1 404 Not Found</h1></body></html>\r\n" 
            connectionSocket.send(browserError)
            # Close client socket
            connectionSocket.close()    
            return 0

# Prepare a sever socket
serverPort = 8080
serverName = "localhost"
serverSocket = socket(AF_INET,SOCK_STREAM)  # # AF_INET = IPv4, SOCK_STREAM = TCP socket

# check to see if user enters more than one argument on the command line
if len(sys.argv) == 2:
    serverPort = int(sys.argv[1])

if len(sys.argv) > 2:
    print("Too many argument on command line") 
    sys.exit()

serverSocket.bind((serverName,serverPort))  # bind the socket to the local address
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# specify the number of unaccepted connections that the system will allow before refusing new connections
serverSocket.listen(5)

clientThread = []  # accumulate all thread-client inside of this list
while 1:
    # Establish the connection
    print ("Ready to serve on port " + str(serverPort) + "...")
    connectionSocket, addr = serverSocket.accept()
    serverSocket.settimeout(120) # system will timeout after 120 seconds
    t = threading.Thread(target=webserver, args=(connectionSocket,))
    clientThread.append(t)    # append all client to clientThread 
    t.start()   # start process for a client
    t.join()    # wait until server is finish with request to client
serverSocket.close() # close server socket
