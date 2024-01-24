![Interclaustra 2 logo](https://raw.githubusercontent.com/Approximately-82-kangaroos/interclaustra-2/main/interclaustra.png)

# What is Interclaustra?
Interclaustra is an open-server distributed computing software.
The server takes work requests from many sources at once, distributes them one-at-a-time to its worker nodes, and then returns the value to the proper owner.
# Notes:
 - All pull requests are welcome!
 - If multiple requests are performed from the same IP at once, the data is not guaranteed to be returned in the same order.
 - Sometimes, the server does not properly return the value and instead returns a null string. I'm not sure why this happens.
 - Worker nodes and requester libraries have to be purpose-built by the developers (Docker support when?)
