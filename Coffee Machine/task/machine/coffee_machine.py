class CoffeeMachine:
    menu = {1: [250, 0, 16, 4],
            2: [350, 75, 20, 7],
            3: [200, 100, 12, 6]}
    buy_command = "buy"
    fill_command = "fill"
    take_command = "take"
    exit_command = "exit"
    remaining_command = "remaining"

    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cup = 9

    def statik(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee_beans} of coffee beans')
        print(f'{self.cup} of disposable cups')
        print(f'${self.money} of money')

    def ferst_level_menu(self):
        print('Write action (buy, fill, take, remaining, exit):')
        return input()

    def second_level_menu(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        return input()

    def fill(self):
        print("Write how many ml of water you want to add:")
        while True:
            try:
                self.water += int(input())
            except ValueError:
                print("Введите число")
            else:
                break
        print("Write how many ml of milk you want to add:")
        while True:
            try:
                self.milk += int(input())
            except ValueError:
                print("Введите число")
            else:
                break
        print("Write how many grams of coffee beans you want to add:")
        while True:
            try:
                self.coffee_beans += int(input())
            except ValueError:
                print("Введите число")
            else:
                break
        print("Write how many disposable coffee cups you want to add:")
        while True:
            try:
                self.cup += int(input())
            except ValueError:
                print("Введите число")
            else:
                break

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def proverka(self, info):
        s = ''
        flag = True
        if self.water < info[0]:
            s = 'water, '
            flag = False
        if self.milk < info[1]:
            s +='milk, '
            flag = False
        if self.coffee_beans < info[2]:
            s += 'coffee_beans, '
            flag = False
        if self.cup == 0:
            s += 'cup '
            flag = False
        return s, flag


    def update(self, info):
        self.cup -= 1
        self.water -= info[0]
        self.milk -= info[1]
        self.coffee_beans -= info[2]
        self.money += info[3]

    def buy(self):
        while True:
            command = self.second_level_menu()
            if command not in ['1', '2', '3', "back"]:
                print("Incorrect input, try again")
            elif command.lower() == 'back':
                break
            else:
                proverka = self.proverka(CoffeeMachine.menu[int(command)])
                if proverka[1]:
                    print("I have enough resources, making you a coffee!")
                    self.update(CoffeeMachine.menu[int(command)])
                    break
                else:
                    print(f"Sorry, not enough {proverka[0][:-2]}!")
                    break

    def main(self):
        command = None
        while command != CoffeeMachine.exit_command:
            command = self.ferst_level_menu()
            if command == self.buy_command:
                self.buy()
            elif command == self.fill_command:
                self.fill()
            elif command == self.remaining_command:
                self.statik()
            elif command == self.take_command:
                self.take_money()
            else:
                exit()
            print()

run = CoffeeMachine()
run.main()


