#! python3

import os

def main():
    banner = """ some banner """
    print("banner")
    print('Users On The System: \n ----------- \n')
    os.system('net users \n')
    print('OS and Version: \n ----------- \n')
    os.system('systeminfo \n')
    print('Installed Programs \n ----------- \n')
    os.system('wmic service list full \n')
    
if __name__ == "__main__":
    main()
# ----------

# Installed programs:

# wmic /output:D:\InstalledSoftwareList.txt product get name,version

# OS/ version?

# winver



# Antivirus??

# Users on the computer

# Superusers

# Admin accounts


# whoami
# net user <username>
# systeminfo
# net config Workstation 
# net users 

# winver
# wmic service list full
# wmic process

# Filesystem:
# tree
# dir /s c:\
