def get_status(cfg):
    return {
        "MTurk": "Connected" if cfg.get("mturk_access_key") else "Not configured",
        "Prolific": "Connected" if cfg.get("prolific_token") else "Not configured",
        "Pollfish": "Connected" if cfg.get("pollfish_token") else "Not configured",
    }

def run(cfg):
    return "Survey automation not yet implemented. Placeholder ready."
