import os
import sys
import subprocess
import platform

def check_python():
    try:
        version = sys.version_info
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
        return version.major == 3 and version.minor >= 7
    except:
        print("❌ Python not found or version too old")
        return False

def install_requirements():
    print("📦 Installing dependencies...")
    
    requirements = [
        "telethon",
        "requests", 
        "python-dotenv",
        "aiohttp"
    ]
    
    for package in requirements:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} installed")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")

def create_directories():
    dirs = ["downloads", "logs", "session_files"]
    for dir_name in dirs:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            print(f"✅ Created {dir_name}/ directory")

def setup_environment():
    if not os.path.exists(".env"):
        if os.path.exists(".env.example"):
            import shutil
            shutil.copy(".env.example", ".env")
            print("✅ Created .env file from .env.example")
        else:
            print("❌ .env.example not found")
    else:
        print("✅ .env file already exists")

def main():
    print("🚀 Telegram SMS Scraper - Universal Setup")
    print("=" * 50)
    print(f"📱 Platform: {platform.system()}")
    print("=" * 50)
    
    if not check_python():
        print("❌ Please install Python 3.7+ first")
        return
    
    install_requirements()
    create_directories()
    setup_environment()
    
    print("\n✅ Setup completed successfully!")
    print("\n📝 Next steps:")
    print("1. Edit .env file with your credentials")
    print("2. Run: python start.py")
    print("3. Or find group IDs: python get_ids.py")

if __name__ == "__main__":
    main()
