"""Sleep sensor entities for M.A.I Tracker."""

from __future__ import annotations

from typing import Any
from homeassistant.components.sensor.const import SensorDeviceClass, SensorStateClass
from homeassistant.config_entries import ConfigEntry

from ..coordinator import CaffeineCoordinator
from .base import _CaffeineBase


class SleepScoreSensor(_CaffeineBase):
    """Sleep Quality Score Sensor (0-100)."""

    _attr_icon = "mdi:sleep"
    _attr_native_unit_of_measurement = "đ"
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_suggested_display_precision = 0

    def __init__(self, coordinator: CaffeineCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator, entry, suffix="sleep_score")
        self._attr_unique_id = f"{entry.entry_id}_sleep_score"

    @property
    def native_value(self) -> float | None:
        if not self.coordinator.data or self.coordinator.data.sleep_score is None:
            return None
        return self.coordinator.data.sleep_score

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        if not self.coordinator.data:
            return {}
        return self.coordinator.data.sleep_attributes


class SleepDurationSensor(_CaffeineBase):
    """Total Sleep Duration Sensor."""

    _attr_icon = "mdi:bed-clock"
    _attr_native_unit_of_measurement = "h"
    _attr_device_class = SensorDeviceClass.DURATION
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_suggested_display_precision = 1

    def __init__(self, coordinator: CaffeineCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator, entry, suffix="sleep_duration")
        self._attr_unique_id = f"{entry.entry_id}_sleep_duration"

    @property
    def native_value(self) -> float | None:
        if not self.coordinator.data or self.coordinator.data.sleep_duration is None:
            return None
        return self.coordinator.data.sleep_duration


class DeepSleepSensor(_CaffeineBase):
    """Deep Sleep Stage Sensor."""

    _attr_icon = "mdi:power-sleep"
    _attr_native_unit_of_measurement = "h"
    _attr_device_class = SensorDeviceClass.DURATION
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_suggested_display_precision = 1

    def __init__(self, coordinator: CaffeineCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator, entry, suffix="deep_sleep")
        self._attr_unique_id = f"{entry.entry_id}_deep_sleep"

    @property
    def native_value(self) -> float | None:
        if not self.coordinator.data or self.coordinator.data.sleep_deep is None:
            return None
        return self.coordinator.data.sleep_deep


class RemSleepSensor(_CaffeineBase):
    """REM Sleep Stage Sensor."""

    _attr_icon = "mdi:brain"
    _attr_native_unit_of_measurement = "h"
    _attr_device_class = SensorDeviceClass.DURATION
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_suggested_display_precision = 1

    def __init__(self, coordinator: CaffeineCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator, entry, suffix="rem_sleep")
        self._attr_unique_id = f"{entry.entry_id}_rem_sleep"

    @property
    def native_value(self) -> float | None:
        if not self.coordinator.data or self.coordinator.data.sleep_rem is None:
            return None
        return self.coordinator.data.sleep_rem


class LightSleepSensor(_CaffeineBase):
    """Light Sleep Stage Sensor."""

    _attr_icon = "mdi:weather-night"
    _attr_native_unit_of_measurement = "h"
    _attr_device_class = SensorDeviceClass.DURATION
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_suggested_display_precision = 1

    def __init__(self, coordinator: CaffeineCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator, entry, suffix="light_sleep")
        self._attr_unique_id = f"{entry.entry_id}_light_sleep"

    @property
    def native_value(self) -> float | None:
        if not self.coordinator.data or self.coordinator.data.sleep_light is None:
            return None
        return self.coordinator.data.sleep_light


class SleepAwakeSensor(_CaffeineBase):
    """Awake Time during Sleep Sensor."""

    _attr_icon = "mdi:alarm-snooze"
    _attr_native_unit_of_measurement = "min"
    _attr_device_class = SensorDeviceClass.DURATION
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_suggested_display_precision = 0

    def __init__(self, coordinator: CaffeineCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator, entry, suffix="awake_time")
        self._attr_unique_id = f"{entry.entry_id}_awake_time"

    @property
    def native_value(self) -> float | None:
        if not self.coordinator.data or self.coordinator.data.sleep_awake is None:
            return None
        return self.coordinator.data.sleep_awake


class SleepEfficiencySensor(_CaffeineBase):
    """Sleep Efficiency Percentage Sensor (%)."""

    _attr_icon = "mdi:chart-arc"
    _attr_native_unit_of_measurement = "%"
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_suggested_display_precision = 0

    def __init__(self, coordinator: CaffeineCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator, entry, suffix="sleep_efficiency")
        self._attr_unique_id = f"{entry.entry_id}_sleep_efficiency"

    @property
    def native_value(self) -> float | None:
        if not self.coordinator.data or self.coordinator.data.sleep_efficiency is None:
            return None
        return self.coordinator.data.sleep_efficiency


class SleepStateSensor(_CaffeineBase):
    """Current Sleep State / Stage Sensor (Sleeping / Awake / Deep / REM / Light)."""

    _attr_icon = "mdi:sleep"

    def __init__(self, coordinator: CaffeineCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator, entry, suffix="sleep_state")
        self._attr_unique_id = f"{entry.entry_id}_sleep_state"

    @property
    def native_value(self) -> str | None:
        if not self.coordinator.data or not self.coordinator.data.sleep_state:
            return "awake"
        return self.coordinator.data.sleep_state


class SleepSummarySensor(_CaffeineBase):
    """Comprehensive Sleep Summary Sensor."""

    _attr_icon = "mdi:sleep"

    def __init__(self, coordinator: CaffeineCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator, entry, suffix="sleep_summary")
        self._attr_unique_id = f"{entry.entry_id}_sleep_summary"

    @property
    def native_value(self) -> str | None:
        if not self.coordinator.data:
            return "No Data"
        score = self.coordinator.data.sleep_score
        if score is not None:
            if score >= 85:
                return f"Tốt ({score}đ)"
            elif score >= 70:
                return f"Khá ({score}đ)"
            elif score >= 50:
                return f"Trung bình ({score}đ)"
            else:
                return f"Kém ({score}đ)"
        duration = self.coordinator.data.sleep_duration
        if duration is not None:
            return f"{duration}h"
        return "Chưa có dữ liệu"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        if not self.coordinator.data:
            return {}
        data = self.coordinator.data
        attrs = {
            "score": data.sleep_score,
            "duration": data.sleep_duration,
            "deep": data.sleep_deep,
            "rem": data.sleep_rem,
            "light": data.sleep_light,
            "awake": data.sleep_awake,
            "efficiency": data.sleep_efficiency,
            "state": data.sleep_state,
            "wearable_device": data.sleep_wearable_name,
        }
        attrs.update(data.sleep_attributes)
        return attrs
