import requests

class tournament:

    def __init__(self):
        self.size = self.choose_size()
        self.fact_number = 2**self.size
        self.facts = self.choose_facts()
        self.rounds_array = []
        self.winners_array = []
        while len(self.facts) > 1:
            self.make_rounds()
            for x in range(0,len(self.rounds_array)):
                self.pick_winner(x)
            self.facts = self.winners_array
            self.winners_array = []
            print("---------------")
            print("round complete.")
            print("---------------")
        print("your favorite fact was...")
        print(self.facts[0])
    
    def choose_size(self):
        print("what would you like the size of your tournament to be?")
        print("(minimum of 1, recommended maximum of 5.)")
        can_continue = False
        while not can_continue:
            try: 
                choice = int(input())
                if choice > 0:
                    if choice > 5:
                        print("are you sure? this will take a very long time to complete. (y or n)")
                        decision = input()
                        if decision == "y":
                            can_continue = True
                            return choice
                        elif decision == "n":
                            print("okay, please choose a new number.")
                            can_continue = False
                        else:
                            print("please say y or n.")
                            can_continue = False
                    else:
                        can_continue = True
                        return choice
                else:
                    print("please enter a number greater than 0.")
                    can_continue = False
            except ValueError:
                print("please input an integer.")

    def choose_facts(self):
        url = "https://meowfacts.herokuapp.com/"
        params = {"count" : self.fact_number}
        data = requests.get(url, params = params).json()
        return data["data"]

    def make_rounds(self):
        self.rounds_array = []
        for x in range(0,len(self.facts)//2):
            self.rounds_array.append([self.facts[2*x] , self.facts[2*x + 1]])
    
    def pick_winner(self, round : int):
        print("---------------")
        print("Which cat fact is cooler?")
        print(self.rounds_array[round][0])
        print(self.rounds_array[round][1])
        print("enter 1 if the first cat fact is cooler and 2 if the second cat fact is cooler.")
        can_continue = False
        while not can_continue:
            try: 
                choice = int(input())
                if choice == 1 or choice == 2:
                    can_continue = True
                    self.winners_array.append(self.rounds_array[round][choice-1])
                    print("---------------")
                    break
                else:
                    print("please enter 1 or 2.")
                    can_continue = False
            except ValueError:
                print("please input an integer.")
                can_continue = False

tournament()