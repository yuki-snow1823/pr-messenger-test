import os
import requests
import json

# コメントしたいIssue番号
issue_number = 1  # https://github.com/yuki-snow1823/pr-messenger-test/issues/1

# PR情報をGitHub Actionsのイベントから取得
event_path = os.environ.get('GITHUB_EVENT_PATH')
if event_path and os.path.exists(event_path):
    with open(event_path, 'r') as f:
        event = json.load(f)
else:
    event = {}

pr = event.get('pull_request', {})
pr_title = pr.get('title', 'PRタイトル不明')
pr_url = pr.get('html_url', 'URL不明')
pr_user = pr.get('user', {}).get('login', 'ユーザー不明')

# 投稿する内容
text = f"PRがマージされました！\nタイトル: {pr_title}\nリンク: {pr_url}\n提案者: {pr_user}"

# GitHub APIエンドポイント
repo = os.environ.get('GITHUB_REPOSITORY', 'yuki-snow1823/pr-messenger-test')
url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"

headers = {
    "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
    "Accept": "application/vnd.github+json"
}
payload = {
    "body": text
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code, response.text) 