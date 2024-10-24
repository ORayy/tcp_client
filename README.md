# TCP Client

                 _______                         _______
                |       |                       |       |
                |  TCP  |                       |  TCP  |
                |Client | ====================> |Server |
                |_______|  Request (Send Data)  |_______|
                      ||                            ||
                      ||<===========================||
                          Response (Receive Data)


## Overview

This is a simple TCP client implemented in Python. It demonstrates how to:
1. Create a TCP socket.
2. Connect to a server.
3. Send data to the server.
4. Receive a response from the server.
5. Close the connection.

The client connects to the server, sends an HTTP GET request, receives the server's response, and prints it to the console.

## How to Use

### Prerequisites

You need to have **Python 3** installed on your system. You can check your Python version with:

```bash
python --version


####  Instructions
1) Clone this repository or download the Python file (tcp_client.py).
2) Modify the target_host, target_port, and data variables inside the script if necessary.
3) Run the TCP client script using Python:
4) python tcp_client.py


Example Usage
You can use the following HTTP request as data to be sent to the server:

http_request = b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"

To call the function and connect to the target server:
tcp_client("example.com", 80, http_request)

Output
The TCP client will output the following:

1) The connection status.
2) The data being sent.
3) The response received from the server.
4) The confirmation of the connection being closed.

Example:
Connecting to example.com on port 80
Sending: b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'
Received Response:
HTTP/1.1 200 OK
...
Closing the connection

Code Structure
tcp_client():
Creates a TCP socket.
Connects to a server.
Sends a message (sendall()).
Receives the server's response (recv()).
Closes the socket.
License
This project is open source and free to use.


---

