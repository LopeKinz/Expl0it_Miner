import requests

s = requests.Session()

l = "balance"
maintance = "BitcoinChain.com is under maintenance."

def check_adress(address):
    try:
        wallet = s.get(f"https://api-r.bitcoinchain.com/v1/address/{address}", stream = True)
        response = wallet.text
        if l in response:
            return(response)
        else:
            return(0)
    except:
        return("maintance")
    
