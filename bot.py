import os
import requests
import json

token = os.environ["GITHUB_TOKEN"]
repo = os.environ["GITHUB_REPOSITORY"]

# Issue numarasını al
with open(os.environ["GITHUB_EVENT_PATH"]) as f:
    event = json.load(f)

issue_number = event["issue"]["number"]

# Yorum at
url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"

headers = {
    "Authorization": f"token {token}"
}

data = {
    "body": "🤖 Selam! Ben otomatik botum 🚀"
}

requests.post(url, json=data, headers=headers)
