# Changelog - M.A.I Tracker

Tất cả các thay đổi, tính năng mới và bản sửa lỗi của integration **M.A.I Tracker** được ghi nhận chi tiết tại đây theo định dạng phiên bản `YYYY.MM.DD.bx`.

---

## [2026.08.27.b2] - 2026-08-27

### 🐛 Sửa lỗi tương thích & Tối ưu (Bug Fixes & Improvements)
- **Sửa lỗi không load được integration ("Not loaded")**: Khắc phục lỗi tương thích import `UTC` từ thư viện `datetime` trên môi trường Home Assistant Core/Python, chuyển sang chuẩn `timezone.utc`.
- **Chuẩn hóa toàn bộ mã nguồn sạch**: Làm sạch mã nguồn `utils/caffeine_calc.py` và `utils/alcohol_calc.py`, loại bỏ hoàn toàn các đoạn code nén `exec` để tăng tốc độ load và độ ổn định.

---

## [2026.08.27.b1] - 2026-08-27

### ✨ Tính năng mới (Features)
- **Bổ sung các Entity chỉ số giấc ngủ (Sleep Index Entities)**:
  - Tích hợp 8 chỉ số giấc ngủ trực tiếp vào **Bước 3/5: Cấu hình Cảm biến & Đồng bộ** (`environment`) cho từng thiết bị đeo thông minh (`Wearable 1`, `Wearable 2`, `Wearable 3`):
    - `wearable_{i}_sleep_score`: Cảm biến điểm số giấc ngủ (Sleep Score)
    - `wearable_{i}_sleep_duration`: Cảm biến thời lượng ngủ (Sleep Duration)
    - `wearable_{i}_sleep_deep`: Cảm biến thời gian ngủ sâu (Deep Sleep)
    - `wearable_{i}_sleep_rem`: Cảm biến thời gian ngủ REM (REM Sleep)
    - `wearable_{i}_sleep_light`: Cảm biến thời gian ngủ nông (Light Sleep)
    - `wearable_{i}_sleep_awake`: Cảm biến thời gian thức trong đêm (Awake Time)
    - `wearable_{i}_sleep_efficiency`: Cảm biến hiệu suất giấc ngủ (Sleep Efficiency %)
    - `wearable_{i}_sleep_state`: Cảm biến trạng thái giấc ngủ (Sleep State / Stage)
- **Tự động khởi tạo hệ thống cảm biến giấc ngủ trong Home Assistant**:
  - `sensor.mait_{person}_sleep_score`: Điểm số chất lượng giấc ngủ (icon `mdi:sleep`).
  - `sensor.mait_{person}_sleep_duration`: Tổng thời lượng ngủ (icon `mdi:bed-clock`).
  - `sensor.mait_{person}_deep_sleep`: Thời gian ngủ sâu (icon `mdi:power-sleep`).
  - `sensor.mait_{person}_rem_sleep`: Thời gian ngủ REM (icon `mdi:brain`).
  - `sensor.mait_{person}_light_sleep`: Thời gian ngủ nông (icon `mdi:weather-night`).
  - `sensor.mait_{person}_awake_time`: Thời gian thức trong đêm (icon `mdi:alarm-snooze`).
  - `sensor.mait_{person}_sleep_efficiency`: Hiệu suất giấc ngủ (đơn vị `%`, icon `mdi:chart-arc`).
  - `sensor.mait_{person}_sleep_state`: Trạng thái giấc ngủ thời gian thực.
  - `sensor.mait_{person}_sleep_summary`: Tổng quan đánh giá giấc ngủ kèm thuộc tính chi tiết (`extra_state_attributes`).
- **Tổng hợp thông minh từ thiết bị đeo (`coordinator.py`)**:
  - Tự động ưu tiên đọc dữ liệu giấc ngủ từ thiết bị đang đeo trên tay (`on_body == on`).
  - Tự động đưa các cảm biến giấc ngủ vào chu kỳ đánh thức/cập nhật dữ liệu từ ứng dụng di động (`update_entity`).
- **Bổ sung thuộc tính giấc ngủ vào `LastMedicineSensor`**:
  - Expose toàn bộ cấu hình và trạng thái cảm biến giấc ngủ vào danh sách `wearables` attribute.

### 🔧 Chuẩn hóa quy trình (Chores & Rules)
- Chuyển đổi định dạng phiên bản build sang quy chuẩn: `YYYY.MM.DD.bx`.
- Cập nhật quy tắc bắt buộc cập nhật Changelog, Version Manifest và đẩy GitHub tự động.

---

## [2.2.27] - 2026-07-14
- Hỗ trợ đồng bộ động nhiều thiết bị đeo (multi-device force sync).
- Tối ưu chu kỳ đồng bộ Companion App.

---

## [2.2.26] - 2026-07-13
- Hỗ trợ cấu hình tối đa 3 thiết bị đeo thông minh (Wearable 1, 2, 3) với cảm biến on-body, pin, và calo.
- Đồng bộ hóa bản dịch và phân vùng hiển thị trong Options Flow.

---

## [2.2.0] - 2026-07-06
- Tái cấu trúc toàn bộ quy trình thiết lập thành chuẩn 5 bước rõ ràng.
- Áp dụng nguyên tắc Single Source of Truth cho toàn bộ ngôn ngữ và thực thể tại `strings.json`.
