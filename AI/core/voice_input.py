# voice_input.py
import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Đang nghe...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="vi-VN")  # Tiếng Việt
            print("🗣️ Bạn nói:", text)
            return text
        except:
            print("Không hiểu gì cả 😅")
            return ""
