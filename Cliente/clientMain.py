from udpConfig import * 

def selectAnProtocol():
    answ = int(input('Seleccione el protocolo: 1- TCP  2-UDP'))
    return answ

def selectActionToSendServer():
    message = input('Ingrese el mensaje para ser enviado al servidor: ')
    return message
    

if __name__ == '__main__':
    client = UDPConfig(12000)
    client.createSocket()
    message = selectActionToSendServer()
    client.sendMessage(message)
    response = client.receiveMessage()
    print(response)
    
