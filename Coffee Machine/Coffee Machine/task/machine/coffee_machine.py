# Write your code here
# print('''Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!''')
# cup_of_coffees = int(input("Write how many cups of coffee you will need:\n"))
# print("For",cup_of_coffees,"cups of coffee you will need:")
# print(cup_of_coffees*200,"ml of water")
# print(cup_of_coffees*50,"ml of milk")
# print(cup_of_coffees*15,"g of coffee beans")
# water = int( input( "Write how many ml of water the coffee machine has:\n" ) )
# milk = int( input( "Write how many ml of milk the coffee machine has:\n" ) )
# beans = int( input( "Write how many grams of coffee beans the coffee machine has:\n" ) )
# cups = int( input( "Write how many cups of coffee you will need:\n" ) )
# w = 200
# m = 50
# b = 15
# wc = water // w  # wc=no of cups can be made using "water" amount of water
# mc = milk // m  # mc = no of cups can be made using "milk" amount of milk
# bc = beans // b # bc = no of cups can be made using "beans" amount of coffe beans
# cups_can_be_really_made = min(wc,mc,bc)
# if cups_can_be_really_made == cups:
#     print("Yes, I can make that amount of coffee")
# elif cups_can_be_really_made > cups:
#     N = cups_can_be_really_made - cups
#     print("Yes, I can make that amount of coffee (and even",N,"more than that)")
# else:
#     print("No, I can make only",cups_can_be_really_made,"cups of coffee")
class CoffeeMachine:  # coffeMachine class where all functions can be handled
    def __init__(self):
        self.water = 400  # This was told to be the available amount by the jetbrains
        self.milk = 540
        self.beans = 120
        self.dis_cups = 9
        self.money = 550

    def display(self):  # This method shows the current condition of the coffee machine
        global water
        global milk
        global beans
        global dis_cups
        global money
        print( "The coffee machine has:" )
        print( self.water, "of water" )
        print( self.milk, " of milk" )
        print( self.beans, "of coffee beans" )
        print( self.dis_cups, "of disposable cups" )
        print( "$", self.money, " of money\n", sep="" )
        return

    def buy(self, no):  # The "no" variable is the choice number which is given by the user in the while loop
        global water
        global milk
        global beans
        global dis_cups
        global money
        if no == 1:
            if self.water < 250:
                print( "Sorry, not enough water!" )
                return
            elif self.beans < 16:
                print( "Sorry, not enough coffee beans!" )
                return
            else:
                print( "I have enough resources, making you a coffee!" )
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.dis_cups -= 1
                return
        elif no == 2:
            if self.water < 350:
                print( "Sorry, not enough water!" )
                return
            elif self.beans < 20:
                print( "Sorry, not enough coffee beans!" )
                return
            elif self.milk < 75:
                print( "Sorry, not enough milk!" )
                return
            else:
                print( "I have enough resources, making you a coffee!" )
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.dis_cups -= 1
                return
        elif no == 3:
            if self.water < 200:
                print( "Sorry, not enough water!" )
                return
            elif self.beans < 12:
                print( "Sorry, not enough coffee beans!" )
                return
            elif self.milk < 100:
                print( "Sorry, not enough milk!" )
                return
            else:
                print( "I have enough resources, making you a coffee!" )
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.dis_cups -= 1
                return
        else:
            return

    def fill(self):
        global water
        global milk
        global beans
        global dis_cups
        global money
        w = int( input( "Write how many ml of water do you want to add:\n" ) )
        m = int( input( "Write how many ml of milk do you want to add:\n" ) )
        b = int( input( "Write how many grams of coffee beans do you want to add:\n" ) )
        c = int( input( "Write how many disposable cups of coffee do you want to add:\n" ) )
        self.water += w
        self.milk += m
        self.beans += b
        self.dis_cups += c
        return

    def take(self):
        global water
        global milk
        global beans
        global dis_cups
        global money
        print( "I gave you $", self.money, sep="" )
        self.money = 0
        return


# main part of the code.In here there is a loop which is used to take choices from the user
x = CoffeeMachine()
action = input( "Write action(buy, fill, take, remaining, exit):\n" )
while action != "exit":
    if action == "buy":
        no = input( "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n" )
        if no == "back":
            action = input( "Write action(buy, fill, take):\n" )
            continue
        x.buy( int( no ) )
    elif action == "fill":
        x.fill()
    elif action == "take":
        x.take()
    elif action == "remaining":
        x.display()
    action = input( "Write action(buy, fill, take, remaining, exit):\n" )
