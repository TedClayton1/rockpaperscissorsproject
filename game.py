from human import Human
x = 0
class Game:
    def __init__(self):
        self.player_1 = None
        self.player_2 = None
        pass

    def run_game(self):
        self.display_welcome_rules ()
        pass


    def display_welcome_rules(self):

        print('Welcome to the amazing game of paper, rock, scissors, lizard and spock. This is a best of 3 series with the person winning 2 games is the winner. How many people are playing? Please enter 1 for one player and 2 for two players.')

    def compare_gestures(self):
        self.player_1.choose_gesture()
        self.player_2.choose_gesture()

        if self.player_1.choice == self.player_2.choice:
            print(f"It's a tie now! Both users chose {self.player_1.choice} ")
        elif self.player_1.choice == 'Rock' and self.player_2.choice == 'Paper':
            self.player_2.score += 1
            print('Player Two has won the round with Paper')
        elif self.player_1.choice == 'Scissors' and self.player_2.choice == 'lizard':
            self.player_1.score += 1
            print('Player One has won the round with lizard')
        elif self.player_1.choice == 'scissors' and self.player_2.choice == 'Spock':
            self.player_2.score += 1
            print('Player Two has won the round with scissors')
        elif self.player_1.choice == 'lizard' and self.player_2.choice == 'rock':
            self.player_2.score += 1 
            print('Player Two has won the round with lizard')
        elif self.player_1.choice == 'scissors' and self.player_2.choice == 'paper':
            self.player_1.score += 1   
            print('Player One has won the round with paper')
        elif self.player_1.choice == 'spock' and self.player_2.choice == 'lizard':
            self.player_2 += 1
            print('Player Two has won the round with spock')
        elif self.player_1.choice == 'paper' and self.player_2.choice == 'lizard':
            self.player_2.score += 1
            print('Player Two has won the round with paper')
        elif self.player_1.choice == 'paper' and self.player_2.choice == 'spock':
            self.player_1.score += 1
            print('Player One has won the round with spock') 
        elif self.player_1.choice == 'rock' and self.player_2.choice == 'spock':
            self.player_2.score += 1
            print('Player Two has won the round with rock')










        # if choose_gesture == ai_choice: 
            
        # elif user_choice == "rock":
        #     if ai_choice == "scissors":
        #         print("Rock smashes scissors, you win the game!")
        #     else:
        #         print("Paper covers rock, you lose")
        # elif user_choice == "paper":
        #     if ai_choice == "rock":
        #         print("Paper covers rock you win!") 
        #     else:
        #         print("Scissors cut paper, you lose")
        # elif user_choice == "scissors":
        #     if ai_choice == "paper":
        #         print("Scissors cut paper, you win!")
        #     else:
        #         print("Rock smashes scissors, you lose!")
        # elif user_choice == "lizard":
        #     if ai_choice == "spock":
        #         print("Lizard poisons spock, you win.")
        #     else:
        #         print("Scissors decapitates lizard, you lose")
        # elif user_choice == "Spock":
        #     if ai_choice =="rock":
        #         print("Spock vaporizes rock, you win.")
        #     else:
        #         print("Paper disproves spock, you lose")
        # else:
        #     print(f"You used {user_choice} which isn't a valid choice.")

    
 x = x+1
 print(x game won by you.)   
               

        










#     def __init__(self):
#         pass
#     def run_game(self):
#         self.runninggame != self.runninggame
#     def display_welcome_rules(self):
#         self.displayingwelcome != self.displayingwelcome
#     def choose_gamemode(self):
#         self.choosinggamemode != self.choosinggamemode
#     def p1_turn(self):
#         self.playeroneturn != self.playeroneturn
#     def p2_turn(self):
#         self.playertwoturn != self.playeroneturn
#     def compare(self):
#         self.comparing != self.comparing
#     def display_round_winner(self):
#         self.displayingwinner != self.displayingwinner
#     def give_points(self):
#         self.givingpoints != self.givingpoints
#     def check_for_winner(self):
#         self.checkingforwinner != self.checkingforwinner
#   



# # We want to account for and handle bad user input, ensuring that any user input is validated
# # and reobtained if necessary


# while True:
#     print("Make your choice please")
#    user_choice = input(" Type rock, paper, scissors, spock, or lizard: ")  
#    if user_choice in self.choices:
#     ai_choice = random.choice(CHOICES)
#     print(f' "You chose {user_choice}, the computer chose {computer_choice}")
#    else:
#       print(f'You chose {user_choice} which isn't a valid choice")

    # repeat = input("Do you want more (y/n): ")
    # if repeat.lower() == "n":
#        break

# print("Maybe you'll have better luck next time.")
#         
  
#     if number <=5:
#         print('Would you please re-enter a number 1-5.')
#         continue
#     break

# print(f'The number you chose is {number}.')

















