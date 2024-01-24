import socket

HOST, PORT = "localhost", 42790
IP = "localhost"

def requestData(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"REQ")
        data2 = s.recv(1024)
        if (data2 == b"ACK"):
            s.sendall(f"{data}:{IP}".encode())
            data = s.recv(1024).strip().decode("utf-8")
    return data

if __name__ == "__main__":
    print(requestData("e81c4e4f2b7b93b481e13a8553c2ae1b"))
