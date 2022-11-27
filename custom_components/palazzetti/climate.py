"""Support for Palazzetti thermostats."""
from __future__ import annotations

import logging
from typing import Any, Literal


from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import (
    FAN_AUTO,
    FAN_HIGH,
    ClimateEntityFeature,
    HVACAction,
    HVACMode,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE, TEMP_CELSIUS
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import (
    DOMAIN,
    FAN_1,
    FAN_2,
    FAN_3,
    FAN_4,
    FAN_5,
    FAN_HA_TO_PALAZZETTI,
    FAN_PALAZZETTI_TO_HA,
)

from .entity import PalazzettiEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Setup climate platform"""

    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([PalazzettiClimate(coordinator, entry)])


class PalazzettiClimate(PalazzettiEntity, ClimateEntity):
    """Palazetti stove Climate entity"""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_temperature_unit = TEMP_CELSIUS
    _attr_target_temperature_step = 1
    _attr_hvac_modes = [HVACMode.OFF, HVACMode.HEAT]
    _attr_supported_features = (
        ClimateEntityFeature.TARGET_TEMPERATURE | ClimateEntityFeature.FAN_MODE
    )

    _attr_hvac_mode = None
    _attr_fan_mode = None
    _attr_hvac_action = None

    _state = None

    def __init__(self, coordinator: DataUpdateCoordinator, config_entry: ConfigEntry):
        PalazzettiEntity.__init__(self, coordinator, config_entry)
        self._attr_min_temp = self.coordinator.data.get("SPLMIN")
        self._attr_max_temp = self.coordinator.data.get("SPLMAX")

        fan_modes: list[Literal] = [FAN_1, FAN_2, FAN_3, FAN_4, FAN_5]
        if self.coordinator.data.get("FAN2MODE") in [2, 3]:
            fan_modes.append(FAN_AUTO)
        if self.coordinator.data.get("FAN2MODE") == 3:
            fan_modes.append(FAN_HIGH)

        self._attr_fan_modes = fan_modes

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return extra attributes."""
        state_attr = super().extra_state_attributes
        state_attr["STATE"] = self._state
        return state_attr

    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None:
        """Set new target hvac mode."""
        if hvac_mode == HVACMode.OFF:
            await self.hass.async_add_executor_job(
                self.coordinator.hub.product.power_off
            )
        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self.coordinator.hub.product.power_on
            )
        await self.coordinator.async_request_refresh()

    async def async_set_fan_mode(self, fan_mode: str) -> None:
        """Set new target fan mode."""
        if fan_mode == FAN_HIGH:
            await self.coordinator.hub.product.async_set_fan_high_mode(1)
        elif fan_mode == FAN_AUTO:
            await self.coordinator.hub.product.async_set_fan_auto_mode(1)
        else:
            await self.coordinator.hub.product.async_set_fan(
                1, FAN_HA_TO_PALAZZETTI[fan_mode]
            )
        await self.coordinator.async_request_refresh()

    async def async_set_temperature(self, **kwargs: Any) -> None:
        """Set new target temperature."""
        temperature = kwargs.get(ATTR_TEMPERATURE)
        await self.coordinator.hub.product.async_set_setpoint(int(temperature))
        await self.coordinator.async_request_refresh()

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_current_temperature = self.coordinator.data.get("T1")
        self._attr_target_temperature = self.coordinator.data.get("SETP")
        self._attr_fan_mode = FAN_PALAZZETTI_TO_HA[self.coordinator.data.get("F2L")]

        if (
            self.coordinator.data.get("STATUS") > 0
            and self.coordinator.data.get("STATUS") != 10
        ):
            self._attr_hvac_mode = HVACMode.HEAT
            if (
                self.coordinator.data.get("STATUS") == 9
                or self.coordinator.data.get("STATUS") > 11
            ):
                self._attr_hvac_action = HVACAction.IDLE
            self._attr_hvac_action = HVACAction.HEATING
        else:
            self._attr_hvac_mode = HVACMode.OFF
            self._attr_hvac_action = HVACAction.OFF

        self._state = self.coordinator.data.get("STATE")

        self.async_write_ha_state()
