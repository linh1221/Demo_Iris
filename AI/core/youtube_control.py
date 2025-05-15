import os
import time
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def open_youtube_video(query):
    print(f"🔍 Đang tìm kiếm: {query}")
    search_query = quote_plus(query)
    url = f"https://www.youtube.com/results?search_query={search_query}"

    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Bỏ comment nếu không cần hiển thị Chrome

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    time.sleep(2)
    try:
        video = driver.find_element(By.ID, "video-title")
        video.click()
    except:
        print("❌ Không thể mở video đầu tiên.")

def close_youtube():
    print("🛑 Đang đóng YouTube...")
    os.system("taskkill /f /im chrome.exe")
