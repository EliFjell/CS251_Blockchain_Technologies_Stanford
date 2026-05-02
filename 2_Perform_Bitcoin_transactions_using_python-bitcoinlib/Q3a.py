from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_secret_key_BCY,
                        bank_public_key_BCY,
                        cust1_public_key_BCY, cust2_public_key_BCY, cust3_public_key_BCY)
from Q1 import send_from_P2PKH_transaction

network_type = 'bcy-test'

######################################################################

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
    bank_public_key_BCY,
    OP_CHECKSIGVERIFY,
    OP_1,
    cust1_public_key_BCY,
    cust2_public_key_BCY,
    cust3_public_key_BCY,
    OP_3,
    OP_CHECKMULTISIG
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    amount_to_send = 0.00087 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        'f331290f4d616d78ca2bd1832855fcd41aecae8189c17c8f74fcbb6db1c55228')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_secret_key_BCY, network_type)
    print(response.status_code, response.reason)
    print(response.text)
