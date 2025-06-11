import os
import requests
import json

# GitHub Actionsのイベント情報を取得
event_path = os.environ.get('GITHUB_EVENT_PATH')
if event_path and os.path.exists(event_path):
    with open(event_path, 'r') as f:
        event = json.load(f)
else:
    event = {}

pr = event.get('pull_request', {})
pr_title = pr.get('title', 'PRタイトル')
pr_url = pr.get('html_url', 'PRリンク')
pr_user = pr.get('user', {}).get('login', 'ユーザー名')

text = f"PRがマージされました！\nタイトル: {pr_title}\nリンク: {pr_url}\n提案者: {pr_user}"

# X APIに投稿
headers = {
    "Authorization": f"Bearer {os.environ['X_BEARER_TOKEN']}",
    "Content-Type": "application/json"
}
payload = {
    "text": text
}
response = requests.post("https://api.twitter.com/2/tweets", headers=headers, json=payload)
print(response.status_code, response.text) 