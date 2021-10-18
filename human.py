from player import Player

class Human(Player):
    def __init__(self, gesture):
        self.gesture = gesture
        super().__init__()
    
    def choose_gesture(self)