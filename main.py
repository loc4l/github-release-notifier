import requests
import json
import os

CONFIG_FILE = 'config.json'
MESSAGES_FILE = 'messages.json'
LAST_RELEASE_FILE = 'last_release.txt'

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_latest_release(repo, messages):
    url = f'https://api.github.com/repos/{repo}/releases/latest'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['tag_name']
    else:
        print(messages["error_fetching_release"].format(status_code = response.status_code))
        return None

def get_saved_release():
    if os.path.exists(LAST_RELEASE_FILE):
        with open(LAST_RELEASE_FILE, 'r') as f:
            return f.read().strip()
    return None

def save_release(tag):
    with open(LAST_RELEASE_FILE, 'w') as f:
        f.write(tag)

def send_telegram_message(token, chat_id, message, messages):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data = payload)
    if response.status_code != 200:
        print(messages["error_sending_telegram"].format(
            status_code = response.status_code,
            response_text = response.text
        ))

def main():
    config = load_json(CONFIG_FILE)
    messages = load_json(MESSAGES_FILE)

    repo = config['github_repo']
    token = config['telegram_bot_token']
    chat_id = config['telegram_chat_id']

    latest_release = get_latest_release(repo, messages)
    if not latest_release:
        return

    saved_release = get_saved_release()

    if latest_release != saved_release:
        message = messages["new_release_message"].format(
            repo = repo,
            new_release_tag = latest_release,
            old_release_tag = saved_release if saved_release else messages["no_previous_release"]
        )
        send_telegram_message(token, chat_id, message, messages)
        save_release(latest_release)
    else:
        print(messages["no_new_release"])

if __name__ == "__main__":
    main()
