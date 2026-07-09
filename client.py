import builtins
import socket
import pandas as pd
import time
import builtins
s=socket.socket()
def print(*args, delay=0.06, end="\n"):
    text = " ".join(str(arg) for arg in args)
    for char in text:
        builtins.print(char, end="", flush=True)
        time.sleep(delay)
    builtins.print(end=end, flush=True)
bo_c=['1','2','3','4','5','6']
IP=input('[+] Enter the server IP address: ')
s.connect((IP,5050))
n_b=s.recv(1024).decode()
n_bo=input('[+] Enter Your Name: ')
s.send(n_bo.encode())
print(f'[+] This Game is between {n_b} and {n_bo}')
while True:
    bowl=input('[+] Enter your bowling number (1-6): ')
    if bowl not in bo_c:
        print('[+] Invalid Input')
        s.close()
        break
    
    
    
    s.send(bowl.encode())
    bat=s.recv(1024).decode()
    print(f'[+] Server says: {bat}')
    
    if bat=='OUT':
        s.close()
        break
    
