from custom_components.hemsdelft.demkit.meter import get_export, get_import

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import UnitOfPower

class ImportSensor(SensorEntity):
    _attr_name = "Import power"
    _attr_native_unit_of_measurement = UnitOfPower.WATT
    _attr_device_class = SensorDeviceClass.POWER
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        measurement = get_import()
        self._attr_native_value = measurement.value


class ExportSensor(SensorEntity):
    _attr_name = "Export power"
    _attr_native_unit_of_measurement = UnitOfPower.WATT
    _attr_device_class = SensorDeviceClass.POWER
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        measurement = get_export()
        self._attr_native_value = measurement.value
