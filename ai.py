import random
from player import Player


class Ai(Player):
    def __init__(self,name):
        super().__init__(name)

    def choose_gesture(self):
        ran = random.choice("rock", "paper", "scissors", "spock", "lizard")
        self.choice == ran
        pass

       