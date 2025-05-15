from gtts import gTTS
import os
from playsound import playsound
import uuid

def speak(text):
    try:
        # Tạo tên file ngẫu nhiên để tránh lỗi trùng
        filename = f"speech_{uuid.uuid4().hex}.mp3"
        tts = gTTS(text=text, lang='vi')
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("❌ Lỗi khi phát âm:", e)
