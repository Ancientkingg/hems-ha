from homeassistant.components.switch import SwitchDeviceClass, SwitchEntity

from custom_components.hemsdelft.demkit.solar import set_solar_state

class PvPanelSwitch(SwitchEntity):
    _attr_name = "PV Panel"
    _attr_assumed_state = True
    _attr_device_class = SwitchDeviceClass.OUTLET

    def turn_on(self, **kwargs) -> None:
        set_solar_state(True)

    def turn_off(self, **kwargs) -> None:
        set_solar_state(False)
