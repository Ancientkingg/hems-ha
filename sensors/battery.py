from custom_components.hemsdelft.demkit.battery import get_energy_in, get_energy_out

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import UnitOfEnergy


class BatteryEnergyInSensor(SensorEntity):
    _attr_name = "Battery Energy In"
    _attr_native_unit_of_measurement = UnitOfEnergy.WATT_HOUR
    _attr_device_class = SensorDeviceClass.ENERGY
    _attr_state_class = SensorStateClass.TOTAL

    def update(self) -> None:
        measurement = get_energy_in()
        self._attr_native_value = measurement.value


class BatteryEnergyOutSensor(SensorEntity):
    _attr_name = "Battery Energy Out"
    _attr_native_unit_of_measurement = UnitOfEnergy.WATT_HOUR
    _attr_device_class = SensorDeviceClass.ENERGY
    _attr_state_class = SensorStateClass.TOTAL

    def update(self) -> None:
        measurement = get_energy_out()
        self._attr_native_value = measurement.value
