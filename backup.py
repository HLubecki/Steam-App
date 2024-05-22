import requests
import re  # do wekstraktowania profile Id
from bs4 import BeautifulSoup
import json
import pprint


class UserStats:
    def __init__(self, profileLink):
        self.profileLink = profileLink
        self.apiKey = "A7659EB2D8265D261E9AEE61B3983D5D"

    def get_user_id(self):
        link = self.profileLink

        if link[-1] == "/":
            link = link[slice(-1)]
            print(link)
        try:
            self.userId = re.search(r'\d+$', link).group(0)
            return self.userId
        except AttributeError:
            print("dupa")

            return "dupa"

        # dodać wyjątki typy zmiennych itp. i wyjątek do ciągów znaków kończących się liczbami
    def get_api_link(self):
        id = self.get_user_id()
        print(id)
        self.apiLink = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=A7659EB2D8265D261E9AEE61B3983D5D&steamid=" + \
            str(id) + "&format=json"
        return self.apiLink

    def get_json(self):
        r = requests.get(self.get_api_link())
        jsonData = r.json()

        return (jsonData["response"])

    def get_data(self):
        base = self.get_json()

        self.gamesDict = dict()
        self.gameCount = base["game_count"]

        games = base["games"]

        index = 0
        for el in games:

            index += 1

            game = el["appid"]
            playtime = el["playtime_forever"]
            lastplay = el["rtime_last_played"]

            record = {"id": index,
                      "game": game,
                      "playtime": playtime,
                      "lastplay": lastplay
                      }

            self.gamesDict[f"game{index}"] = record
        print(self.gamesDict)
