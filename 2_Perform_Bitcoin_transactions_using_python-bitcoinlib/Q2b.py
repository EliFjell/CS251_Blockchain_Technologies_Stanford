from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from Q1 import P2PKH_scriptPubKey
from Q2a import Q2a_txout_scriptPubKey

from lib.config import my_address_BCY

network_type = 'bcy-test'
######################################################################
amount_to_send = 0.00087 # amount of BTC in the output you're sending minus fee
txid_to_spend = (
        'c7018d0cb41bbb6a983727d34c0530960ae2b95d88413e25985df0d4f1f8e6c7')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################

txin_scriptPubKey = Q2a_txout_scriptPubKey
######################################################################
txin_scriptSig = [
        1712,
        -395
]
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(my_address_BCY)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)
