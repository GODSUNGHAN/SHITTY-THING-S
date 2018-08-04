import random


moves = {"Rock" : (0), "Scissor" : (1), "Paper" : (2)}


class RockScissorPaper:
    def __init__(self):

    def attack(self):
        raise NotImplementedError



    class player(RockScissorPaper):
        def attack(self):
            while True:
                choice = str.lower(input("\n RockScissorPaper"))

                if choice == "Rock":
                    if num == com:
                        print("Draw")
                    elif num + 1 == com or (num == 2 and com == 0):
                        print("Lose")
                    else:
                        print("win")

                if choice == "Scissor":
                    if num == com:
                        print("Draw")
                    elif num + 1 == com or (num == 2 and com == 0):
                        print("Lose")
                    else:
                        print("win")

                if choice == "Papaer":
                    if num == com:
                        print("Draw")
                    elif num + 1 == com or (num == 2 and com == 0):
                        print("Lose")
                    else:
                        print("win")

                else:
                    print("Input valid text")

com = random.randrange(1,3)
print(com)


