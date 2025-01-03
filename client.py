import socket
import time
PORT = 12345
SERVER_IP = "127.0.0.1"  
#This python file playes the role of a client server
def main():
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
       
        server_addr = (SERVER_IP, PORT)

       
        client_socket.connect(server_addr)
        print("Connected to server")
        time.sleep(3)
        
        data = client_socket.recv(1024) 
        print(f"Received data: {data.decode()}")  

    except Exception as e:
        print(f"Error: {e}")
    finally:
       
        client_socket.close()

if __name__ == "__main__":
    main()

