from bit import *
from bitcoin import *

def gen_priv_adress():
    private_key = random_key()
    privadress = privkey_to_address(private_key)
    return(private_key)

def gen_adress():
    private_key = random_key()
    public_key = privtopub(private_key)
    address = pubtoaddr(public_key)
    return address