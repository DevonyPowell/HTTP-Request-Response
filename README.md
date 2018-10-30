Name: Devony Powell

Sources: 
      	  Skeleton code (inside of folder submitted): Programming Assignment 1_reference_Python.pdf
          Textbook: Computer Networking: A Top-Down Approach (6th Edition)
          External Source:   https://pymotw.com/2/threading/ , http://www.pythonforbeginners.com/system/python-sys-argv
IDE:     Visual Studio Code


HOW TO RUN THE PROGRAM:

Option 1: default values (filename = index.htm, Port = 8080, Host: localhost)
Step 1: open two terminal windows - one for the web server, and the next for the client
	Note: make sure that the opened terminals are in the directory with the files 

Step 2: compile and run the web server and client
#	a. in the first terminal window, type: python TCPServer.py
	b. in the second terminal window, type: python TCPClient.py

				
Option 2: choose your own values (filename = test.htm, Port = 12000, Host: localhost)
Step 1: open two terminal windows - one for the web server, and the next for the client
	Note: make sure that the opened terminals are in the directory with the files 

Step 2: compile and run the web server and client
	a. in the first terminal window, type: python TCPServer.py 12000
	b. in the second terminal window, type: python TCPClient.py localhost 12000 test.htm
 

Option 3: Using Web Browser as a Client 
Step 1: open one terminal window to run web server
	a. type: python TCPServer.py

Step 2: open your favorite web browser (I used Google Chrome)
	a. type: http://localhost:8080/index.htm
	


