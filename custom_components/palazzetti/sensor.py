"""Support for Palazzetti power."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.sensor import SensorEntity

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import (
    DOMAIN,
    ICON_INFO,
    SENSOR_UNIT,
    SENSORS,
    SENSOR_KEY,
    SENSOR_ATTRS,
    SENSOR_CATEGORY,
)

from .entity import PalazzettiEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Setup sensor platform"""

    coordinator = hass.data[DOMAIN][entry.entry_id]
    for sensor_id, sensor_def in SENSORS.items():
        async_add_entities(
            [PalazzettiSensor(coordinator, entry, sensor_id, sensor_def)]
        )


class PalazzettiSensor(PalazzettiEntity, SensorEntity):
    """Palazetti sensor entity"""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_icon = ICON_INFO
    _extra_attr = None

    _sensor_id = None
    _data_key = None
    _extra_attributes: dict = None

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        config_entry: ConfigEntry,
        sensor_id: str,
        sensor_definition: dict,
    ):
        self._attr_name = sensor_id
        self._sensor_id = sensor_id
        self._data_key = sensor_definition[SENSOR_KEY]
        if SENSOR_ATTRS in sensor_definition.keys():
            self._extra_attributes = sensor_definition[SENSOR_ATTRS]
        if SENSOR_CATEGORY in sensor_definition.keys():
            self._attr_entity_category = sensor_definition[SENSOR_CATEGORY]
        if SENSOR_UNIT in sensor_definition.keys():
            self._attr_native_unit_of_measurement = sensor_definition[SENSOR_UNIT]

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
            self._extra_attr = {}
            for extra_attr_id, extra_attr_key in self._extra_attributes.items():
                self._extra_attr[extra_attr_id] = self.coordinator.data.get(
                    extra_attr_key
                )
        self.async_write_ha_state()
