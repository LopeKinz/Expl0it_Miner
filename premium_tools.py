from colorama import *
import json
import ctypes
import os
import time
import sys
import subprocess

version = "v2.0"

ctypes.windll.kernel32.SetConsoleTitleW(f"BanHammer Toolkit {version} Made By BanHammer Team!")


if os.name == 'nt':
        hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
else:
        print("Error while getting Windows HWID")

res = requests.get('https://pastebin.com/raw/sZ123VPy')
hwid = getLisencekey()
if hwid in res.text:
            class Menu:
                def __init__(self):
                    self.fileName = "config.txt" 
                def main(self):
                    logo = f"""{Fore.RESET}
                    ███████████████████████████████████████████████████████████████████████████████████████████████████
                    █▄─▄─▀██▀▄─██▄─▀█▄─▄█─█─██▀▄─██▄─▀█▀─▄█▄─▀█▀─▄█▄─▄▄─█▄─▄▄▀███─▄─▄─█─▄▄─█─▄▄─█▄─▄███▄─█─▄█▄─▄█─▄─▄─█
                    ██─▄─▀██─▀─███─█▄▀─██─▄─██─▀─███─█▄█─███─█▄█─███─▄█▀██─▄─▄█████─███─██─█─██─██─██▀██─▄▀███─████─███
                    ▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▀▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▄▀▀
                    """
                    main_menu = f"""{Fore.RESET}
                                                +------------+---------+----------+
                                                |   Tools    | Version | Working? |
                                                +============+=========+==========+
                                                | Ping       |     1.0 | No       |
                                                | Portscan   |     1.0 | YES      |
                                                | UserFinder |     1.0 | YES      |
                                                | NitroGen   |     1.0 | YES      |
                                                | GiftCard   |     1.0 | YES      |
                                                |DC ACC Nuker|     1.0 | YES      |
                                                |CS:GO hacks |     1.0 | YES      |
                                                +------------+---------+----------+
                    """
                    
                    self.slowType(logo, 0.00001, False)
                    self.slowType(main_menu, 0.00001, False)
                    input_command = input("\n> ")
                    self.console(command = input_command)
                def reopen_console(self):
                    command = input("\n> ")
                    self.console(command=command)
                def slowType(self, text, speed, newLine = True):
                        for i in text:
                            print(i, end = "", flush = True)
                            time.sleep(speed)
                        if newLine:
                            print()
                            
                def console(self,command):
                    if command == 'help':
                        print("""
                        Commands:
                        ping - Ping a host
                        portscan - Scan for ports
                        userfinder - Find users on websites
                        nitrogen - Generate nitro codes and checks them
                        BTCStealer - Steal BTC
                        giftcard - Generate gift cards
                        dcaccnuker - Nuke discord accounts
                        csgohacks - CS:GO hacks
                        help - Show this help
                        clear - Clear the console
                        exit - Exit the console
                        
                        """)
                        self.reopen_console()
                    if command == 'ping':
                        self.reopen_console()
                    if command == 'portscan':
                        os.system("python port-scanner/main.py")
                    if command == 'BTCStealer':
                        print("BTCStealer is currently not working")
                        self.reopen_console()
                    if command == 'clear':
                        os.system('cls')
                        self.main()
                    if command == 'exit':
                        exit()
                    if command == 'userfinder':
                        username = input("Username to find: ")
                        os.system(f'python user-finder/sherlock/sherlock.py {username}')
                    if command == 'nitrogen':
                        print("NitroGen is currently not working")
                        self.reopen_console()
                    if command == 'giftcard':
                        os.system("python giftcardgen/main.py")
                    if command == 'dcaccnuker':
                        os.system("python accnuker/main.py")
                    if command == 'csgohacks':
                        os.system("python csgoesp/main.py")
            if __name__ == '__main__':
                menu = Menu()
                menu.main()
        else:
            print("Invalid License Key")


