import streamlit as st
from web3 import Web3
from bots import yearn_claim, odysee, captcha, surveys, blockchain

st.set_page_config(page_title="Karmic Bot Farm", layout="wide")

# Load secrets
wallets = st.secrets["wallets"]
infura = st.secrets["infura"]
yearn = st.secrets["yearn"]
odysee_cfg = st.secrets["odysee"]
captcha_cfg = st.secrets["captcha"]
surveys_cfg = st.secrets["surveys"]
settings = st.secrets["settings"]

dry_run = settings.get("dry_run_mode", True)
enable_auto_claim = settings.get("enable_auto_claim", False)

# Web3 provider
w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{infura['project_id']}"))

st.title("🧿 Karmic Bot Farm Dashboard")

# Wallet balances
st.header("💰 Wallet Balances")
eth_balance = blockchain.get_eth_balance(w3, wallets["eth_address"])
st.metric("Ethereum", f"{eth_balance:.4f} ETH")

# Yearn
st.header("🌾 Yearn Vault Earnings")
vaults = yearn_claim.get_vaults(yearn["endpoint"])
st.write(vaults)

if st.button("Estimate Yearn Claim"):
    gas = yearn_claim.estimate_claim_gas(w3, wallets["eth_address"], wallets["private_key"], dry_run=True)
    st.success(f"Estimated gas: {gas} ETH")

if st.button("Execute Yearn Claim"):
    if dry_run or not enable_auto_claim:
        st.warning("Dry-run mode ON. Enable auto-claim in secrets to run.")
    else:
        tx_hash = yearn_claim.execute_claim(w3, wallets["eth_address"], wallets["private_key"])
        st.success(f"Claim TX sent: {tx_hash}")

# Odysee
st.header("📺 Odysee Rewards")
lbc_balance = odysee.get_balance(odysee_cfg["username"], odysee_cfg["password"])
st.metric("Odysee LBC", lbc_balance)

if st.button("Auto-Claim Odysee"):
    if enable_auto_claim:
        result = odysee.claim_rewards(odysee_cfg["username"], odysee_cfg["password"])
        st.success(result)
    else:
        st.warning("Dry-run only. Enable auto-claim to run.")

# Captcha
st.header("🔑 Captcha Earnings")
two_captcha = captcha.get_balance_2captcha(captcha_cfg["twocaptcha_api_key"])
anti_captcha = captcha.get_balance_anticaptcha(captcha_cfg["anticaptcha_api_key"])

col1, col2 = st.columns(2)
col1.metric("2Captcha", f"${two_captcha:.2f}")
col2.metric("AntiCaptcha", f"${anti_captcha:.2f}")

# Surveys
st.header("📊 Surveys")
survey_status = surveys.get_status(surveys_cfg)
st.write(survey_status)

if st.button("Auto-Run Survey Bot"):
    if enable_auto_claim:
        result = surveys.run(surveys_cfg)
        st.success(result)
    else:
        st.warning("Dry-run only. Enable auto-claim to run.")

st.info("All modules respect dry-run mode unless explicitly enabled in secrets.toml.")
