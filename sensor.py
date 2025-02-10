"""Platform for sensor integration."""

from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType

from custom_components.hemsdelft.sensors.meter import ExportSensor, ImportSensor
from custom_components.hemsdelft.sensors.battery import BatteryEnergyInSensor, BatteryEnergyOutSensor
from custom_components.hemsdelft.sensors.solar import SolarEnergyProductionSensor


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info=None,
):
    async_add_entities([ExportSensor(), ImportSensor(), BatteryEnergyInSensor(), BatteryEnergyOutSensor(), SolarEnergyProductionSensor()])  # noqa: F821
