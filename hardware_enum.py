import os, platform, psutil, wmi

c = wmi.WMI()   
my_system = c.Win32_ComputerSystem()[0]

f = open("userHardware.txt", "w+")

f.write(f"System: {platform.system()}\n\
Node: {platform.node()}\n\
Release: {platform.release()}\n\
Version: {platform.version()}\n\
Machine: {platform.machine()}\n\
Processor: {platform.processor()}\n")

f.write(f"\nManufacturer: {my_system.Manufacturer}\n\
Model: {my_system.Model}\n\
Name: {my_system.Name}\n\
NumberOfProcessors: {my_system.NumberOfProcessors}\n\
SystemType: {my_system.SystemType}\n\
SystemFamily: {my_system.SystemFamily}\n")

