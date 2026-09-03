"""Text platform for M.A.I Tracker."""
from __future__ import annotations

from homeassistant.components.text import TextEntity, TextMode
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
    """Set up M.A.I Tracker text entities."""
    coordinator: CaffeineCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([CustomTTSMessageText(coordinator, entry)])


class CustomTTSMessageText(CoordinatorEntity[CaffeineCoordinator], TextEntity):
    """Text entity to input custom TTS message."""

    _attr_has_entity_name = True
    _attr_icon = "mdi:message-text-outline"
    _attr_translation_key = "custom_tts_message"
    _attr_mode = TextMode.TEXT

    def __init__(self, coordinator: CaffeineCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator)
        self._entry = entry
        person = coordinator.person_name.lower().replace(" ", "_")
        self.entity_id = f"text.mait_{person}_tts_message"
        self._attr_unique_id = f"{entry.entry_id}_tts_message_text"

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.entry_id)},
            name=f"M.A.I Tracker {self.coordinator.person_name}",
            manufacturer="M.A.I Tracker",
            model="Assistant Tracker",
        )

    @property
    def native_value(self) -> str | None:
        return self.coordinator.custom_tts_message or ""

    async def async_set_value(self, value: str) -> None:
        await self.coordinator.async_set_custom_tts_message(value)
