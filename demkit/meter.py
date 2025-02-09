from const import BASE_URL  # noqa: D100
from model.measurement import Measurement
import requests
from rest import _get_measurement


def get_import() -> Measurement:
    return _get_measurement("/houses/0/meters/0/import")


def get_export() -> Measurement:
    return _get_measurement("/houses/0/meters/0/import")
