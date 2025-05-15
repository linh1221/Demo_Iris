import requests
from bs4 import BeautifulSoup

def get_weather(city="Hà Nội"):
    try:
        city = city.replace(" ", "+")
        url = f"https://www.google.com/search?q=thời+tiết+{city}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        location = soup.select_one("#wob_loc")
        time = soup.select_one("#wob_dts")
        weather = soup.select_one("#wob_dc")
        temp = soup.select_one("#wob_tm")

        if None in (location, time, weather, temp):
            return "⚠️ Không lấy được thông tin thời tiết từ Google."

        return f"📍 {location.text}, {time.text}: {weather.text}, {temp.text}°C."
    except Exception as e:
        return f"⚠️ Lỗi khi lấy thời tiết: {e}"
