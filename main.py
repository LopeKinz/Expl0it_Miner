from colorama import init, Fore, Back, Style
from addons import generate, check, visual
import time
from tkinter import * 
import os
import subprocess
import requests
import webbrowser

init(convert=True)

w = Tk()

def callback(url):
    webbrowser.open_new(url)

def getLisencekey():
    if os.name == 'nt':
        return (
            subprocess.check_output('wmic csproduct get uuid')
            .decode()
            .split('\n')[1]
            .strip()
        )
    else:
        return("Error while getting Windows HWID")


def checkhwid():
    res = requests.get('https://pastebin.com/raw/sZ123VPy')
    hwid = getLisencekey()
    return hwid in res.text


def f():
    while True:
        adress = generate.gen_adress()
        check_results = check.check_adress(adress)
        visual.print_results(adress, check_results)

def prem():
    premi = checkhwid()
    if premi == True:
        try:
            print("Loading file.txt...")
            with open("file.txt", "r") as infile:
                while True:
                    for line in infile:
                        a = line.replace("\r", "")
                        b = a.replace("\n", "")
                        check_results = check.check_adress(b)
                        visual.print_results(b, check_results)
        except:
            print("Error while loading file.txt")
    if premi == False:
        print("You are not premium")
    else:
        print(premi)

def prem_stuff():
    premi = checkhwid()
    if premi == True:
        try:
            os.system("python premium_tools.py")
        except:
            os.system("python3 premium_tools.py")
    if premi == False:
        print("You are not premium")
    else:
        print(premi)

def gui():
    w.wm_iconbitmap('EXM.ico')
    w.title("Exploit Miner")
    title1 = Label(w, text="Expl0it Miner", font=("Terminal"))
    title1.config(font=("Courier", 44))
    install_requirements = Button(w, text="Free Miner", command = f)
    startapi_btn = Button(w, text = "Premium Miner", command = prem)
    stuff = Button(w, text= ("Premium Tools"), command = prem_stuff)
    hwid = Label(
        w,
        text=f"HWID: {getLisencekey()}"
        + '\n'
        + 'Premium: '
        + str(checkhwid()),
    )
    credit = Label(w, text="By Pinkyhax & Banhammer")
    discord = Label(w, text="Buy Premium Here : https://discord.gg/gWHyq7B7ss", fg="blue", cursor="hand2")
    title1.pack()
    install_requirements.pack()
    startapi_btn.pack()
    stuff.pack()
    hwid.pack()
    discord.pack()
    credit.pack()
    discord.bind("<Button-1>", lambda e: callback("https://discord.gg/gWHyq7B7ss"))
    w.mainloop()


gui()

