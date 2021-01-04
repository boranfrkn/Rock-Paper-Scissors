class Computer:
    def __init__(self):
        self.get_choice = self.get_choice()
    def get_choice(self):
        human = Human
        human_choice = human.set_choice(human)
        if human_choice == "paper":
            computer_choice = "scissors"
            print(f"Sorry, but the computer chose {computer_choice}")
        elif human_choice == "rock":
            computer_choice = "paper"
            print(f"Sorry, but the computer chose {computer_choice}")
        elif human_choice == "scissors":
            computer_choice = "rock"
            print(f"Sorry, but the computer chose {computer_choice}")
class Human:
    def __init__(self):
        pass
    def set_choice(self):
        self.set_choice = input().lower()
        return self.set_choice
if __name__ == '__main__':
    cumputer = Computer()
