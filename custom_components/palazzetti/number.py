"""Support for Palazzetti power."""
from __future__ import annotations

import logging

from homeassistant.components.number import NumberEntity, NumberMode

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN

from .entity import PalazzettiEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Setup number platform"""

    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([PalazzettiPower(coordinator, entry)])


class PalazzettiPower(PalazzettiEntity, NumberEntity):
    """Palazetti stove power entity"""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_mode = NumberMode.SLIDER
    _attr_native_min_value = 1
    _attr_native_max_value = 5
    _attr_native_step = 1

    def __init__(self, coordinator: DataUpdateCoordinator, config_entry: ConfigEntry):
        PalazzettiEntity.__init__(self, coordinator, config_entry)

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        await self.coordinator.hub.product.async_set_power(int(value))
        await self.coordinator.async_request_refresh()

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_native_value = self.coordinator.data.get("PWR")

        self.async_write_ha_state()
