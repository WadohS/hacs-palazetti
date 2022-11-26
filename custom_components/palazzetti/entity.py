"""PalazzettiEntity class"""

from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN, NAME, VERSION, ATTRIBUTION


class PalazzettiEntity(CoordinatorEntity):
    """PalazzettiEntity class"""

    _sensor_id = None

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        config_entry: ConfigEntry,
        sensor_id: str = None,
    ):
        super().__init__(coordinator)
        self.config_entry = config_entry
        self._sensor_id = sensor_id

    @property
    def entity_id(self):
        """Return the entity id"""
        if self._sensor_id is not None:
            return super().entity_id + "_" + self._sensor_id
        return super().entity_id

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        if self._sensor_id is not None:
            return self.config_entry.entry_id + "_" + self._sensor_id
        return self.config_entry.entry_id

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.config_entry.entry_id)},
            "name": NAME,
            "model": VERSION,
            "manufacturer": NAME,
        }

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return {
            "attribution": ATTRIBUTION,
            "id": str(self.coordinator.data.get("SN")),
            "integration": DOMAIN,
        }
