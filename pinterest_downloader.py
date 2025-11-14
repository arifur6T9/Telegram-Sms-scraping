import requests
import os
import aiohttp
import re

class PinterestDownloader:
    def __init__(self):
        self.download_path = "downloads"
        os.makedirs(self.download_path, exist_ok=True)
    
    def extract_pinterest_urls(self, text):
        if not text:
            return []
            
        patterns = [
            r'https?://pin\.it/[^\s]+',
            r'https?://(?:www\.)?pinterest\.(?:com|fr|de|it|es|jp|ru|com\.br)/pin/[^\s]+',
            r'https?://(?:www\.)?pinterest\.(?:com|fr|de|it|es|jp|ru|com\.br)/[^\s]+'
        ]
        
        urls = []
        for pattern in patterns:
            urls.extend(re.findall(pattern, text))
        
        return urls

    async def download_pinterest_image(self, url):
        try:
            print(f"📥 Downloading from Pinterest: {url}")
            
            async with aiohttp.ClientSession() as session:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                
                async with session.get(url, headers=headers) as response:
                    if response.status == 200:
                        image_data = await response.read()
                        
                        filename = f"pinterest_{hash(url)}.jpg"
                        filepath = os.path.join(self.download_path, filename)
                        
                        with open(filepath, 'wb') as f:
                            f.write(image_data)
                        
                        print(f"✅ Pinterest image downloaded: {filepath}")
                        return filepath
                        
        except Exception as e:
            print(f"❌ Pinterest download failed: {e}")
            return None

pinterest_downloader = PinterestDownloader()
