import socket                   

s = socket.socket()
port = 6000                                
s.bind(('', port))
s.listen(5)                     

print ("Server listening.......")

while True:
    conn, addr = s.accept()     
    print ("Dapat Connection daripada", addr)
    
    filename='test.txt'
    file = open(filename, 'wb')
    print('Sedang menerima data...')
    data = conn.recv(1024)
    file.write(data)            

    file.close()
    print('Berjaya dapatkan file!')
    conn.close()
    s.close()
