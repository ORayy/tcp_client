'''
1) Create a socket: Use socket.socket() to create a TCP/IP socket.
2) Connect to a server: Use connect() to establish a connection to a specific IP address and port.
3) Send data: Use either send() or sendall() to send a message.
4) Receive data: Use recv() to receive a response from the server.
5) Close the connection: Use close() to close the socket when done.
'''

import socket

def tcp_client(target_host, target_port, data):

    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to client
    print(f"Connecting to ip: {target_host} on port: {target_port}")
    client.connect((target_host, target_port))

    # sending some data
    print(f"Sending: {data}")
    client.sendall(data)

    # receive data
    response = client.recv(1024)

    print(response.decode())
    client.close()


# setting the data to be sent/requested (this will be passed in as argument for the data parameter)
http_request = b"GET / HTTP/1.1\r\nHost: scanme.nmap.org\r\n\r\n"

# calling function
tcp_client("scanme.nmap.org" , 80, http_request)