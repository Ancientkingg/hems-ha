"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import UnitOfEnergy
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType

import requests


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info=None
):
    async_add_entities([ExportSensor(), ImportSensor()])


def get_import() -> float:
    resp = requests.get("http://host.docker.internal:8080/houses/0/meters/0/import", timeout=5)
    return float(resp.json()["value"])

def get_export() -> float:
    resp = requests.get("http://host.docker.internal:8080/houses/0/meters/0/export", timeout=5)
    return float(resp.json()["value"])


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

