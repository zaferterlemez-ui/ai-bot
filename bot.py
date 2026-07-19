import os
import requests

token = os.environ["GITHUB_TOKEN"]
issue_number = os.environ["ISSUE_NUMBER"]
repo = os.environ["REPO"]

url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

data = {
    "body": "🤖 Selam! %100 çalışan bot aktif 🚀"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.text)
