import requests

def get_balance_2captcha(api_key):
    try:
        r = requests.get(f"http://2captcha.com/res.php?key={api_key}&action=getbalance&json=1").json()
        return float(r.get("balance", 0))
    except:
        return 0.0

def get_balance_anticaptcha(api_key):
    try:
        r = requests.post("https://api.anti-captcha.com/getBalance", json={"clientKey": api_key}).json()
        return float(r.get("balance", 0))
    except:
        return 0.0
