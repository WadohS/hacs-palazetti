"""Support for Palazzetti power."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.sensor import SensorEntity

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN, ICON_INFO, SENSORS

from .entity import PalazzettiEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Setup sensor platform"""

    coordinator = hass.data[DOMAIN][entry.entry_id]
    for key, value in SENSORS.items():
        async_add_entities(
            [PalazzettiSensor(coordinator, entry, key, value[0], value[1])]
        )


class PalazzettiSensor(PalazzettiEntity, SensorEntity):
    """Palazetti sensor entity"""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_icon = ICON_INFO
    _extra_attr = None

    _sensor_id = None
    _data_key = None
    _extra_attributes = None

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        config_entry: ConfigEntry,
        sensor_id: str,
        data_key: str,
        extra_attributes=None,
    ):
        self._sensor_id = sensor_id
        self._data_key = data_key
        self._extra_attributes = extra_attributes
        PalazzettiEntity.__init__(self, coordinator, config_entry, sensor_id)

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return extra attributes."""
        state_attr = super().extra_state_attributes
        if self._extra_attr is not None:
            state_attr.update(self._extra_attr)
        return state_attr

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_native_value = self.coordinator.data.get(self._data_key)
        if self._extra_attributes is not None:
            for extra_attr in self._extra_attributes:
                self._extra_attr[extra_attr] = self.coordinator.data.get(extra_attr)
        self.async_write_ha_state()
