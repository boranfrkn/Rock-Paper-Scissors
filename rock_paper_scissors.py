import random
class Computer:
    def __init__(self):
        self.get_choice = self.get_choice()
    def get_choice(self):
        random_choice = random.randint(1, 3)
        human = Human
        human_choice = human.set_choice(human)
        if random_choice == 1:
            computer_choice = "paper"
            if human_choice == "scissors":
                print(f"Well done. The computer chose {computer_choice} and failed")
            elif human_choice == "paper":
                print(f"There is a draw ({computer_choice})")
            else:
                print(f"Sorry, but the computer chose {computer_choice}")
        elif random_choice == 2:
            computer_choice = "rock"
            if human_choice == "paper":
                print(f"Well done. The computer chose {computer_choice} and failed")
            elif human_choice == "rock":
                print(f"There is a draw ({computer_choice})")
            else:
                print(f"Sorry, but the computer chose {computer_choice}")
        else:
            computer_choice = "scissors"
            if human_choice == "rock":
                print(f"Well done. The computer chose {computer_choice} and failed")
            elif human_choice == "scissors":
                print(f"There is a draw ({computer_choice})")
            else:
                print(f"Sorry, but the computer chose {computer_choice}")
class Human:
    def __init__(self):
        pass
    def set_choice(self):
        self.set_choice = input().lower()
        return self.set_choice
if __name__ == '__main__':
    cumputer = Computer()
