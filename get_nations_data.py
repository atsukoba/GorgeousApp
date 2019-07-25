import requests
from bs4 import BeautifulSoup


res = requests.get("https://qiita.com/tao_s/items/32b90a2751bfbdd585ea")
if res.ok:
    data = BeautifulSoup(res.content, "lxml")
with open("data/nations.csv", "w") as f:
    f.write(data.find("div", class_="code-frame").text.strip())
