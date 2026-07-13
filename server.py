import socket
import pandas as pd
import time
import builtins
from pyfiglet import Figlet
from rich.console import Console
from rich.progress import Progress
console = Console()
fig = Figlet(font="starwars")
banner = fig.renderText("Hand Cricket")

colors = [
    "red",
    "yellow",
    "green",
    "cyan",
    "blue",
    "magenta",
    "bright_red",
    "bright_green",
    "bright_blue",
]

for i, line in enumerate(banner.splitlines()):
    console.print(f"[bold {colors[i % len(colors)]}]{line}[/]")
with Progress() as progress:
    task = progress.add_task("[cyan]Loading...", total=100)

    while not progress.finished:
        time.sleep(0.05)
        progress.update(task, advance=1)

time.sleep(3)


def print(text, style="white", delay=0.05):
    for char in text:
        console.print(char, style=style, end="")
        time.sleep(delay)
    console.print()
s=socket.socket()
run=[]

s.bind(('', 5050))
s.listen(1)
print('[+] Welcome To Hand Cricket Game',style='bold bright_green')
n_b=input('[+] Enter Your Name: ')
print(f'[+] Server is listening on 5050 ...', style="bold bright_cyan")
conn, addr = s.accept()
print(f'[+] Connection established from {addr[0]}:{addr[1]}', style="bold bright_magenta")
conn.send(n_b.encode())
n_bo=conn.recv(1024).decode()
print(f'[+] This Game is between {n_b} and {n_bo}', style="bold bright_yellow")
while True:
    print('[+] Waiting for bowling from player ...', style="bold cyan")
    data = conn.recv(1024).decode()
    bowl= data
    if not data:
        print("[?] Bowler disconnected.")
        break
   

    
    
    bat=input('[+] Enter your batting number (1-6): ' ,style="bold green")
    if bat not in ['1','2','3','4','5','6']:
        print('[+] Invalid Input')
        conn.close()
        s.close()
        break
    if bat== bowl:
        print('[+] You are OUT!', style="bold white on red")
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
