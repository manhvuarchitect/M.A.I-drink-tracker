from typing import Any
from homeassistant.components.sensor.const import SensorDeviceClass, SensorStateClass
from homeassistant.config_entries import ConfigEntry

from ..coordinator import CaffeineCoordinator
from .base import _CaffeineBase

class LastMedicineSensor(_CaffeineBase):
    _attr_icon = "mdi:pill"

    def __init__(self, coordinator: CaffeineCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator, entry, suffix="last_medicine")
        self._attr_unique_id = f"{entry.entry_id}_last_medicine"

    @property
    def native_value(self) -> str | None:
        if not self.coordinator.data or not self.coordinator.data.medicines:
            return "None"
        last = self.coordinator.data.medicines[-1]
        return last.name

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        wearables = []
        for i in range(1, 4):
            w_name = self._entry.options.get(f"wearable_{i}_name", self._entry.data.get(f"wearable_{i}_name", ""))
            w_on_body = self._entry.options.get(f"wearable_{i}_on_body", self._entry.data.get(f"wearable_{i}_on_body", ""))
            w_battery = self._entry.options.get(f"wearable_{i}_battery", self._entry.data.get(f"wearable_{i}_battery", ""))
            w_calories = self._entry.options.get(f"wearable_{i}_calories", self._entry.data.get(f"wearable_{i}_calories", ""))
            w_sleep_score = self._entry.options.get(f"wearable_{i}_sleep_score", self._entry.data.get(f"wearable_{i}_sleep_score", ""))
            w_sleep_duration = self._entry.options.get(f"wearable_{i}_sleep_duration", self._entry.data.get(f"wearable_{i}_sleep_duration", ""))
            w_sleep_deep = self._entry.options.get(f"wearable_{i}_sleep_deep", self._entry.data.get(f"wearable_{i}_sleep_deep", ""))
            w_sleep_rem = self._entry.options.get(f"wearable_{i}_sleep_rem", self._entry.data.get(f"wearable_{i}_sleep_rem", ""))
            w_sleep_light = self._entry.options.get(f"wearable_{i}_sleep_light", self._entry.data.get(f"wearable_{i}_sleep_light", ""))
            w_sleep_awake = self._entry.options.get(f"wearable_{i}_sleep_awake", self._entry.data.get(f"wearable_{i}_sleep_awake", ""))
            w_sleep_efficiency = self._entry.options.get(f"wearable_{i}_sleep_efficiency", self._entry.data.get(f"wearable_{i}_sleep_efficiency", ""))
            w_sleep_state = self._entry.options.get(f"wearable_{i}_sleep_state", self._entry.data.get(f"wearable_{i}_sleep_state", ""))
            if w_name or w_on_body:
                wearables.append({
                    "name": w_name,
                    "on_body": w_on_body,
                    "battery": w_battery,
                    "calories": w_calories,
                    "sleep_score": w_sleep_score,
                    "sleep_duration": w_sleep_duration,
                    "sleep_deep": w_sleep_deep,
                    "sleep_rem": w_sleep_rem,
                    "sleep_light": w_sleep_light,
                    "sleep_awake": w_sleep_awake,
                    "sleep_efficiency": w_sleep_efficiency,
                    "sleep_state": w_sleep_state,
                })

        attrs = {
            "calendars": self._entry.options.get("calendars", self._entry.data.get("calendars", [])),
            "wearables": wearables,
            "low_battery_threshold": self._entry.options.get("low_battery_threshold", self._entry.data.get("low_battery_threshold", 15)),
            "notify_target": self._entry.options.get("notify_target", self._entry.data.get("notify_target", []))
        }
        if self.coordinator.data and self.coordinator.data.medicines:
            last = self.coordinator.data.medicines[-1]
            attrs.update({
                "type": last.med_type,
                "timestamp": last.timestamp.isoformat(),
                "reminder_time": last.reminder_time.isoformat() if last.reminder_time else None
            })
        return attrs

class AggregatedHeartRateSensor(_CaffeineBase):
    _attr_icon = "mdi:heart-pulse"
    _attr_native_unit_of_measurement = "bpm"
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator: CaffeineCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator, entry, suffix="aggregated_heart_rate")
        self._attr_unique_id = f"{entry.entry_id}_aggregated_heart_rate"

    @property
    def native_value(self) -> float | None:
        return self.coordinator.data.aggregated_heart_rate if self.coordinator.data else None

class AggregatedStepsSensor(_CaffeineBase):
    _attr_icon = "mdi:shoe-print"
    _attr_native_unit_of_measurement = "steps"
    _attr_state_class = SensorStateClass.TOTAL_INCREASING

    def __init__(self, coordinator: CaffeineCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator, entry, suffix="aggregated_steps")
        self._attr_unique_id = f"{entry.entry_id}_aggregated_steps"

    @property
    def native_value(self) -> int | None:
        return self.coordinator.data.aggregated_steps if self.coordinator.data else None

class WeightSensor(_CaffeineBase):
    _attr_icon = "mdi:weight-kilogram"
    _attr_native_unit_of_measurement = "kg"
    _attr_device_class = SensorDeviceClass.WEIGHT
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_suggested_display_precision = 1

    def __init__(self, coordinator: CaffeineCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator, entry, suffix="weight")
        self._attr_unique_id = f"{entry.entry_id}_weight"

    @property
    def native_value(self) -> float | None:
        return self.coordinator.weight_kg

