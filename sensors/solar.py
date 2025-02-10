from custom_components.hemsdelft.demkit.solar import get_production

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import UnitOfEnergy


class SolarEnergyProductionSensor(SensorEntity):
    _attr_name = "Solar Energy Production"
    _attr_native_unit_of_measurement = UnitOfEnergy.WATT_HOUR
    _attr_device_class = SensorDeviceClass.ENERGY
    _attr_state_class = SensorStateClass.TOTAL

    def update(self) -> None:
        measurement = get_production()
        self._attr_native_value = -measurement
