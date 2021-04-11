import os, platform, psutil, subprocess

f = open("userHardware.txt", "w+")

f.write("""
==============================================================================================================================================

 __    __       ___      .______       _______  ____    __    ____  ___      .______       _______     _______ .__   __.  __    __  .___  ___. 
|  |  |  |     /   \     |   _  \     |       \ \   \  /  \  /   / /   \     |   _  \     |   ____|   |   ____||  \ |  | |  |  |  | |   \/   | 
|  |__|  |    /  ^  \    |  |_)  |    |  .--.  | \   \/    \/   / /  ^  \    |  |_)  |    |  |__      |  |__   |   \|  | |  |  |  | |  \  /  | 
|   __   |   /  /_\  \   |      /     |  |  |  |  \            / /  /_\  \   |      /     |   __|     |   __|  |  . `  | |  |  |  | |  |\/|  | 
|  |  |  |  /  _____  \  |  |\  \----.|  '--'  |   \    /\    / /  _____  \  |  |\  \----.|  |____    |  |____ |  |\   | |  `--'  | |  |  |  | 
|__|  |__| /__/     \__\ | _| `._____||_______/     \__/  \__/ /__/     \__\ | _| `._____||_______|   |_______||__| \__|  \______/  |__|  |__| 

==============================================================================================================================================                                                                                                                                               
                                                                                                                                               """)
                                                                                                                                               


devicesFile = open("userDevices.txt","+w")

# traverse the info
Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
new = []

# arrange the string into clear info
for item in Id:
	new.append(str(item.split("\r")[:-1]))
for i in new:
	f.write(f"{(i[2:-2])}\n")

serialNum = subprocess.Popen(['wmic','BIOS','get','SERIALNUMBER'], stdout = subprocess.PIPE, shell=True).communicate()[0].decode('utf-8')
gpu = subprocess.Popen(['wmic','path','win32_VideoController','get','name'], stdout = subprocess.PIPE, shell=True).communicate()[0].decode('utf-8')



#Slower run time with filters vvvv
#devices = subprocess.Popen(['powershell','-command','Get-PnpDevice | Sort-Object -Property Name | Where Class -NotLike "Volume" | Where Class -NotLike "System" | ft Class, Name'], stdout = subprocess.PIPE, shell=True).communicate()[0].decode('utf-8')

devices = subprocess.Popen(['powershell','-command','Get-PnpDevice'], stdout = subprocess.PIPE, shell=True).communicate()[0].decode('utf-8')
f.write(f"GPU:                       {gpu[4:].strip()}\n\
Serial:                    {serialNum[12:].strip()}")

diskSpace = psutil.disk_usage("/")

def bytes2GB(x):
    x = x//(1024**3)
    x = int(x)
    return x


f.write(f"\nDisk Storage:\n\
                           Total: {bytes2GB(diskSpace[0])} GB\n\
                           Used: {bytes2GB(diskSpace[0]) - bytes2GB(diskSpace[2])} GB\n\
                           Available: {bytes2GB(diskSpace[2])} GB")

partit = psutil.disk_partitions()                           
f.write(f"\nDisk Partition: {partit}")

devicesFile.write("""
=============================================================================================================
 _______   ___________    ____  __    ______  _______     _______.    _______ .__   __.  __    __  .___  ___. 
|       \ |   ____\   \  /   / |  |  /      ||   ____|   /       |   |   ____||  \ |  | |  |  |  | |   \/   | 
|  .--.  ||  |__   \   \/   /  |  | |  ,----'|  |__     |   (----`   |  |__   |   \|  | |  |  |  | |  \  /  | 
|  |  |  ||   __|   \      /   |  | |  |     |   __|     \   \       |   __|  |  . `  | |  |  |  | |  |\/|  | 
|  '--'  ||  |____   \    /    |  | |  `----.|  |____.----)   |      |  |____ |  |\   | |  `--'  | |  |  |  | 
|_______/ |_______|   \__/     |__|  \______||_______|_______/       |_______||__| \__|  \______/  |__|  |__| 

=============================================================================================================
                                                                                                              """
)

devicesFile.write(f"{devices}")



