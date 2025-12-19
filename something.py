import requests

class tournament:

    def __init__(self):
        self.size = self.choose_size()
        self.food_number = 2 ** self.size
        self.foods = self.choose_foods()
        self.rounds_array = []
        self.winners_array = []
        while len(self.foods) > 1:
            self.make_rounds()
            for x in range(0, len(self.rounds_array)):
                self.pick_winner(x)
            self.foods = self.winners_array
            self.winners_array = []
            print("---------------")
            print("round complete.")
            print("---------------")
        print("your favorite food was...")
        print(self.foods[0])

    def choose_size(self):
        print("what would you like the size of your food tournament to be?")
        print("(minimum of 1, recommended maximum of 5.)")
        can_continue = False
        while not can_continue:
            try:
                choice = int(input())
                if choice > 0:
                    if choice > 5:
                        print("are you sure? this will take a long time. (y or n)")
                        decision = input()
                        if decision == "y":
                            can_continue = True
                            return choice
                        elif decision == "n":
                            print("okay, please choose a new number.")
                        else:
                            print("please say y or n.")
                    else:
                        can_continue = True
                        return choice
                else:
                    print("please enter a number greater than 0.")
            except ValueError:
                print("please input an integer.")

    def choose_foods(self):
        url = "https://www.themealdb.com/api/json/v1/1/random.php"
        foods = []
        while len(foods) < self.food_number:
            data = requests.get(url).json()
            foods.append(data["meals"][0]["strMeal"])
        return foods

    def make_rounds(self):
        self.rounds_array = []
        for x in range(0, len(self.foods) // 2):
            self.rounds_array.append([self.foods[2 * x], self.foods[2 * x + 1]])

    def pick_winner(self, round: int):
        print("---------------")
        print("Which food do you like more?")
        print("1:", self.rounds_array[round][0])
        print("2:", self.rounds_array[round][1])
        print("enter 1 or 2")
        can_continue = False
        while not can_continue:
            try:
                choice = int(input())
                if choice == 1 or choice == 2:
                    can_continue = True
                    self.winners_array.append(self.rounds_array[round][choice - 1])
                    print("---------------")
                else:
                    print("please enter 1 or 2.")
            except ValueError:
                print("please input an integer.")

tournament()
