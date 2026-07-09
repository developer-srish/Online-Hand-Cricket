import socket
import pandas as pd
import time
import builtins


def print(*args, delay=0.06, end="\n"):
    text = " ".join(str(arg) for arg in args)
    for char in text:
        builtins.print(char, end="", flush=True)
        time.sleep(delay)
    builtins.print(end=end, flush=True)
s=socket.socket()
run=[]

s.bind(('', 5050))
s.listen(1)
print('[+] Welcome To Hand Cricket Game')
n_b=input('[+] Enter Your Name: ')
print(f'[+] Server is listening on 5050 ...')
conn, addr = s.accept()
print(f'[+] Connection established from {addr[0]}:{addr[1]}')
conn.send(n_b.encode())
n_bo=conn.recv(1024).decode()
print(f'[+] This Game is between {n_b} and {n_bo}')
while True:
    print('[+] Waiting for bowling from player ...')
    data = conn.recv(1024).decode()
    bowl= data
    if not data:
        print("[?] Bowler disconnected.")
        break
   

    
    
    bat=input('[+] Enter your batting number (1-6): ')
    if bat not in ['1','2','3','4','5','6']:
        print('[+] Invalid Input')
        conn.close()
        s.close()
        break
    if bat== bowl:
        print('[+] You are OUT!')
        conn.send(b'OUT')
        
        pd.DataFrame(
    {
        "Ball": range(1,len(run)+1),
        "Run": run
    }
).to_csv("run.csv",index=False)
        
        conn.close()
        s.close()
        break
    else:
        run.append(int(bat))
        print(f'[+] Your run is {bat}')
        conn.send(f'Your run is {bat}|NOT OUT'.encode())
        
# Made With Srish Ghosh
# Github:developer-srish