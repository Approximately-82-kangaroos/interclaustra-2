import _thread
import socket
import time

problems = []
solutions = []

time1 = time.time()

def onNewClient(client, addr):
    newData = client.recv(1024).strip()
    if newData == b"WRK":
        print(f"Work request: {addr[0]}")
        while True:
            try:
                currentProblem = problems.pop(0)
                client.send(currentProblem.encode("utf-8"))
                data = client.recv(1024).strip().decode("utf-8")
                if data == "ERR":
                    client.send(b"ACK")
                    problems.append(client.recv(1024).strip().decode("utf-8"))
                    client.close()
                    return
                else:
                    solutions.append(data)
                    print(f"New solution: {solutions[-1]}")
                    client.close()
                    return
            except:
                currentProblem = ""
                client.send(currentProblem.encode("utf-8"))
        
    elif newData == b"REQ":
        print(f"Request: {addr[0]}")
        client.send(b"ACK")
        newData = client.recv(1024).strip()
        problems.append(f"{newData.decode('utf-8')}:{addr[0]}")
        print(f"New problem: {problems[-1].split(':')[0]}")
        for i in solutions:
            address = i.split(":")[1]
            if address == "localhost":
                address = "127.0.0.1"
            if address == addr[0]:
                client.send(i.split(":")[0].encode("utf-8"))
                print(f"Sent solution: {i}")
                solutions.remove(i)
                client.close()
                return

HOST = "localhost"
PORT = 42790

server = socket.socket()

server.bind((HOST, PORT))
server.listen(5)

print(f"Server up and running at {HOST}:{PORT}")

if __name__ == "__main__":
    while True:
        client, addr = server.accept()
        print(f"New connection from {addr[0]}\n")
        _thread.start_new_thread(onNewClient, (client, addr))
