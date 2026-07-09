# 🏏 Online Hand Cricket

<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&pause=1000&color=00C853&center=true&vCenter=true&width=900&lines=Online+Hand+Cricket;Python+Socket+Programming;LAN+Multiplayer+Game;Made+by+Srish+Ghosh">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Socket](https://img.shields.io/badge/Socket-TCP-success?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

<p align="center">
<img src="https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif" width="600">
</p>

---

# 📖 About

Online Hand Cricket is a simple multiplayer cricket game built using Python's built-in **socket** module.

Two players connected over the same Local Area Network (LAN) can play Hand Cricket where:

- One player bats
- One player bowls
- If both choose the same number, the batsman is OUT!
- Every run scored is automatically saved into a CSV file.

This project is perfect for beginners learning:

- Python
- Socket Programming
- Client-Server Architecture
- CSV File Handling
- Networking

---

# ✨ Features

✅ LAN Multiplayer

✅ Client-Server Architecture

✅ Typewriter Console Effect

✅ Player Names

✅ Automatic Score Saving

✅ CSV Output

✅ Beginner Friendly

✅ Lightweight

---

# 🎮 Gameplay

- Server becomes the **Batsman**
- Client becomes the **Bowler**
- Bowler chooses a number from **1–6**
- Batsman also chooses a number from **1–6**
- If both numbers are equal:

```text
OUT!
```

Otherwise,

```text
Run = Batting Number
```

The game continues until the batsman gets OUT.

---

# 📂 Project Structure

```text
Online-Hand-Cricket/
│── server.py
│── client.py
│── requirements.txt
│── README.md
```

---

# 📋 Requirements

- Python 3.8+
- Git
- pip

---

# 📥 Install Git

## Windows

Download Git

https://git-scm.com/download/win

Verify installation

```bash
git --version
```

---

## Ubuntu / Debian

```bash
sudo apt update
sudo apt install git
```

---

## Fedora

```bash
sudo dnf install git
```

---

## Arch Linux

```bash
sudo pacman -S git
```

---

## macOS

```bash
brew install git
```

or

```bash
xcode-select --install
```

---

# 📥 Clone Repository

```bash
git clone https://github.com/developer-srish/Online-Hand-Cricket.git
```

```bash
cd Online-Hand-Cricket
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install pandas
```

---

# ▶️ Running the Project

## Step 1 — Start the Server

```bash
python server.py
```

Example:

```text
Welcome To Hand Cricket Game
Enter Your Name:
Server is listening on 5050...
```

---

## Step 2 — Find Your IP Address

### Windows

```bash
ipconfig
```

Example

```text
IPv4 Address : 192.168.1.5
```

---

### Linux

```bash
ip addr
```

or

```bash
ifconfig
```

---

## Step 3 — Start the Client

```bash
python client.py
```

Example

```text
Enter the server IP address:
```

Enter the server's IP address.

---

# 🏏 How to Play

Both players can only enter:

```text
1
2
3
4
5
6
```

### Example

Bowler

```text
3
```

Batsman

```text
5
```

Result

```text
Your run is 5
```

---

Example 2

Bowler

```text
4
```

Batsman

```text
4
```

Result

```text
OUT!
```

Game Over.

---

# 📁 Output

After the batsman gets OUT, a CSV file is generated.

```text
run.csv
```

Example

| Ball | Run |
|------|----:|
| 1 | 2 |
| 2 | 6 |
| 3 | 1 |
| 4 | 4 |
| 5 | 3 |

---

# 💡 Technologies Used

- 🐍 Python
- 🌐 Socket Programming
- 📊 pandas
- 📄 CSV Files
- 💻 TCP Networking

---

# 📚 What You'll Learn

- Python Sockets
- TCP Communication
- Client-Server Programming
- CSV Handling
- Console Applications
- Multiplayer Game Logic

---

# 🌐 Network Flow

```text
        SERVER
      (Batsman)
           │
           │ TCP Socket
           │
      -------------
           │
           │
        CLIENT
      (Bowler)
```

---

# ⭐ Show Your Support

If you enjoyed this project, consider giving it a ⭐ on GitHub.

It helps support future open-source projects.

---

# 📜 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this project.

---

# 👨‍💻 Author

<p align="center">

## **Srish Ghosh**

Python Developer • Open Source Enthusiast • Student

GitHub:

**https://github.com/developer-srish**

</p>

---

<p align="center">

## ⭐ Don't forget to Star this Repository!

If you enjoyed this project, please give it a ⭐ on GitHub.

<img src="https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif" width="300">

### Made with ❤️ in Python By Srish Ghosh

## Happy Coding! 🚀

</p>
