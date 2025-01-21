from  socket import *

serSok=socket()

try:
    serSok.bind(('localhost',5000))
    serSok.listen(5)
    print("Server is listening succesfully")
except:
    raise error("Sever Listening Failed")

while True:
    c,addrs=serSok.accept()
    print(f"Following Client Requested to connect sending Succes message {addrs}")
    c.send("Hello To the Segmentation server please, Enter size of the packet".encode());
    PacketSize=c.recv(2048).decode();
    with open ("data.txt",'r') as fs:
        data=fs.read();
    Datalen=len(data)
    NoOfPackets=Datalen//int(PacketSize)+1;
    c.send(f"Server is Starting to send the File of Size {Datalen} in {NoOfPackets} Packets".encode())

    Seg=""
    for i in range(0,Datalen+1):
        if i%int(PacketSize)==0 or i==Datalen:
            print(f"Sent {i} Bytes")
            c.send(Seg.encode())
            Seg="";
            if i==Datalen :
                break;
        Seg+=data[i]
    
    print("All data Sent Closing the Connection")
    c.send("-1".encode())
    c.close()




            

