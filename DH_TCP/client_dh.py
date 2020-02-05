import socket

ser_ip="192.168.104.44"
ser_host=5606

CS=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

CS.connect((ser_ip,ser_host))

while True:
	p =int(raw_input("enter the value for P"))
	#g =(raw_input("enter the value for G"))
	CS.send(str(p))
	g =int(CS.recv(2048))
	print "Server:- ",g
	if g > 1:      
           for i in range(2, g//2):      
                if (g % i) == 0:
                 print(g, "is not a prime number")
                 break
                else:
                    print(g, "is a prime number")
                    break     
        else:
                print(g, "is not a prime number") 
	
	if g=="bye":
		CS.close()
		break
	
	#msg=CS.recv(2048)
	a=int(raw_input("Alice private key")) 
	print "Alice private key",a
	X=(g**a)%p
	CS.send(str(X))
	Y =int(CS.recv(2048))
	print "Server :- ",Y
	k2=(Y**a)%p
	print (k2)
	break
	#if msg=="bye":
	#	CS.close()
	#	break
		
print("Connection terminated....")
