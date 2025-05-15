import sys
import os
from core.youtube_control import open_youtube_video, close_youtube
from core.voice_input import listen
from core.AI import ask_gpt
from core.voice_output import speak
from core.weather import get_weather
from core.code_writer import write_code_from_command

print("🤖 Trợ lý AI đã sẵn sàng!")

while True:
    mode = input("\n👉 Bạn muốn dùng giọng nói hay nhập tay? (nói/nhập/thoát): ").strip().lower()

    if mode == "thoát":
        speak("Tạm biệt bạn nhé!")
        break

    if mode == "nói":
        user_input = listen()
    elif mode == "nhập":
        user_input = input("🗣️ Bạn: ")
    else:
        print("⚠️ Lựa chọn không hợp lệ. Vui lòng nhập 'nói', 'nhập' hoặc 'thoát'.")
        continue

    if not user_input:
        print("⚠️ Không nhận được nội dung. Hãy thử lại.")
        continue

    print(f"👂 Bạn nói: {user_input}")
    user_input_lower = user_input.lower()

    if "thời tiết" in user_input_lower:
        weather = get_weather()
        speak(weather)

    elif "youtube" in user_input_lower or "phát nhạc" in user_input_lower or "mở nhạc" in user_input_lower:
        speak("Bạn muốn nghe gì trên YouTube?")
        query = listen() if mode == "nói" else input("🔎 Nhập nội dung tìm kiếm: ")
        if query:
            open_youtube_video(query)

    elif "đóng youtube" in user_input_lower or "tắt youtube" in user_input_lower:
        close_youtube()

    elif any(keyword in user_input_lower for keyword in ["viết", "hàm", "function", "tạo code"]):
        result_msg, generated_code = write_code_from_command(user_input)
        speak(result_msg)
        print(f"📄 Code được tạo:\n\n{generated_code}")

    elif user_input_lower in ["thoát", "tạm biệt", "kết thúc"]:
        speak("Tạm biệt bạn nhé! Hẹn gặp lại.")
        break

    else:
        response = ask_gpt(user_input)
        speak(response)
        print(f"🤖 Trợ lý AI: {response}")
