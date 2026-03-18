import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

URL = "https://schools.mealviewer.com/school/WaltonHighSchool"

headers = {"User-Agent": "Mozilla/5.0"}
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

food = list(dict.fromkeys(food))

message = "🍽 Walton Lunch Menu:\n\n"
for item in food:
    message += f"• {item}\n"

# EMAIL SETUP
sender = "gatorkid5041@gmail.com"
password = "ouypxtuyhgmwpygu"
receiver = "masonpassarella10@gmail.com"

msg = MIMEText(message)
msg["Subject"] = "Walton Lunch Menu"
msg["From"] = sender
msg["To"] = receiver

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.send_message(msg)

print("Email sent!")
