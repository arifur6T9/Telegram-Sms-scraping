# Telegram SMS Scraper 🤖

A powerful and versatile Telegram bot that automatically copies messages from one group to another with intelligent media handling and credit system support.

## ✨ Features

- **🔄 Auto Message Copying**: Automatically copies messages from source group to destination group
- **📸 Pinterest Integration**: Detects Pinterest URLs and downloads images automatically
- **👤 Smart Credit System**: Attributes messages to original senders with username credits
- **📱 Dual Platform Support**: Works on both Termux (Android) and Windows
- **🖼️ Media Support**: Handles images, text, and combined media+text messages
- **⚡ Rate Limiting**: Built-in protection against API limits and bans
- **🔒 Safe & Secure**: No hardcoded credentials, uses environment variables

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Telegram API credentials from [my.telegram.org](https://my.telegram.org)
- Bot Token from [@BotFather](https://t.me/BotFather)

### Installation

#### Method 1: Using Git
```bash
git clone https://github.com/arifur6T9/Telegram-SMS-Scraper.git
cd Telegram-SMS-Scraper
python setup.py
```

#### Method 2: Manual Download
1. Download all files from the repository
2. Run setup script:
```bash
python setup.py
```

### Configuration

1. **Get API Credentials**:
   - Visit [my.telegram.org](https://my.telegram.org)
   - Go to API Development Tools
   - Create new application and get `API_ID` and `API_HASH`

2. **Get Bot Token**:
   - Message [@BotFather](https://t.me/BotFather) on Telegram
   - Use `/newbot` command
   - Copy the bot token

3. **Configure Environment**:
   - Copy `.env.example` to `.env`
   - Edit `.env` with your credentials:
   ```env
   API_ID=12345678
   API_HASH=your_api_hash_here
   BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
   SOURCE_GROUP=-1001234567890
   DESTINATION_GROUP=-1009876543210
   ```

4. **Find Group IDs**:
   ```bash
   python get_ids.py
   ```

### Usage

```bash
# Start the bot
python start.py
```

## 📸 How It Works

### Input (Source Group):
```
Check this amazing design: https://pin.it/example123

[🔴] Approved Scrapper
[🔴] CC | VBV: UNKNOWN
[🔴] Bin: 441451 | Country: UNITED STATES
[🔴] Type: DEBIT - VISA
```

### Output (Your Group):
```
[🖼️ Pinterest Image Displayed]

[🔴] Approved Scrapper
[🔴] CC | VBV: UNKNOWN
[🔴] Bin: 441451 | Country: UNITED STATES
[🔴] Type: DEBIT - VISA

**Credit:** @original_sender
```

## 🛠️ Project Structure

```
Telegram-SMS-Scraper/
├── main.py                 # Main bot logic
├── config.py              # Configuration management
├── media_handler.py       # Media processing
├── pinterest_downloader.py # Pinterest integration
├── setup.py              # Automated setup script
├── start.py              # Bot starter script
├── get_ids.py            # Group ID finder utility
├── requirements.txt      # Python dependencies
├── .env.example          # Environment template
├── README.md             # Documentation
└── .gitignore           # Git ignore rules
```

## 🔧 Technical Details

### Supported Platforms
- **Android**: Termux app
- **Windows**: Command Prompt/PowerShell
- **Linux**: Terminal

### Dependencies
- `telethon` - Telegram API client
- `requests` - HTTP requests
- `python-dotenv` - Environment management
- `aiohttp` - Async HTTP client
- `Pillow` - Image processing

### Message Types Handled
- Text messages with Pinterest URLs
- Image messages with captions
- Text-only messages
- Media-only messages

## ⚙️ Advanced Configuration

### Rate Limiting
The bot includes built-in rate limiting to prevent API bans:
- Windows: 1 second delay between messages
- Termux: 2 seconds delay between messages

### File Size Limits
- Windows: 10MB maximum file size
- Termux: 5MB maximum file size (mobile optimized)

## 🐛 Troubleshooting

### Common Issues

**Bot not starting:**
```bash
# Check dependencies
pip install -r requirements.txt

# Validate configuration
python -c "from config import validate_config; validate_config()"
```

**Group IDs not found:**
```bash
# Make sure bot is added to groups
python get_ids.py
```

**Pinterest images not downloading:**
- Check internet connection
- Verify Pinterest URL format
- Check download permissions

### Error Messages
- `❌ Missing configuration`: Edit .env file with credentials
- `❌ Initialization failed`: Check API credentials
- `🚨 Handler error`: Check bot permissions in groups

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/arifur6T9/Telegram-SMS-Scraper/issues)
- **Telegram**: @cybersecurity_Jubo

## 🎯 Use Cases

- **Content Sharing**: Automatically share messages between related groups
- **Backup**: Create backups of important messages
- **Moderation**: Monitor and copy messages for review
- **News Distribution**: Share news across multiple channels
- **Community Management**: Keep multiple groups synchronized

---

**⭐ Star this repository if you find it helpful!**

**🔔 Watch for updates and new features!**

**🐛 Report issues to help improve the bot!**
