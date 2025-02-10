from custom_components.hemsdelft.demkit.model.battery_info import BatteryInfo
from .rest import _get_battery_info

def get_battery_info() -> BatteryInfo:
    return _get_battery_info("/houses/0/battery/0")

def get_energy_in() -> float:
    battery_info = get_battery_info()
    return min(battery_info.consumption, 0)

def get_energy_out() -> float:
    battery_info = get_battery_info()
    return min(-battery_info.consumption, 0)
