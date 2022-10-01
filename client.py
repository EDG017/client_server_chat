import socket
import sys

# This checks for the number of arguments. Should be two, the file name and port number.
# Less than two causes an error message and the program to close
# I used https://www.geeksforgeeks.org/socket-programming-python/ to help me create this code.
if len(sys.argv) != 2:
    print("Filename or port incorrect. Please enter input as 'filename.py' 'port number'")
    exit(0)

# Code that creates the socket and connects it the computer listening on the i.p. and port number passed
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = int(sys.argv[1])
host = socket.gethostname()
ip = socket.gethostbyname(host)
client.connect((host, port))

# Prints prompts telling client what i.p. and port they are connected to and welcoming them to the chat room.
# For this project the client will connect to localhost i.p.
print("\nConnected to:", ip, "on port:", port)
print("Welcome to Chat", "\nType /q to quite", "\nWaiting for message...")

# Will keep client alive until "/q" is typed
while True:
    message = client.recv(1024)
    message = message.decode()
    print(">", message)
    message = input(str("Me: "))
    # This is for the /q input. It will send a "left chat" message and close the client.
    if message == "/q":
        message = "Left chat"
        client.send(message.encode())
        print("\n")
        break
    client.send(message.encode())

client.close()
