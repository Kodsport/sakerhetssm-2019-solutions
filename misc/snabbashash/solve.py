import socket, itertools, telnetlib
from hashlib import md5

s = socket.create_connection(("35.228.2.191", 2010))

def readuntil(msg):
    buf = ""
    while msg not in buf:
        buf += s.recv(1)
    return buf

for _ in range(10):
    readuntil(': ')
    inp = readuntil(': ')
    string = inp[:16]
    hsh = md5(string.encode()).hexdigest()
    print (string + ' -> ' + hsh)
    s.send(hsh+'\n')

t = telnetlib.Telnet()
t.sock = s
t.interact()
