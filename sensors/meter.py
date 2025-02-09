from demkit.meter import get_export, get_import

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import UnitOfEnergy


class ImportSensor(SensorEntity):
    _attr_name = "Import power"
    _attr_native_unit_of_measurement = UnitOfEnergy.WATT_HOUR
    _attr_device_class = SensorDeviceClass.ENERGY
    _attr_state_class = SensorStateClass.TOTAL

    def update(self) -> None:
        self._attr_native_value = get_import()


class ExportSensor(SensorEntity):
    _attr_name = "Export power"
    _attr_native_unit_of_measurement = UnitOfEnergy.WATT_HOUR
    _attr_device_class = SensorDeviceClass.ENERGY
    _attr_state_class = SensorStateClass.TOTAL

    def update(self) -> None:
        self._attr_native_value = get_export()
