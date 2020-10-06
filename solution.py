# import socket module
#Web server should accept and parse the HTTP request
#Get the requested file from the server's filesystem
#create an HTTP response message consisting of the requested file preceded by header lines
#not found equals 404, found equals 200, and so on
from socket import *
import sys  # In order to terminate the program


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    port=13331
    serverSocket.bind(("", port))
    serverSocket.listen(1)


    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() # Fill in start      #Fill in end
        try:
            message = connectionSocket.recv(2048).decode()  # Fill in start    #Fill in end
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read() # Fill in start     #Fill in end

            # Send one HTTP header line into socket
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())



            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            connectionSocket.send("HTTP/1.1 404 NOT FOUND\r\n\r\n 404 not found".encode())
            connectionSocket.close()


    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)



