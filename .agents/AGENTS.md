# M.A.I Tracker - Quy tắc phát triển (Rules)

## 1. Nguyên tắc Single Source of Truth (Nguồn Sự Thật Duy Nhất)
* **Bắt buộc** sử dụng file `custom_components/mai_tracker/strings.json` làm nguồn dữ liệu cấu hình duy nhất (Single Source of Truth) cho các tiêu đề (titles), mô tả (descriptions), nhãn phân vùng (section labels), tên gọi/thuộc tính của tất cả các **Entities (thực thể/cảm biến)** và dữ liệu dịch thuật của addon.
* Mọi thay đổi hoặc bổ sung thông tin ngôn ngữ, tiêu đề, cấu hình thực thể (Entities) bắt buộc phải sửa đổi tại `strings.json` trước.
* Sau khi chỉnh sửa `strings.json`, phải chạy script `py scratch/update_strings.py` (hoặc lệnh tương ứng) để đồng bộ tự động sang `translations/vi.json` và dịch tự động/đồng bộ sang `translations/en.json`.
* Tuyệt đối **không sửa đổi thủ công** các file dịch trong thư mục `translations/` để tránh lệch pha dữ liệu.

## 2. Quy trình kiểm tra cú pháp và Deploy
* Trước khi deploy phiên bản mới, bắt buộc phải chạy trình biên dịch kiểm tra lỗi cú pháp Python:
  `py -m py_compile custom_components/mai_tracker/config_flow.py`
* Sau khi xác nhận không có lỗi cú pháp, chạy `py secure_deploy.py` để đóng gói mã nguồn đã mã hóa lên GitHub.
