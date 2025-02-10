from .model.const import BASE_URL
from .model.measurement import Measurement
from .model.rest_error import RestError
import requests


def _get_measurement(path: str) -> Measurement:
    resp = requests.get(
        BASE_URL + path, timeout=5
    )
    data = resp.json()

    # check if data has a unit key
    if "unit" not in data or "value" not in data:
        raise RestError("Invalid data format")

    return Measurement(value=float(data["value"]), unit=data["unit"])
