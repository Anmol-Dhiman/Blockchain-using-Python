from os import access
from eth_utils import to_wei
from web3 import Web3


ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# accounts address in the ganache network 
acount_1 = "0x1A065E1e4568aB20FDaD3f906f470Ce888D57Fc4"
acount_2 = "0xC8c5A7c4a9D1B9Db8b279f2A597B1a2995Fe6c51"

# the private key of those networks
private_key_acount_1 = "a47da5e150c0bed5df18bc7b8c9b83d74ef8973957fd1e725e248e1f9f0548c1"
private_key_acount_2 = "e28ba18645bddbd5c73c28a4616f9e4c5cbd60a7fcba6930b1149a0f22915713"

nonce = web3.eth.getTransactionCount(acount_1)

tx = {
    'nonce': nonce,
    'to': acount_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}


signed_tx = web3.eth.account.signTransaction(tx, private_key_acount_1)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
