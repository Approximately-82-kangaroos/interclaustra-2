![Interclaustra 2 logo](https://raw.githubusercontent.com/Approximately-82-kangaroos/interclaustra-2/main/interclaustra.png)

# What is Interclaustra?
Interclaustra is an open-server distributed computing software.
The server takes work requests from many sources at once, distributes them one-at-a-time to its worker nodes, and then returns the value to the proper owner.
# Notes:
 - All pull requests are welcome!
 - If multiple requests are performed from the same IP at once, the data is not guaranteed to be returned in the same order.
 - Sometimes, the server does not properly return the value and instead returns a null string. I'm not sure why this happens.
 - Worker nodes and requester libraries have to be purpose-built by the developers (Docker support when?)
# How does it work?

Step 1: Establish server
 - Server opens socket, listens for connections

Step 2: Establish worker(s)
 - Worker sends "WRK" signal
 - Worker receives problem
 - Worker solves problem
 - Worker sends problem back to server

Step 3: Receive requests from client
 - Client sends "REQ" signal
 - Server sends "ACK" signal
 - Client sends problem
 - Server sends problem to an idle worker node OR stores it for later if all worker nodes are busy
 - Server receives solution from worker
 - Server sends solution to client

On worker disconnect:
 - Worker sends "ERR" signal
 - Server sends "ACK" signal
 - Worker sends problem back to the server
 - Server either stores problem for later if all nodes are busy or sends problem to an idle node.
