import socket
import time
PORT = 12345
SERVER_IP = "127.0.0.1"  # Localhost IP

def main():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Set up the server address
        server_addr = (SERVER_IP, PORT)

        # Connect to the server
        client_socket.connect(server_addr)
        print("Connected to server")
        time.sleep(3)
        # Receive data from the server
        data = client_socket.recv(1024)  # buffer size of 1024 bytes
        print(f"Received data: {data.decode()}")  # Decode bytes to string

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    main()

