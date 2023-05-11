import requests
import json

s = requests.Session()

l = "balance"
maintance = "BitcoinChain.com is under maintenance."
hit = 0
def check_adress(address):
    try:
        wallet = s.get(f"https://api-r.bitcoinchain.com/v1/address/{address}", stream = True)
        lol = wallet.text
        ls = json.loads(lol)
        if l not in lol:
            return(0)
        with open("hits.txt", "a") as f:
            f.write(lol + "\n")
        for balance in ls:
            money = balance["balance"]
            return (
                f"{address} is valid. With the balance of {money} BTC"
                if money > 0
                else 1
            )
    except:
        return(maintance)

