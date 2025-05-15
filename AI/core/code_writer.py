import os
from core.AI import ask_gpt

def write_code_from_command(command, save_path="Test/div.py"):
    """
    Tạo mã Python dựa trên lệnh người dùng và lưu vào file.
    """
    if not os.path.exists("Test"):
        os.makedirs("Test")

    prompt = f"Viết code Python cho yêu cầu sau:\n{command}"
    code = ask_gpt(prompt)

    try:
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(code)
        return f"✅ Đã tạo file code tại {save_path}", code
    except Exception as e:
        return f"❌ Lỗi khi lưu file: {e}", ""
