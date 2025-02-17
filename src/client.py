import socket
import json
from message_handler import parse_code, unparse_code

HOST = "127.0.0.1"
PORT = 65433

def send_message(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(parse_code(message))
        data = s.recv(1024)
        print("data: ", data)
        response = unparse_code(data)
        print("response: ", response)
        
if __name__ == "__main__":
    with open("src/commands.json", "r") as file:
        commands = json.load(file)["commands"]
    
    for msg in commands:
        send_message(msg)
        