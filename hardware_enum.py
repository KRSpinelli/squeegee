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


gpu = subprocess.Popen(['wmic','path','win32_VideoController','get','name'], stdout = subprocess.PIPE, shell=True).communicate()[0].decode('utf-8')
f.write(f"GPU:                       {gpu[4:].strip()}")

