from web3 import Web3

def get_eth_balance(w3: Web3, address: str) -> float:
    try:
        balance = w3.eth.get_balance(address)
        return float(w3.fromWei(balance, 'ether'))
    except:
        return 0.0
