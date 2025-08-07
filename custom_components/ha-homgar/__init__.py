"""A minimal custom integration for Home Assistant."""

# Import necessary libraries from Home Assistant and Python
import logging
import voluptuous as vol

from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.typing import ConfigType
from homeassistant.const import ATTR_NAME

# The domain of the integration. This must match the folder name.
DOMAIN = "hahomgar"

# Get the logger for this component, which will show up in the Home Assistant logs.
_LOGGER = logging.getLogger(__name__)

# This is a sample schema for a service. It's not strictly necessary for this
# minimal example, but it's good practice for validating service call data.
SERVICE_HELLO_SCHEMA = vol.Schema({
    vol.Optional(ATTR_NAME, default="World"): str,
})


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the 'ha-homgar' component."""
    _LOGGER.info("The 'ha-homgar' component is being set up.")

    async def handle_hello_world(call: ServiceCall):
        """Handle the service call for 'hello_world'."""
        # Get the 'name' from the service call data, defaulting to 'World'.
        name = call.data.get(ATTR_NAME)

        # Log a warning message that will be visible in the Home Assistant logs.
        _LOGGER.warning(f"Hello, {name}! This message came from your custom integration.")

    # Register our service with Home Assistant.
    # The full service name will be 'my_first_integration.hello_world'.
    hass.services.async_register(
        DOMAIN,
        "hello_world",
        handle_hello_world,
        schema=SERVICE_HELLO_SCHEMA,
    )

    # Return True to signal that the setup was successful.
    return True
