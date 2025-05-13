import socket

host = "127.0.0.1"  # Replace with your server IP if different
port = 7777

s = socket.socket()
s.connect((host, port))

# Get difficulty prompt
difficulty_msg = s.recv(1024).decode().strip()
print(difficulty_msg)

# Choose difficulty
difficulty = "2"  # Bot picks Medium
s.sendall(difficulty.encode())

# Set guessing range
if difficulty == "1":
    low, high = 1, 10
elif difficulty == "2":
    low, high = 1, 50
else:
    low, high = 1, 100

# Receive banner
banner = s.recv(1024).decode().strip()
print(banner)

# Start guessing using binary search
while True:
    guess = (low + high) // 2
    print(f"[BOT] Guessing: {guess}")
    s.sendall(str(guess).encode())
    
    reply = s.recv(1024).decode().strip()
    print(f"[SERVER] {reply}")
    
    if "CORRECT!" in reply:
        break
    elif "Higher" in reply:
        low = guess + 1
    elif "Lower" in reply:
        high = guess - 1

s.close()
