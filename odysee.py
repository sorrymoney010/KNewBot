import requests

API_URL = "https://api.odysee.com"

def get_balance(username, password):
    try:
        login = requests.post(f"{API_URL}/user/signin", json={"username": username, "password": password}).json()
        if not login.get("success"):
            return 0
        token = login["data"]["auth_token"]
        balance = requests.post(f"{API_URL}/wallet/balance", headers={"Authorization": token}).json()
        return float(balance["data"].get("available", 0))
    except Exception as e:
        return f"Error: {e}"

def claim_rewards(username, password):
    try:
        login = requests.post(f"{API_URL}/user/signin", json={"username": username, "password": password}).json()
        if not login.get("success"):
            return "Login failed"
        token = login["data"]["auth_token"]
        resp = requests.post(f"{API_URL}/reward/claim", headers={"Authorization": token}).json()
        return resp
    except Exception as e:
        return f"Error: {e}"
