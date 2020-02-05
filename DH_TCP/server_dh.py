import socket

server_port=5606
server_ip="localhost" #192.168.104.115 pass server ip address or write "localhost" to run on same machine

SS=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
SS.bind((server_ip,server_port))

SS.listen(5)

con, addr=SS.accept()

while True:
     p = int(con.recv(2048))
     print("Bob send P: ", p)      
     if p > 1:
          for i in range(2, p//2):
               if (p % i) == 0:
                    print(p, "is not a prime number")
                    break
               else:
                    print(p, "is a prime number")
                    break
     else:
          print(p,"is not a prime number")
     g=int(raw_input("Enter value of G : "))
     con.send(str(g))
     
     x=int(con.recv(2048))
     b=int(raw_input("Enter Bob private number b : "))
     y=((g**b)%p)
     #print("y : ",y)
     con.send(str(y))#Sending calculated value of Y to Alice
     k1=(x**b)%p
     print(" Secret Key is",k1)   
     break  
"""     if msg=="bye":
          SS.close()
          break

     msg=raw_input("You:- ")
     con.send(msg)
     if msg=="bye":
          SS.close()
          break
"""
print("Connection terminated....")
