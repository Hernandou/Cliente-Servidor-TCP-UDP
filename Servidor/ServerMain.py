from udpServerConfig import * 


if __name__ == '__main__':
    server = UDPServer(12000)
    server.createSocket()
    server.receiveMessage()