"""Config flow for Palazzetti integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_HOST
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError

from palazzetti_sdk_local_api import Hub

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST): str,
    }
)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Palazzetti."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}
        
        if user_input is not None:
            try:
                hub = Hub(user_input[CONF_HOST])
                await hub.async_update(discovery=True, deep=True)
                
                if not hub.hub_online or not hub.product_online:
                    raise CannotConnect
                    
                await self.async_set_unique_id(hub.product.system)
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=hub.product.name, data=user_input
                )
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
        else:
            # Show help message pointing to WadohS repository
            self.context["show_advanced_options"] = False

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
            description_placeholders={
                "docs_url": "https://github.com/WadohS/hacs-palazetti"
            },
        )


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""
