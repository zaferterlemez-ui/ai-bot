import os
import requests

token = os.environ["GITHUB_TOKEN"]

repo = os.environ["GITHUB_REPOSITORY"]
issue_number = os.environ["GITHUB_REF"].split("/")[-1]

url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"

headers = {
    "Authorization": f"token {token}"
}

data = {
    "body": "🤖 Merhaba! Ben otomatik AI botum. Issue'nu gördüm 🚀"
}

requests.post(url, json=data, headers=headers)
