import random


class Computer:
    def __init__(self):
        pass

    def rules(self):
        rules = {
            'scissors': 'rock',
            'rock': 'paper',
            'paper': 'scissors'
        }
        return rules

    def get_choice(self):
        rules = self.rules()
        self.computer_choice = random.choice(list(rules.keys()))
        return self.computer_choice

class Game:
    def __init__(self):
        self.game = self.game()

    def game(self):
        human_choice = input().lower()
        computer = Computer()
        rules = computer.rules()
        computer_choice = computer.get_choice()
        while human_choice != "!exit":
            if human_choice not in rules.keys():
                print("Invalid input")
                human_choice = input().lower()
            else:
                if human_choice == computer_choice:
                    print(f"There is a draw ({computer_choice})")
                    computer_choice = computer.get_choice()
                    human_choice = input().lower()
                elif rules[human_choice] == computer_choice:
                    print(f"Sorry, but the computer chose {computer_choice}")
                    computer_choice = computer.get_choice()
                    human_choice = input().lower()
                else:
                    print(f"Well done. The computer chose {computer_choice} and failed")
                    computer_choice = computer.get_choice()
                    human_choice = input().lower()
        else:
            print("Bye!")


if __name__ == '__main__':
    game = Game()
