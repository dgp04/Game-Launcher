import configparser
import os

GAMES_INI = "games.ini"

def load_games_from_ini():
    games = []

    if not os.path.exists(GAMES_INI):
        return games

    config = configparser.ConfigParser()
    config.read(GAMES_INI, encoding="utf-8")

    for section in config.sections():
        game = {
            "name": section,
            "category": config.get(section, "category", fallback=""),
            "exe": config.get(section, "exe", fallback=""),
            "image": config.get(section, "image", fallback="")
        }
        games.append(game)

    return games
