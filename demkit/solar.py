from custom_components.hemsdelft.demkit.model.solar_info import SolarInfo
from .rest import _get_solar_info


def get_solar_info() -> SolarInfo:
    return _get_solar_info("/houses/0/solar/0")


def get_production() -> float:
    solar_info = get_solar_info()
    return min(-solar_info.consumption, 0)
