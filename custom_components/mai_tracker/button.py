"""Button platform for M.A.I Tracker."""
from __future__ import annotations

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import CaffeineCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up M.A.I Tracker button entities."""
    coordinator: CaffeineCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([PlayTTSButton(coordinator, entry)])


class PlayTTSButton(CoordinatorEntity[CaffeineCoordinator], ButtonEntity):
    """Button to trigger playing the custom TTS message on speaker."""

    _attr_has_entity_name = True
    _attr_icon = "mdi:volume-high"
    _attr_translation_key = "play_tts"

    def __init__(self, coordinator: CaffeineCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator)
        self._entry = entry
        person = coordinator.person_name.lower().replace(" ", "_")
        self.entity_id = f"button.mait_{person}_play_tts"
        self._attr_unique_id = f"{entry.entry_id}_play_tts_button"

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.entry_id)},
            name=f"M.A.I Tracker {self.coordinator.person_name}",
            manufacturer="M.A.I Tracker",
            model="Assistant Tracker",
        )

    async def async_press(self) -> None:
        await self.coordinator.async_play_custom_tts()
