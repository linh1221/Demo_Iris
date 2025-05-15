import openai
import os
from dotenv import load_dotenv

# Nạp các biến môi trường từ file .env
load_dotenv()

# Thiết lập cấu hình API từ biến môi trường
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
openai.api_type = os.getenv("OPENAI_API_TYPE", "openai")
openai.api_version = os.getenv("OPENAI_API_VERSION", "2023-05-15")

# Mô hình được chỉ định trong .env
MODEL_NAME = os.getenv("OPENAI_API_MODEL", "gpt-3.5-turbo")

def ask_gpt(prompt):
    try:
        # Gửi yêu cầu đến OpenAI ChatCompletion API
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Bạn là trợ lý thân thiện."},
                {"role": "user", "content": prompt}
            ]
        )
        # Tách nội dung phản hồi và trả về
        return response.choices[0].message.content.strip()
    except openai.error.RateLimitError:
        return "Bạn đã vượt quá hạn mức sử dụng API. Vui lòng kiểm tra gói dịch vụ của bạn."
    except Exception as e:
        return f"Đã xảy ra lỗi: {e}"
