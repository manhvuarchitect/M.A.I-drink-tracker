# Quy tắc phát triển dự án M.A.I Tracker (Workspace Rules)

## 1. Quy tắc quản lý phiên bản Build và Deploy lên GitHub
- **Hậu tố phiên bản (Suffix format)**: `_YYYYMMDD.bx`
  - `YYYYMMDD`: Năm, tháng, ngày hiện tại (ví dụ: `20260827`).
  - `bx`: Số thứ tự bản build / thay đổi trong ngày, tự động tăng dần (`b1`, `b2`, `b3`...).
- **Quy trình thực hiện bắt buộc**:
  - Sau mỗi lần thay đổi mã nguồn hoặc thực hiện build, luôn tạo bản build có tên phiên bản mới kèm hậu tố `_YYYYMMDD.bx`.
  - Tự động kiểm tra các bản build / tag đã có trong cùng ngày để xác định chỉ số `bx` tiếp theo chính xác.
  - Tiến hành commit và đẩy (push) toàn bộ mã nguồn / tag lên GitHub repository.

## 2. Nguyên tắc Single Source of Truth cho Ngôn ngữ & Entity
- Sử dụng file `custom_components/mai_tracker/strings.json` làm nguồn dữ liệu cấu hình duy nhất cho titles, descriptions, labels và entity names.
- Sau khi chỉnh sửa `strings.json`, đồng bộ tự động sang `translations/vi.json` và `translations/en.json`.
- Kiểm tra cú pháp Python (`py -m py_compile ...`) trước khi hoàn tất.
