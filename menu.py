import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://schools.mealviewer.com/school/WaltonHighSchool"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(URL, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

text = soup.get_text()

keywords = ["chicken","pizza","burger","taco","sandwich","fries","fruit","apple","milk","dip","nacho"]

lines = text.split("\n")
food = []

for line in lines:
    for k in keywords:
        if k.lower() in line.lower():
            food.append(line.strip())

# remove duplicates
food = list(dict.fromkeys(food))

message = "🍽 Walton Lunch Menu:\n\n"
for item in food:
    message += f"• {item}\n"

print(message)

# SEND TO DISCORD WEBHOOK
WEBHOOK = "PASTE_YOUR_WEBHOOK_HERE"

requests.post(WEBHOOK, json={"content": message})
