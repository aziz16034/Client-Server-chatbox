import socket

ob = socket.socket()
ob.bind(('144.89.207.190', 2301))

ob.listen(4)
clientobject,add =ob.accept()
print("server ready to accept connection")
print('connected with this address', add)

'''gotmsg = clientobject.recv(1024)
gotmsg.decode('utf-8')
print(gotmsg)
#ob.close()'''


conn = True
while conn:
    gotmsg = clientobject.recv(1024)
    gotmsg.decode('utf-8')
    print(gotmsg)

    if len(gotmsg) ==0:
        comm = False
        ob.close()




