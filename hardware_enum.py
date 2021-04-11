import os, platform, psutil, wmi, subprocess

c = wmi.WMI()   
my_system = c.Win32_ComputerSystem()[0]

f = open("userHardware.txt", "w+")

# traverse the info
Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
new = []

# arrange the string into clear info
for item in Id:
	new.append(str(item.split("\r")[:-1]))
for i in new:
	f.write(f"{(i[2:-2])}\n")

f.write(f"Disk Partitions: {psutil.disk_partitions()}\n\n\
NIC: {psutil.net_if_stats()}")
