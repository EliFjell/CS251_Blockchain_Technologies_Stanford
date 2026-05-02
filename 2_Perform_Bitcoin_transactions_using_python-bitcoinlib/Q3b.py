from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_address_BCY,
                        bank_secret_key_BCY,
                        cust1_secret_key_BCY, cust2_secret_key_BCY, cust3_secret_key_BCY)
from Q1 import P2PKH_scriptPubKey
from Q3a import Q3a_txout_scriptPubKey

network_type = 'bcy-test'

def multisig_scriptSig(txin, txout, txin_scriptPubKey):
    bank_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             bank_secret_key_BCY)
    cust1_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust1_secret_key_BCY)
    cust2_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust2_secret_key_BCY)
    cust3_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust3_secret_key_BCY)
    ######################################################################
    return [
        OP_0,
        cust2_sig,
        bank_sig
    ]
    ######################################################################


def send_from_multisig_transaction(amount_to_send, txid_to_spend, utxo_index,
                                   txin_scriptPubKey, txout_scriptPubKey, network):
    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = multisig_scriptSig(txin, txout, txin_scriptPubKey)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)

if __name__ == '__main__':
    ######################################################################
    amount_to_send = 0.00085 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '64fc797b3c81407883a35ae4773c28fde869ce4b635d1ba3e105a477178b56d3')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    txin_scriptPubKey = Q3a_txout_scriptPubKey
    txout_scriptPubKey = P2PKH_scriptPubKey(my_address_BCY)

    response = send_from_multisig_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txin_scriptPubKey, txout_scriptPubKey, network_type)
    print(response.status_code, response.reason)
    print(response.text)
