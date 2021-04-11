#!/usr/bin/env python3

# Network

# ---------

# Open ports?

# what conenctions does it have

# What wifi does it connect to

# what computers does it talk to

# outbound/inbound connections

# firewall?
import psutil, socket

f = open("network_enum.txt", "w+")

f.write("""
.__   __.  _______ .___________.____    __    ____  ______   .______       __  ___     _______ .__   __.  __    __  .___  ___. 
|  \ |  | |   ____||           |\   \  /  \  /   / /  __  \  |   _  \     |  |/  /    |   ____||  \ |  | |  |  |  | |   \/   | 
|   \|  | |  |__   `---|  |----` \   \/    \/   / |  |  |  | |  |_)  |    |  '  /     |  |__   |   \|  | |  |  |  | |  \  /  | 
|  . `  | |   __|      |  |       \            /  |  |  |  | |      /     |    <      |   __|  |  . `  | |  |  |  | |  |\/|  | 
|  |\   | |  |____     |  |        \    /\    /   |  `--'  | |  |\  \----.|  .  \     |  |____ |  |\   | |  `--'  | |  |  |  | 
|__| \__| |_______|    |__|         \__/  \__/     \______/  | _| `._____||__|\__\    |_______||__| \__|  \______/  |__|  |__| 


==============================================================================================================================

    """)

f.write("LIST OF INTERFACES // IP ADDRS")

addrs = psutil.net_if_addrs()

# List interfaces and the network information associated with them

for gen in addrs.keys():
    f.write("\n==============================\n")
    f.write(gen + '\n')
    f.write("==============================\n")
    
    for addr in addrs[gen]:
        if addr.family == psutil.AF_LINK:
            f.write(f"MAC Address: {addr.address}\n")

        elif addr.family == socket.AF_INET:
            f.write(f"IPv4 Address: {addr.address}\n")
            f.write(f"netmask: {addr.netmask}\n")

        elif addr.family == socket.AF_INET6:
            f.write(f"IPv6 Address: {addr.address}\n")
