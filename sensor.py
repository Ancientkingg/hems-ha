"""Platform for sensor integration."""

from __future__ import annotations

from sensors.meter import ExportSensor, ImportSensor

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info=None,
):
    async_add_entities([ExportSensor(), ImportSensor()])  # noqa: F821
