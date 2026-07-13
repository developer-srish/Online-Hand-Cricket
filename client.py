import builtins
import socket
import pandas as pd
import time
import builtins
s=socket.socket()
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

bo_c=['1','2','3','4','5','6']
IP=input('[+] Enter the server IP address: ')
s.connect((IP,5050))
n_b=s.recv(1024).decode()
n_bo=input('[+] Enter Your Name: ')
s.send(n_bo.encode())
print(f'[+] This Game is between {n_b} and {n_bo}', style="bold bright_yellow")
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
    
