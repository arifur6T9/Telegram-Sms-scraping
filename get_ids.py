import asyncio
import os
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

async def get_group_ids():
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    
    if not api_id or not api_hash:
        print("❌ Please set API_ID and API_HASH in .env file first")
        return
    
    async with TelegramClient('session_finder', api_id, api_hash) as client:
        await client.start()
        
        print("🔍 Finding your groups and channels...")
        print("=" * 60)
        
        async for dialog in client.iter_dialogs():
            if dialog.is_group or dialog.is_channel:
                print(f"🏷️ {dialog.name:30} -> ID: {dialog.id}")
        
        print("=" * 60)
        print("📝 Copy the ID and add to .env file")

if __name__ == "__main__":
    asyncio.run(get_group_ids())
