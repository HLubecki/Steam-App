# A7659EB2D8265D261E9AEE61B3983D5D
# https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=A7659EB2D8265D261E9AEE61B3983D5D&steamid=76561198201332390&format=json


import requests
from bs4 import BeautifulSoup


def pobierz_pelny_link(czesc_linku):
    url = f"https://store.steampowered.com/app/{czesc_linku}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    full_link = soup.find('link', {'rel': 'canonical'}).get('href')
    return full_link


czesc_linku = "21980"
pelny_link = pobierz_pelny_link(czesc_linku)
print(pelny_link)

# użytnik podaje linka do profilu z profilu wyciągane jest userID
# userId jest przekazywane do linku api
# zlinku api pobierana jest baza
# z api przekazywane są id gry, godziny i ostatnio grane
# id gry zamineniane jest na nazwę
# wszystko tworzy struktura danych
# prezencja
