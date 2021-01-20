import socket
import pandas as pd
 
file = pd.read_csv('data.csv')
localIP     = "127.0.0.1"

localPort   = 20001

bufferSize  = 1024

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    info=message.split("/")
    rslt_df = file[file['Section'] == info[1]]
    if info[0]=="FETCH":
	if len(rslt_df)!=0:
    		msgFromServer   = str(rslt_df.iloc[0][info[2]])
	else:
		msgFromServer   = "Data not available"
    else:
	msgFromServer   = str(info[3])
 	if len(file[file['Section'] == info[1]])!=0:
		file.loc[list(rslt_df.index)[0],info[2]]=info[3]
                file.to_csv ("data.csv", index = False, header=True)
        else:
		file=file.append({'Section' : info[1] , info[2] :info[3]} , ignore_index=True)
		file.to_csv ("data.csv", index = False, header=True)
    

    address = bytesAddressPair[1]
	#change
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

   

    # Sending a reply to client
    

    bytesToSend         = str.encode(msgFromServer)

    UDPServerSocket.sendto(bytesToSend, address)
