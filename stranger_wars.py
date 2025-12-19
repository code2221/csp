import requests

class Strangerwars:

    url = "https://hawapi.theproject.id/api/v1/characters"

    def __init__(self):
        self.intro()
        self.characters = self.get_characters(8)

        while len(self.characters) > 1:
            self.characters = self.run_round(self.characters)
            print("On to the next battle!")
            print("                  ")

        winner = self.characters[0]
        print(f"Your favorite Stranger Things character is: {winner['first_name']} {winner['last_name']}")

    def intro(self):
        print("Welcome to the Stranger Things Character Battle!")
        print("This game is created in honor of the final season of stranger things!")
        print("Choose between two characters at a time, and you can enter 3 to refresh the choices")
        print("Let's get started!")
        print("          ")

    def fetch_random_character(self):
        response = requests.get(f"{self.url}/random")
        return response.json()

    def get_characters(self, count):
        characters = []
        while len(characters) < count:
            char = self.fetch_random_character()
            if char not in characters:
                characters.append(char)
        return characters

    def run_round(self, characters):
        winners = []
        for i in range(0, len(characters), 2):
            pair = [characters[i], characters[i+1]]
            while True:
                print("1:", pair[0]["first_name"], pair[0]["last_name"])
                print("2:", pair[1]["first_name"], pair[1]["last_name"])
                print("3: Refresh")
                choice = input("Choose 1, 2, or 3: ")
                if choice == "3":
                    pair = [self.fetch_random_character(), self.fetch_random_character()]
                elif choice in ("1","2"):
                    winners.append(pair[int(choice)-1])
                    break
                else:
                    print("Invalid input.")
        return winners

Strangerwars()
