from socket import *

clientSock=socket()

clientSock.connect(("localhost",5000))

print(clientSock.recv(2048).decode())
clientSock.send(input().encode())

data=''
Seg=''
while True:
    Seg=clientSock.recv(2048).decode()
    if Seg=='-1':
        break;
    data+=Seg;
    print(Seg)
    Seg=''

print(f"Final Data recieced is {data}")
clientSock.close()