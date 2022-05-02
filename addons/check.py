import requests
import json

s = requests.Session()

l = "balance"
maintance = "BitcoinChain.com is under maintenance."
hit = 0
def check_adress(address):
        wallet = s.get(f"https://api-r.bitcoinchain.com/v1/address/{address}", stream = True)
        lol = wallet.text
        ls = json.loads(lol)
        if l in lol:
            f = open("hits.txt", "a")
            f.write(lol + "\n")
            f.close()
            for balance in ls:
                money = balance["balance"]
            return(f"{address} is valid. With the balance of {money}")
        else:
            return(0)

