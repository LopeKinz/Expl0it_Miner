from colorama import init, Fore, Back, Style

def print_results(address, results):
    if results == 0:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} {address} : {Fore.RED}Not found{Style.RESET_ALL}")
    else:
        if results == "maintance":
            print(f"{Fore.RED}[!]{Style.RESET_ALL} API is under maintenance.")
            input("Press Enter to continue...")
        else:
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} {address} | {results}")

        


def main_menu():
    menu = f"""
  _____  _____ _    __ ___ _____   __  __ _              
 | __\ \/ / _ \ |  /  \_ _|_   _| |  \/  (_)_ _  ___ _ _ 
 | _| >  <|  _/ |_| () | |  | |   | |\/| | | ' \/ -_) '_|
 |___/_/\_\_| |____\__/___| |_|   |_|  |_|_|_||_\___|_|  
                by legendpinkyhax#1694
    """
    print(menu)