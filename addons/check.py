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
        if l in lol:
            for balance in ls:
                money = balance["balance"]
                text = ""
                f = open("hits.txt", "a")
                if not money == 0:
                    if money >= 0.0001:
                        text = "  good wallet"
                    elif money >= 1:
                        text = "  great wallet"
                    elif money >= 10:
                        text = "  ledger or cold wallet"
                    elif money <= 0.0001:
                        text = "  decent wallet"
                    data = (str(address)+"   "+str(money)+"        "+str(text))
                    f.write(str(data) + "\n")
                    f.close()
                    return(f"{address} is valid. With the balance of {money} BTC")
                else:
                    return(1)
        else:
            return(0)
    except:
        return(maintance)
