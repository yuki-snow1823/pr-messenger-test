import os
import requests

# コメントしたいIssue番号
issue_number = 1  # https://github.com/yuki-snow1823/pr-messenger-test/issues/1

# 投稿する内容
text = "GitHub Actionsからのテストコメントです！"

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