#!/usr/bin/env python3

# Network

# ---------

# Open ports?

# what conenctions does it have

# What wifi does it connect to

# what computers does it talk to

# outbound/inbound connections

# firewall?
import psutil, socket, subprocess

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

addrs = psutil.net_if_addrs()

# List interfaces and the network information associated with them

# for gen in addrs.keys():
#     f.write("\n==============================\n")
#     f.write(gen + '\n')
#     f.write("==============================\n")
    
#     for addr in addrs[gen]:
#         if addr.family == psutil.AF_LINK:
#             f.write(f"MAC Address: {addr.address}\n")

#         elif addr.family == socket.AF_INET:
#             f.write(f"IPv4 Address: {addr.address}\n")
#             f.write(f"netmask: {addr.netmask}\n")

#         elif addr.family == socket.AF_INET6:
#             f.write(f"IPv6 Address: {addr.address}\n")

ipinfo=subprocess.Popen(['ipconfig'], stdout=subprocess.PIPE, shell=True).communicate()[0].decode('utf-8')

for line in ipinfo.split('\n'):
    f.write(line.strip()+'\n')


wifi=subprocess.Popen('netsh WLAN show profiles'.split(), stdout=subprocess.PIPE, shell=True).communicate()[0].decode('utf-8')

wifiprofs = [x.strip() for x in wifi.split("    All User Profile     : ")[1:]]

print(wifiprofs)


for prof in wifiprofs:
    f.write("\n\n")
    wifid=subprocess.Popen(['netsh', 'wlan', 'show', 'profile', prof, 'key=clear'], stdout=subprocess.PIPE, shell=True).communicate()[0].decode('utf-8')
    for l in wifid.strip().split('\n'):
        f.write(f"{l.strip()}\n")


conns = psutil.net_connections()

t = {}

def getTransportProto(proto):
    if proto == socket.SOCK_STREAM:
        return "TCP"
    elif proto == socket.SOCK_DGRAM:
        return "UDP"
    else:
        return "Unknown"

for conn in conns:
    if conn.raddr:
        t[str(conn.pid)]=[getTransportProto(conn.type), f"{conn.laddr.ip}:{conn.laddr.port}", f"{conn.raddr.ip}:{conn.raddr.port}"]
    else:
        t[str(conn.pid)]=[getTransportProto(conn.type), f"{conn.laddr.ip}:{conn.laddr.port}"]

f.write("| {:<8} | {:<15} | {:<35} | {:<25} |".format("PID", "ConnType", "Local", "Remote"))

f.write("\n|==========|=================|=====================================|===========================|\n")

for k, v in t.items():
    if len(v) == 3:
        ty, local, remote = v
    else:
        ty, local = v
        remote = ' '

    f.write("| {:<8} | {:<15} | {:<35} | {:<25} |".format(k, ty, local, remote))
    f.write("\n")



