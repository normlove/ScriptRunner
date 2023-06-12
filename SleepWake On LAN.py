import socket
import subprocess
import tkinter as tk
from tkinter import messagebox

def send_wol_packet(ip_address):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set socket options to enable broadcasting
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Create a magic packet
    mac_bytes = b'\xFF' * 6
    magic_packet = mac_bytes + (mac_bytes * 16)

    # Send the magic packet to the target IP address
    sock.sendto(magic_packet, (ip_address, 9))

    # Close the socket
    sock.close()

def check_pc_status(ip_address):
    while True:
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Set a timeout of 1 second
            sock.settimeout(1.0)

            # Attempt to connect to the target IP address
            result = sock.connect_ex((ip_address, 135))

            # Check if the connection was successful (PC is awake)
            if result == 0:
                messagebox.showinfo("PC Awake", "The PC at {} is awake!".format(ip_address))
                break

            # Close the socket
            sock.close()
        except socket.error:
            pass

def hibernate_pc():
    # Execute the command to hibernate the PC
    subprocess.call("shutdown /h", shell=True)

# Create the GUI window
window = tk.Tk()
window.title("Wake-on-LAN")

# Function to handle button click event
def send_wol():
    # Get the IP address from the user
    ip_address = entry.get()

    # Send the Wake-on-LAN packet
    send_wol_packet(ip_address)

    # Start checking the PC status
    check_pc_status(ip_address)

# Create a label and an entry field
label = tk.Label(window, text="Enter the IP address:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create a button to send the Wake-on-LAN packet
wol_button = tk.Button(window, text="Send Wake-on-LAN", command=send_wol)
wol_button.pack()

# Create a button to hibernate the PC
hibernate_button = tk.Button(window, text="Hibernate PC", command=hibernate_pc)
hibernate_button.pack()

# Start the GUI event loop
window.mainloop()
