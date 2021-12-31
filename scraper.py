import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys

URL = "https://varldenidag.se/"
page = requests.get(URL)
today = datetime.today().strftime("%Y-%m-%d")

results = pd.read_csv("results.csv")

if today in list(results["date"]):
    print("already executed, skipping")
    sys.exit(0)

soup = BeautifulSoup(page.content, "html.parser")
titles = soup.find_all("h2")
for title in titles:
    results = results.append({"date": today, "title": title.text}, ignore_index=True)

results.to_csv("results.csv", index=False)
