import requests

def get_import() -> float:
    resp = requests.get(
        "http://host.docker.internal:8080/houses/0/meters/0/import", timeout=5
    )
    return float(resp.json()["value"])


def get_export() -> float:
    resp = requests.get(
        "http://host.docker.internal:8080/houses/0/meters/0/export", timeout=5
    )
    return float(resp.json()["value"])
