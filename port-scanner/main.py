#
# Made By diverse Lisenced To BanHammer
#

import os
import pyfiglet
import sys
import socket
from datetime import datetime
from colorama import *




target = input('Please enter IPV4 adress: ')


print(f'Target: {target}\nPort Range: 1 - 65535')

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.01)
        result = s.connect_ex((target,port))
        print(f'{Fore.RED}Port {port}|Result : {result} CLOSED')
        if result == 0:
            print(f"{Fore.GREEN}Port {port} is open")
        s.close()

except KeyboardInterrupt:
        print("Exiting...")
        os.system("python main.py")

except socket.gaierror:
        print("Hostname Could Not Be Resolved...")
        os.system("python main.py")

except socket.error:
        print("Server not responding...")
        os.system("python main.py")