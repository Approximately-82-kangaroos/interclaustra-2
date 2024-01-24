import hashlib
import random
import socket
import string

HOST, PORT = "localhost", 42790

def genRandomString(length):
    return ''.join(random.choice(string.printable) for i in range(length))

def md5(inputString):
    return hashlib.md5(inputString.encode('utf-8')).hexdigest()

def crackHash(hash):
    stringToHash = genRandomString(2)
    while md5(stringToHash) != hash:
        stringToHash = genRandomString(2)
    return stringToHash

connected = True

while connected is True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes("WRK", "utf-8"))
        data = sock.recv(1024).decode("utf-8")
        if data != "":
            ip = data.split(":")[1]
            data = data.split(":")[0]
            try:
                sock.sendall(bytes(f"{crackHash(data)}:{ip}", "utf-8"))
            except:
                sock.sendall(bytes("ERR", "utf-8"))
                data2 = sock.recv(1024).strip()
                if data2 == b"ACK":
                    connected = False
                    sock.sendall(bytes(f"{data}:{ip}", "utf-8"))
                    sock.close()
        else:
            sock.close()
