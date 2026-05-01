from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_secret_key_BCY, network_type)
from Q1 import send_from_P2PKH_transaction


######################################################################
first_half = 1317
second_half = 2107

Q2a_txout_scriptPubKey = [
        OP_2DUP,
        OP_ADD,
        first_half,
        OP_EQUALVERIFY,
        OP_SUB,
        second_half,
        OP_EQUAL
    ]
######################################################################

if __name__ == '__main__':
    ######################################################################
    amount_to_send = 0.00089 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        'f331290f4d616d78ca2bd1832855fcd41aecae8189c17c8f74fcbb6db1c55228')
    utxo_index = 2 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_secret_key_BCY, network_type)
    print(response.status_code, response.reason)
    print(response.text)
