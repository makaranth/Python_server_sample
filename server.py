import socket

PORT = 12345
print("What do you want to send to the client?")
print("""1) Message
2) Flag""")
res = input("> ")
if res == "1":
    FLAG = input("Enter the message to send: ")

    res = "Message"
elif res == "2":
    print("Sending the flag")
    FLAG = "CyberForgers{network_traffic_is_fun}"
    res = "Flag"
else:
    print("Wrong option choosen, try again...")
    exit()
def main():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set up the server address
    server_addr = ('', PORT)  # '' means INADDR_ANY (listens on all interfaces)
    
    try:
        # Bind the socket to the address and port
        server_socket.bind(server_addr)
        
        # Listen for incoming connections
        server_socket.listen(5)
        print(f"Server listening on port {PORT}...")
        
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        
        # Send the flag to the client
        client_socket.send(FLAG.encode())  # Ensure the flag is sent as bytes
        print(f"{res} sent to client")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the sockets
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    main()

