import os
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from pinterest_downloader import pinterest_downloader

class MediaHandler:
    @staticmethod
    async def handle_message(event, client, destination_group):
        try:
            sender = await event.get_sender()
            
            if hasattr(sender, 'username') and sender.username:
                credit = f"@{sender.username}"
            else:
                credit = getattr(sender, 'first_name', 'Unknown Source')
            
            message_text = event.message.text or ""
            
            pinterest_urls = pinterest_downloader.extract_pinterest_urls(message_text)
            
            if pinterest_urls:
                return await MediaHandler._handle_pinterest_with_group_text(
                    event, client, destination_group, credit, message_text, pinterest_urls
                )
            elif event.message.media and event.message.text:
                credited_caption = f"**Credit:** {credit}\n\n{event.message.text}"
                await client.send_file(
                    destination_group,
                    file=event.message.media,
                    caption=credited_caption
                )
            elif event.message.text:
                credited_text = f"**Credit:** {credit}\n\n{event.message.text}"
                await client.send_message(destination_group, credited_text)
            elif event.message.media:
                await client.send_file(
                    destination_group,
                    file=event.message.media,
                    caption=f"**Credit:** {credit}"
                )
            
            return True
            
        except Exception as e:
            print(f"Media handling error: {e}")
            return False

    @staticmethod
    async def _handle_pinterest_with_group_text(event, client, destination_group, credit, group_text, pinterest_urls):
        try:
            pinterest_url = pinterest_urls[0]
            image_path = await pinterest_downloader.download_pinterest_image(pinterest_url)
            
            if image_path and os.path.exists(image_path):
                caption = f"{group_text}\n\n**Credit:** {credit}"
                
                await client.send_file(
                    destination_group,
                    image_path,
                    caption=caption
                )
                
                os.remove(image_path)
                print("✅ Pinterest image + Group text sent successfully!")
                return True
            else:
                credited_text = f"**Credit:** {credit}\n\n{group_text}"
                await client.send_message(destination_group, credited_text)
                return True
                
        except Exception as e:
            print(f"Pinterest+Group text error: {e}")
            credited_text = f"**Credit:** {credit}\n\n{group_text}"
            await client.send_message(destination_group, credited_text)
            return True

media_handler = MediaHandler()
