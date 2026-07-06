import base64
import zlib
import os

FILES_TO_PROTECT = [
    "D:/OneDrive - MIDAR/3_MIDAR_MORE/MIDAR - VIBERCODING/HASS/M.A.I-Tracker/custom_components/mai_tracker/coordinator.py",
    "D:/OneDrive - MIDAR/3_MIDAR_MORE/MIDAR - VIBERCODING/HASS/M.A.I-Tracker/custom_components/mai_tracker/utils/caffeine_calc.py",
    "D:/OneDrive - MIDAR/3_MIDAR_MORE/MIDAR - VIBERCODING/HASS/M.A.I-Tracker/custom_components/mai_tracker/utils/alcohol_calc.py"
]

def obfuscate_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return False
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Mã hóa dùng zlib + base64 để bảo mật mã nguồn
    compressed = zlib.compress(content.encode('utf-8'))
    b64_encoded = base64.b64encode(compressed).decode('utf-8')
    
    # Tạo wrapper code sử dụng exec để giải mã tại runtime
    obfuscated_code = f"# Obfuscated Code for Protection\nimport base64, zlib\nexec(zlib.decompress(base64.b64decode({repr(b64_encoded)})).decode('utf-8'))\n"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(obfuscated_code)
        
    print(f"Obfuscated and secured: {file_path}")
    return True

if __name__ == '__main__':
    for p in FILES_TO_PROTECT:
        obfuscate_file(p)
