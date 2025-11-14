import os
import platform
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv('API_ID', 0))
API_HASH = os.getenv('API_HASH', '')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')
SOURCE_GROUP = int(os.getenv('SOURCE_GROUP', 0))
DESTINATION_GROUP = int(os.getenv('DESTINATION_GROUP', 0))

CURRENT_PLATFORM = platform.system()
IS_TERMUX = 'com.termux' in os.getcwd()

if CURRENT_PLATFORM == "Windows" or not IS_TERMUX:
    RATE_LIMIT_DELAY = 1
    MAX_FILE_SIZE = 10 * 1024 * 1024
    DOWNLOAD_PATH = "downloads"
else:
    RATE_LIMIT_DELAY = 2
    MAX_FILE_SIZE = 5 * 1024 * 1024
    DOWNLOAD_PATH = "/data/data/com.termux/files/home/downloads"

os.makedirs(DOWNLOAD_PATH, exist_ok=True)

def validate_config():
    missing = []
    if not API_ID or API_ID == 0: missing.append('API_ID')
    if not API_HASH: missing.append('API_HASH') 
    if not BOT_TOKEN: missing.append('BOT_TOKEN')
    if not SOURCE_GROUP or SOURCE_GROUP == 0: missing.append('SOURCE_GROUP')
    if not DESTINATION_GROUP or DESTINATION_GROUP == 0: missing.append('DESTINATION_GROUP')
    
    if missing:
        print("❌ Missing configuration in .env file:")
        for item in missing:
            print(f"   - {item}")
        print("\n📝 Please edit .env file with your credentials")
        return False
    
    print(f"✅ Configuration validated - Platform: {CURRENT_PLATFORM}")
    return True
