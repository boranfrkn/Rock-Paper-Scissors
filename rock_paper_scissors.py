import random
class Computer:
    def __init__(self):
        self.get_choice = self.get_choice()
    def get_choice(self):
        human = Human
        human_choice = human.set_choice(human)
        rules = {
            'scissors': 'rock',
            'rock': 'paper',
            'paper': 'scissors'
        }
        computer_choice = random.choice(list(rules.keys()))
        if human_choice in rules.keys():
            if human_choice == computer_choice:
                print(f"There is a draw ({computer_choice})")
            elif rules[human_choice] == computer_choice:
                print(f"Sorry, but the computer chose {computer_choice}")
            else:
                print(f"Well done. The computer chose {computer_choice} and failed")
class Human:
    def __init__(self):
        pass
    def set_choice(self):
        self.set_choice = input().lower()
        return self.set_choice
if __name__ == '__main__':
    cumputer = Computer()
