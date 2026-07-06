import json

def update_strings():
    f = 'D:/OneDrive - MIDAR/3_MIDAR_MORE/MIDAR - VIBERCODING/HASS/M.A.I-Tracker/custom_components/mai_tracker/strings.json'
    d = json.load(open(f, encoding='utf-8'))
    
    # [Single Source of Truth cho Tiếng Việt trong strings.json]
    # Config Flow (Tạo mới)
    d['config']['step']['user']['title'] = 'M.A.I Tracker - Tạo hồ sơ (Bước 1/5)'
    d['config']['step']['basic_settings']['title'] = 'Thông số Nền tảng & Sinh lý (Bước 2/5)'
    d['config']['step']['environment']['title'] = 'Cấu hình Cảm biến & Đồng bộ (Bước 3/5)'
    d['config']['step']['notifications']['title'] = 'Trung tâm Thông báo & Loa (Bước 4/5)'
    d['config']['step']['medicine']['title'] = 'Lịch trình & Thuốc uống (Bước 5/5)'
    
    if 'calendars' in d['config']['step']:
        del d['config']['step']['calendars']
    if 'bio_sensors' in d['config']['step']:
        del d['config']['step']['bio_sensors']
        
    # Options Flow (Chỉnh sửa) - Bây giờ đồng nhất cấu trúc 5 bước hoàn chỉnh
    d['options']['step']['init']['title'] = 'M.A.I Tracker - Chỉnh sửa Hồ sơ (Bước 1/5)'
    d['options']['step']['basic_settings'] = {
        "title": "Thông số Nền tảng & Sinh lý (Bước 2/5)",
        "description": "Cấu hình lại các thông số cơ thể và mục tiêu Cafein/Nước của bạn.",
        "data": {
            "water_goal": "Mục tiêu nước (ml)",
            "half_life_hours": "Thời gian bán phân hủy Cafein",
            "sleep_safe_mg": "Ngưỡng Cafein an toàn để ngủ",
            "enable_absorption": "Mô phỏng hấp thụ (Gradual Absorption)",
            "absorption_time_min": "Thời gian hấp thụ (Phút)",
            "weight_kg": "Cân nặng mặc định (kg)",
            "gender": "Giới tính"
        }
    }
    d['options']['step']['environment']['title'] = 'Cấu hình Cảm biến & Đồng bộ (Bước 3/5)'
    d['options']['step']['notifications']['title'] = 'Trung tâm Thông báo & Loa (Bước 4/5)'
    d['options']['step']['medicine']['title'] = 'Lịch trình & Thuốc uống (Bước 5/5)'
    
    if 'calendars' in d['options']['step']:
        del d['options']['step']['calendars']
    if 'bio_sensors' in d['options']['step']:
        del d['options']['step']['bio_sensors']

    # Thêm mô tả các nhãn phân chia vùng để tránh bị hiện box nhập chữ
    labels_vi = {
        "environment_label": "========== [1] CẢM BIẾN MÔI TRƯỜNG (Environment) ==========",
        "bio_label": "========== [2] CẢM BIẾN SINH HỌC & ĐỒ ĐEO (Bio Wearables) ==========",
        "sync_label": "========== [3] CHU KỲ ĐỒNG BỘ ĐIỆN THOẠI (Companion Sync) ==========",
        "notify_dev_label": "========== [1] PHÂN CẤP THIẾT BỊ NHẬN THÔNG BÁO ==========",
        "tts_voice_label": "========== [2] PHÁT THANH GIỌNG NÓI & NỘI DUNG TTS ==========",
        "water_cycle_label": "========== [3] CHU KỲ NHẮC NHỞ UỐNG NƯỚC ==========",
        "templates_label": "========== [4] KHO MẪU CÂU THOẠI TÙY BIẾN (Templates) ==========",
        "calendar_label": "========== [1] TÍCH HỢP LỊCH TRÌNH & BẢN TIN AGENDAS ==========",
        "med_label": "========== [2] LỊCH NHẮC UỐNG THUỐC LEO THANG (Medicine 1 đến 10) =========="
    }
    
    # Cập nhật nhãn phân vùng vào data của config
    for step_key in ['environment', 'notifications', 'medicine']:
        if step_key in d['config']['step']:
            for k, v in labels_vi.items():
                d['config']['step'][step_key]['data'][k] = v

    # Cập nhật nhãn phân vùng vào data của options
    for step_key in ['environment', 'notifications', 'medicine']:
        if step_key in d['options']['step']:
            if 'data' not in d['options']['step'][step_key]:
                d['options']['step'][step_key]['data'] = {}
            for k, v in labels_vi.items():
                d['options']['step'][step_key]['data'][k] = v
        
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    
    # Định nghĩa bản dịch cho step init của options flow
    d['options']['step']['init']['data'] = {
        "person_name": "Tên thành viên (Prefix)",
        "linked_user": "Tài khoản liên kết (User)"
    }
    
    # Định nghĩa bản dịch cho step environment của options flow
    d['options']['step']['environment']['data'] = {
        "temp_sensor": "Cảm biến nhiệt độ",
        "humidity_sensor": "Cảm biến độ ẩm",
        "weather_entity": "Thực thể thời tiết",
        "heart_rate_sensors": "Cảm biến nhịp tim (Heart Rate)",
        "step_sensors": "Cảm biến số bước (Steps)",
        "weight_sensor": "Cảm biến cân nặng (Weight)",
        "bio_sync_interval": "Chu kỳ đồng bộ tự động"
    }

    # Định nghĩa bản dịch cho step notifications của options flow
    d['options']['step']['notifications']['data'] = {
        "notify_target": "Thiết bị nhận thông báo Cá nhân (Xưng hô 'Bạn')",
        "notify_target_management": "Thiết bị nhận thông báo Giám sát (Xưng hô '{person_name}')",
        "tts_target": "Loa phát thanh (TTS Target)",
        "tts_message": "Nội dung phát thanh nhắc uống nước",
        "water_reminder_interval": "Chu kỳ nhắc uống nước (Phút, 0 để tắt)",
        "water_reminder_tts": "Mẫu phát nhắc nước qua Loa (dùng '{hours}')",
        "water_reminder_notify": "Mẫu nhắc nước Cá nhân (dùng '{hours}')",
        "water_reminder_notify_management": "Mẫu nhắc nước Giám sát (dùng '{hours}', '{person_name}')",
        "drink_log_notify_personal": "Mẫu báo uống nước Cá nhân (dùng '{amount}', '{drink_name}')",
        "drink_log_notify_management": "Mẫu báo uống nước Giám sát (dùng '{person_name}', '{amount}', '{drink_name}')",
        "drink_log_notify_remove": "Mẫu báo hoàn tác uống nước (dùng '{person_name}')"
    }

    # Định nghĩa bản dịch cho step medicine của options flow
    d['options']['step']['medicine']['data'] = {
        "calendars": "Chọn lịch trình (Calendars)"
    }
    for i in range(1, 11):
        d['options']['step']['medicine']['data'][f"medicine_{i}_name"] = f"-------- [{i}] TÊN THUỐC --------"
        d['options']['step']['medicine']['data'][f"medicine_{i}_time"] = "Giờ uống"
        d['options']['step']['medicine']['data'][f"medicine_{i}_notify"] = "Điện thoại nhận thông báo"
        d['options']['step']['medicine']['data'][f"medicine_{i}_notify_secondary"] = f"Điện thoại nhận thông báo phụ [{i}]"
        d['options']['step']['medicine']['data'][f"medicine_{i}_tts"] = "Loa phát thanh (TTS)"

    # Vietnam translation (đồng bộ từ strings.json)
    vi_f = f.replace('strings.json', 'translations/vi.json')
    json.dump(d, open(vi_f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    
    # English translation (map từ strings.json nhưng dịch sang tiếng Anh)
    en_f = f.replace('strings.json', 'translations/en.json')
    d_en = json.load(open(en_f, encoding='utf-8'))
    
    # Config Flow (English)
    d_en['config']['step']['user']['title'] = 'Create Profile (Step 1/5)'
    d_en['config']['step']['basic_settings']['title'] = 'Basic Settings (Step 2/5)'
    d_en['config']['step']['environment']['title'] = 'Sensors & Sync (Step 3/5)'
    d_en['config']['step']['notifications']['title'] = 'Notification & TTS Hub (Step 4/5)'
    d_en['config']['step']['medicine']['title'] = 'Schedule & Medicine Hub (Step 5/5)'
    
    if 'calendars' in d_en['config']['step']:
        del d_en['config']['step']['calendars']
    if 'bio_sensors' in d_en['config']['step']:
        del d_en['config']['step']['bio_sensors']
        
    # Options Flow (English)
    d_en['options']['step']['init']['title'] = 'Edit Profile (Step 1/5)'
    d_en['options']['step']['init']['data'] = {
        "person_name": "Member Name (Prefix)",
        "linked_user": "Linked User Account"
    }

    d_en['options']['step']['basic_settings'] = {
        "title": "Basic Settings (Step 2/5)",
        "description": "Configure your basic body metrics and water/caffeine targets.",
        "data": {
            "water_goal": "Daily Water Goal (ml)",
            "half_life_hours": "Caffeine Half-life (Hours)",
            "sleep_safe_mg": "Sleep-safe threshold (mg)",
            "enable_absorption": "Model gradual absorption",
            "absorption_time_min": "Absorption time (Minutes)",
            "weight_kg": "Default weight (kg)",
            "gender": "Gender"
        }
    }
    d_en['options']['step']['environment']['title'] = 'Sensors & Sync (Step 3/5)'
    d_en['options']['step']['environment']['data'] = {
        "temp_sensor": "Temperature Sensor",
        "humidity_sensor": "Humidity Sensor",
        "weather_entity": "Weather Entity",
        "heart_rate_sensors": "Heart rate sensors",
        "step_sensors": "Step sensors",
        "weight_sensor": "Weight sensor",
        "bio_sync_interval": "Sync interval"
    }

    d_en['options']['step']['notifications']['title'] = 'Notification & TTS Hub (Step 4/5)'
    d_en['options']['step']['notifications']['data'] = {
        "notify_target": "Personal Notification Device (Addressing 'Bạn')",
        "notify_target_management": "Monitoring Notification Device (Addressing '{person_name}')",
        "tts_target": "TTS Target (Media Player)",
        "tts_message": "TTS reminder message",
        "water_reminder_interval": "Water Reminder Interval (Minutes, 0 to disable)",
        "water_reminder_tts": "TTS water reminder template (use '{hours}')",
        "water_reminder_notify": "Personal water reminder template (use '{hours}')",
        "water_reminder_notify_management": "Monitoring water reminder template (use '{hours}', '{person_name}')",
        "drink_log_notify_personal": "Personal drink logged template (use '{amount}', '{drink_name}')",
        "drink_log_notify_management": "Monitoring drink logged template (use '{person_name}', '{amount}', '{drink_name}')",
        "drink_log_notify_remove": "Undo logged notification template (use '{person_name}')"
    }

    d_en['options']['step']['medicine']['title'] = 'Schedule & Medicine Hub (Step 5/5)'
    d_en['options']['step']['medicine']['data'] = {
        "calendars": "Calendars"
    }
    for i in range(1, 11):
        d_en['options']['step']['medicine']['data'][f"medicine_{i}_name"] = f"-------- [{i}] MEDICINE NAME --------"
        d_en['options']['step']['medicine']['data'][f"medicine_{i}_time"] = "Time"
        d_en['options']['step']['medicine']['data'][f"medicine_{i}_notify"] = "Notify Device"
        d_en['options']['step']['medicine']['data'][f"medicine_{i}_notify_secondary"] = f"Secondary Notify Device [{i}]"
        d_en['options']['step']['medicine']['data'][f"medicine_{i}_tts"] = "TTS Speaker"
    
    if 'calendars' in d_en['options']['step']:
        del d_en['options']['step']['calendars']
    if 'bio_sensors' in d_en['options']['step']:
        del d_en['options']['step']['bio_sensors']

    json.dump(d_en, open(en_f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print("Successfully updated strings and translations!")

if __name__ == '__main__':
    update_strings()
