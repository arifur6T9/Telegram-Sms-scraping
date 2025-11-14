import os
import sys
import platform

def check_environment():
    if not os.path.exists(".env"):
        print("❌ .env file not found!")
        print("📝 Please run: python setup.py")
        return False
    
    with open(".env", "r") as f:
        content = f.read()
        if "your_api_hash_here" in content or "12345678" in content:
            print("❌ Please update .env file with your credentials")
            return False
    
    return True

def main():
    print("🤖 Starting Telegram SMS Scraper")
    print("=" * 40)
    print(f"📱 Platform: {platform.system()}")
    print("=" * 40)
    
    if not check_environment():
        sys.exit(1)
    
    try:
        from main import main as bot_main
        import asyncio
        
        print("🚀 Starting bot...")
        asyncio.run(bot_main())
        
    except ImportError as e:
        print(f"❌ Dependency error: {e}")
        print("📦 Please run: python setup.py")
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
    except Exception as e:
        print(f"🚨 Fatal error: {e}")

if __name__ == "__main__":
    main()
