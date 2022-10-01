import socket
import sys

# This checks for the number of arguments. Should be two, the file name and port number.
# Less than two causes an error message and eh program to close
# I used https://www.geeksforgeeks.org/socket-programming-python/ to help me create this code.
if len(sys.argv) != 2:
    print("Filename or port incorrect. Please enter input as 'filename.py' 'port number'")
    exit(0)

# Code that creates the socket and binds it to an i.p. and host
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = int(sys.argv[1])
server.bind((host, port))
print("\nServer listening on:", ip, "on port:", port)

# Tell the server to listen for a certain number of connections
server.listen(1)

# Will accept an incoming connection to the chat room and print the i.p. of the connecting computer
connection, response = server.accept()
print("Connected by:", response[0])
print("Welcome to Chat", "\nType /q to quite", "\nWaiting for message...")

# Will keep server alive until "/q" is typed
while True:
    message = input(str("Me: "))
    # This is for the /q input. It will send a "left chat" message and close the server.
    if message == "/q":
        message = "Left chat"
        connection.send(message.encode())
        print("\n")
        break
    connection.send(message.encode())
    message = connection.recv(1024)
    message = message.decode()
    print(">", message)

server.close()
