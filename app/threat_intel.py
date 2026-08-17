import json


def load_indicators():
    with open("data/indicators.json", "r") as file:
        return json.load(file)


def search_indicator(indicator):
    data = load_indicators()

    for category in data.values():
        for item in category:
            if item["indicator"].lower() == indicator.lower():
                return item

    return None
