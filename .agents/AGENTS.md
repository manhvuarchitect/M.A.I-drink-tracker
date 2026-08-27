# M.A.I Tracker - Quy tắc phát triển (Rules)

## 1. Nguyên tắc Single Source of Truth (Nguồn Sự Thật Duy Nhất)
* **Bắt buộc** sử dụng file `custom_components/mai_tracker/strings.json` làm nguồn dữ liệu cấu hình duy nhất (Single Source of Truth) cho các tiêu đề (titles), mô tả (descriptions), nhãn phân vùng (section labels), tên gọi/thuộc tính của tất cả các **Entities (thực thể/cảm biến)** và dữ liệu dịch thuật của addon.
* Mọi thay đổi hoặc bổ sung thông tin ngôn ngữ, tiêu đề, cấu hình thực thể (Entities) bắt buộc phải sửa đổi tại `strings.json` trước.
* Sau khi chỉnh sửa `strings.json`, phải chạy script `py scratch/update_strings.py` (hoặc lệnh tương ứng) để đồng bộ tự động sang `translations/vi.json` và dịch tự động/đồng bộ sang `translations/en.json`.
* Tuyệt đối **không sửa đổi thủ công** các file dịch trong thư mục `translations/` để tránh lệch pha dữ liệu.

## 2. Quy trình kiểm tra cú pháp, Tạo phiên bản Build và Deploy lên GitHub
* **Quy tắc đặt tên phiên bản Build**:
  - Luôn sử dụng hậu tố định dạng: `_YYYYMMDD.bx` (ví dụ: `_20260827.b1`, `_20260827.b2`...).
  - `YYYYMMDD`: Năm, tháng, ngày hiện tại.
  - `bx`: Số thứ tự bản build trong ngày, tự động kiểm tra và tăng dần (`b1`, `b2`, `b3`...).
* **Quy trình bắt buộc sau mỗi lần thay đổi mã nguồn hoặc build**:
  1. Chạy trình biên dịch kiểm tra lỗi cú pháp Python:
     `py -m py_compile custom_components/mai_tracker/config_flow.py`
  2. Tạo bản build / tag / release có tên phiên bản kèm hậu tố `_YYYYMMDD.bx` tương ứng.
  3. Tiến hành commit, gắn tag phiên bản (nếu có) và đẩy (push) toàn bộ mã nguồn lên GitHub.
