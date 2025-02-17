import socket
from message_handler import unparse_code, parse_code
from vehicle import Vehicle

HOST = "127.0.0.1" 
PORT = 65433

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server is listening on {HOST}:{PORT}")
        
        vehicle = Vehicle(speed= 0, direction= "straight")
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if not data:
                    break
                
                message = unparse_code(data)
                response = vehicle.command(message)
                
                conn.sendall(parse_code(response))
                
if __name__ == "__main__":
    start_server()
        