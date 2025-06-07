# 📢 GitHub Release Notifier

A simple Python script that checks for new releases on a specified GitHub repository and sends a notification to a Telegram bot when a new version is available.

## 🚀 Features

- Checks the latest release from any public GitHub repository
- Sends a custom Telegram notification if a new version is detected
- Stores the last known release locally to avoid duplicate messages
- Multilingual support for messages via `messages.json`
- Lightweight and easy to schedule via cron or task scheduler

---

## 📁 Project Structure

```
github-release-notifier/
├── config.json      # Project and bot configuration
├── messages.json    # All message texts (can be translated)
├── main.py          # Main Python script
├── last_release.txt # Stores last known release tag
├── requirements.txt # Python dependencies
├── setup.sh         # Setup script for Linux/macOS
└── setup.bat        # Setup script for Windows
```

---

## ⚙️ Configuration

### `config.json`

```json
{
  "github_repo": "OWNER/REPO",
  "telegram_bot_token": "YOUR_BOT_TOKEN",
  "telegram_chat_id": "YOUR_CHAT_ID"
}
```

- Replace `OWNER/REPO` with the GitHub repository (e.g. `psf/requests`)
- Create a Telegram bot with [BotFather](https://t.me/BotFather)
- Get your `chat_id` by messaging your bot and checking the response with a simple script or bot logging

---

### `messages.json`

```json
{
  "error_fetching_release": "❌ Error fetching release data: {status_code}",
  "no_new_release": "🤷 No new release found.",
  "new_release_message": "📢 New release detected for {repo}: {new_release_tag} (previous was {old_release_tag})",
  "error_sending_telegram": "❌ Error sending Telegram message: {status_code}, {response_text}",
  "no_previous_release": "none"
}
```

Customize or translate these messages as needed.

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/loc4l/github-release-notifier.git
   cd github-release-notifier
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Edit the `config.json` file with your data.

---

## ▶️ Run the Script

```bash
python main.py
```

Or use the setup scripts:

- macOS/Linux:
  ```bash
  ./setup.sh
  ```

- Windows:
  ```bat
  setup.bat
  ```

---

## ⏱️ Automation Tips

### Linux (cron)

```bash
crontab -e
```

Add line (check every hour):

```
0 * * * * /usr/bin/python3 /path/to/github-release-notifier/main.py
```

### Windows (Task Scheduler)

1. Open Task Scheduler
2. Create Basic Task
3. Point to `python.exe` and pass `main.py` as argument

---

## 🧪 Example

When a new release is published on `psf/requests`, the bot will send:

```
📢 New release detected for psf/requests: v2.31.0
```

---

## 📄 License

MIT License. See `LICENSE` file for details.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📬 Contact

Feel free to reach out via GitHub issues or open a discussion.
