"""Support for Palazzetti power."""
from __future__ import annotations

import logging

from homeassistant.components.sensor import SensorEntity

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN, ICON_INFO

from .entity import PalazzettiEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Setup number platform"""

    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([PalazzettiStatus(coordinator, entry)])


class PalazzettiStatus(PalazzettiEntity, SensorEntity):
    """Palazetti stove power entity"""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_icon = ICON_INFO

    def __init__(self, coordinator: DataUpdateCoordinator, config_entry: ConfigEntry):
        PalazzettiEntity.__init__(self, coordinator, config_entry)

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_native_value = self.coordinator.data.get("STATE")

        self.async_write_ha_state()
