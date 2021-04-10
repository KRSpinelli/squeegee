#!/usr/bin/env python3

# Network

# ---------

# Open ports?

# what conenctions does it have

# What wifi does it connect to

# what computers does it talk to

# outbound/inbound connections

# firewall?
import psutil

print("""
.__   __.  _______ .___________.____    __    ____  ______   .______       __  ___     _______ .__   __.  __    __  .___  ___. 
|  \ |  | |   ____||           |\   \  /  \  /   / /  __  \  |   _  \     |  |/  /    |   ____||  \ |  | |  |  |  | |   \/   | 
|   \|  | |  |__   `---|  |----` \   \/    \/   / |  |  |  | |  |_)  |    |  '  /     |  |__   |   \|  | |  |  |  | |  \  /  | 
|  . `  | |   __|      |  |       \            /  |  |  |  | |      /     |    <      |   __|  |  . `  | |  |  |  | |  |\/|  | 
|  |\   | |  |____     |  |        \    /\    /   |  `--'  | |  |\  \----.|  .  \     |  |____ |  |\   | |  `--'  | |  |  |  | 
|__| \__| |_______|    |__|         \__/  \__/     \______/  | _| `._____||__|\__\    |_______||__| \__|  \______/  |__|  |__| 


==============================================================================================================================

    """)

print("LIST OF INTERFACES // IP ADDRS")

addrs = psutil.net_if_addrs()

# List interfaces and the network information associated with them

for gen in addrs.keys():
    print("\n==============================")
    print(gen)
    print("==============================")
    
    for addr in addrs[gen]:
        if addr.family == "AddressFamily.AF_LINK":
            print("MAC Address: %s" % addr.address)

        elif addr.family == "AddressFamily.AF_INET":
            print("IPv4 Address: %s" % addr.address)
            print("netmask: %s" % addr.netmask)

        elif addr.family == "AddressFamily>AF_INET6":
            print("IPv6 Address: %s" % addr.address)
