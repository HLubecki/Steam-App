import requests
import re  # do wekstraktowania profile Id
from bs4 import BeautifulSoup
import json
from converter import timeCon, dateCon, nameCon
from requests.exceptions import JSONDecodeError


class UserStats:
    def __init__(self, profileLink):
        self.profileLink = profileLink
        self.apiKey = "A7659EB2D8265D261E9AEE61B3983D5D"

    def get_user_id(self):
        link = self.profileLink

        if "/" in link:
            print("1")

            if link[-1] == "/":
                link = link[slice(-1)]
                print(link)
            try:
                self.userId = re.search(r'\d+$', link).group(0)
                return self.userId
            except AttributeError:
                print("dupa")

                return "dupa"

        elif "/" not in link:
            link = self.profileLink
            self.userId = link
            return self.userId

        # dodać wyjątki typy zmiennych itp. i wyjątek do ciągów znaków kończących się liczbami
    def get_api_link(self):
        id = self.get_user_id()
        print(id)
        self.apiLink = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=A7659EB2D8265D261E9AEE61B3983D5D&steamid=" + \
            str(id) + "&format=json"
        return self.apiLink

    def get_json(self):
        r = requests.get(self.get_api_link())
        try:
            jsonData = r.json()

            return (jsonData["response"])

        except JSONDecodeError:
            return None

    def get_data(self):
        base = self.get_json()

        self.gamesDict = dict()

        try:
            self.gameCount = base["game_count"]
        except KeyError:
            return self.gamesDict
        except TypeError:
            return "User not found, check your Steam URL"

        games = base["games"]

        try:
            index = 0
            for el in games:

                index += 1

                game = nameCon(el["appid"])
                playtime = timeCon(el["playtime_forever"])
                lastplay = dateCon(el["rtime_last_played"])

                record = {"id": index,
                          "game": game,
                          "playtime": playtime,
                          "lastplay": lastplay
                          }

                self.gamesDict[f"game{index}"] = record
            return self.gamesDict
        except KeyError:
            index = 0
            for el in games:

                index += 1

                game = nameCon(el["appid"])
                playtime = timeCon(el["playtime_forever"])

                record = {"id": index,
                          "game": game,
                          "playtime": playtime,
                          }

                self.gamesDict[f"game{index}"] = record

            return self.gamesDict

    def get_table(self):
        self.gameTable = []

        for rec in self.gamesDict.values():
            self.gameTable.append(
                (rec["id"], rec["game"], (rec["playtime"], "h")))

        return self.gameTable
