from datetime import datetime
import requests
from bs4 import BeautifulSoup


def timeCon(value):

    h = value // 60
    min = value % 60
    partMin = round((min / 60), 1)
    fullTime = h + partMin
    return fullTime


def dateCon(value):
    date = datetime.fromtimestamp(value)

    if date.day < 10:
        day = "0" + str(date.day)
    else:
        day = date.day
    if date.month < 10:
        month = "0" + str(date.month)
    else:
        month = date.month

    year = date.year
    return (str(day) + ":" + str(month) + ":" + str(year))


def nameCon(value):
    url = f"https://store.steampowered.com/app/{value}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    full_link = soup.find('link', {'rel': 'canonical'}).get('href')

    if full_link[-1] == "/":
        full_link = full_link[slice(-1)]

    elements = full_link.split("/")
    gameName = elements[-1]
    gameName = gameName.split("_")
    gameName = " ".join(gameName)

    return gameName
