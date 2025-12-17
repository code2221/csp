import requests

def random_wikipedia_page():
    # Step 1: Get a random page title
    random_url = "https://en.wikipedia.org/w/api.php"
    headers = {
        "User-Agent": "RandomWikiBot/0.1 (chapman.kyle@pusd.us)"
    }
    params = {
        "action": "query",
        "list": "random",
        "rnnamespace": 0,   # 0 = main/article namespace
        "rnlimit": 1,
        "format": "json"
    }
    response = requests.get(random_url, params=params, headers=headers).json()
    title = response["query"]["random"][0]["title"]

    # Step 2: Get the page text for that title
    page_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "extracts",
        "explaintext": True,
        "titles": title,
        "format": "json"
    }
    page_response = requests.get(page_url, params=params, headers=headers).json()

    # Extract the page text
    page = next(iter(page_response["query"]["pages"].values()))
    text = page.get("extract", "")

    return title, text


# Example use:
'''title, text = random_wikipedia_page()
print("TITLE:", title)
print("TEXT:\n", text[:2000], "...")'''



def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    headers = {
        "User-Agent": "WeatherFetcher/0.1"
    }
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    r = requests.get(url, params=params, headers=headers)
    r.raise_for_status()  # optional but useful
    data = r.json()

    return data["current_weather"]


# Example:
'''weather = get_weather(34.1619, -118.0927)  # PHS
print(weather)'''

