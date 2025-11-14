import os
import sys
import asyncio
import platform
from telethon import TelegramClient, events

try:
    from config import API_ID, API_HASH, BOT_TOKEN, SOURCE_GROUP, DESTINATION_GROUP, validate_config
    from media_handler import media_handler
except ImportError as e:
    print(f"❌ Required modules not found: {e}")
    print("📦 Please run: python setup.py")
    sys.exit(1)

class UniversalBot:
    def __init__(self):
        self.client = None
        self.platform = platform.system()
        
    def display_banner(self):
        banner = f"""
╔══════════════════════════════════════╗
║           TELEGRAM SMS SCRAPER       ║
║               {self.platform:^16}          ║
╚══════════════════════════════════════╝
📱 Platform: {self.platform}
📊 Source Group: {SOURCE_GROUP}
🎯 Destination Group: {DESTINATION_GROUP}
        """
        print(banner)
    
    async def initialize(self):
        self.display_banner()
        
        try:
            session_file = f"session_{self.platform.lower()}"
            
            self.client = TelegramClient(
                session_file,
                API_ID,
                API_HASH
            ).start(bot_token=BOT_TOKEN)
            
            print("✅ Bot initialized successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Initialization failed: {e}")
            return False
    
    async def start_handlers(self):
        @self.client.on(events.NewMessage(chats=SOURCE_GROUP))
        async def message_handler(event):
            try:
                print(f"📨 New message: {event.message.id}")
                
                success = await media_handler.handle_message(
                    event, 
                    self.client, 
                    DESTINATION_GROUP
                )
                
                if success:
                    print(f"✅ Processed: {event.message.id}")
                else:
                    print(f"⚠️ Failed: {event.message.id}")
                    
            except Exception as e:
                print(f"🚨 Error: {e}")
        
        print("🎯 Message handlers activated!")
    
    async def run(self):
        if await self.initialize():
            await self.start_handlers()
            
            print("\n" + "=" * 50)
            print("🤖 BOT IS RUNNING!")
            print("📍 Press Ctrl+C to stop")
            print("=" * 50 + "\n")
            
            await self.client.run_until_disconnected()

async def main():
    if not validate_config():
        return
    
    bot = UniversalBot()
    await bot.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
    except Exception as e:
        print(f"🚨 Fatal error: {e}")
