import requests
from bs4 import BeautifulSoup

r = requests.get("https://tw.yahoo.com/")

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, "html.parser")

    stories = soup.find_all("span")
    print(stories)
    for s in stories:
        print(s.text)
