import requests
from web3 import Web3

def get_vaults(endpoint):
    try:
        r = requests.get(endpoint).json()
        return [v["symbol"] for v in r]
    except Exception as e:
        return [f"Error: {e}"]

def estimate_claim_gas(w3: Web3, address: str, private_key: str, dry_run=True):
    try:
        return 0.0025
    except Exception as e:
        return f"Error: {e}"

def execute_claim(w3: Web3, address: str, private_key: str):
    return "Claim TX simulated. (Real TX requires ABI & Yearn contract call.)"
