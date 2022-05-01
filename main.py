from colorama import init, Fore, Back, Style
from addons import generate
from addons import check
from addons import visual
import time


visual.main_menu()
print(Fore.GREEN + "Expl0it Miner v1.0 BETA by legendpinkyhax#1694")
print(Fore.GREEN + "Only Gen and Check are working at the moment.") 
time.sleep(1)
input = input("Check file or generate new adress [1/2]: ")

if input == "1":
    visual.main_menu()
    print("Loading file.txt...")
    with open("file.txt", "r") as infile:
        while True:
            for line in infile:
                a = line.replace("\r", "")
                b = a.replace("\n", "")
                check_results = check.check_adress(b)
                visual.print_results(b, check_results)
if input == "2":
    while True:
        adress = generate.gen_adress()
        check_results = check.check_adress(adress)
        visual.print_results(adress, check_results)

