'''
#Day1
print("Welcome to the Band Name Generator.")
strName = input("What's name of the city you grew up in ? \n")
strPetName = input("What's the name of your pet ? \n")
print("Your band name could be " + " " + strName + " " + strPetName)


#Day2 Mini Exercise: Determining how many days weeks and years left in once life.
#TakeAways: How to use f-string, datatype conversions, Arithmetic operations and order of preferences.
intAge = int(input("What's is your current age ? \n "))
intYearsRemaining = 120-intAge
intDaysRemaining=intYearsRemaining*365
intWeeksRemaining=intYearsRemaining*52
intMonthsRemaining=intYearsRemaining*12
print(f"You have {intDaysRemaining} days, {intWeeksRemaining} weeks and {intMonthsRemaining} months left in your life.")

#Main Exercise: Tip calculator
print("Welcome to the tip calculator. ")
floatTotalBill = float(input("What was the total bill ? \n"))
intTipPercent = int(input("What percentage tip would you like to give? 10, 12, or 15? \n "))
intPeopleToShare = int(input("How many people to split the bill ? \n "))
floatEachPersonsShare = round((floatTotalBill + (floatTotalBill * intTipPercent/100))/intPeopleToShare, 2)
print(f"Each person should pay: {floatEachPersonsShare}")

#Day3 Mini Exercise: Love Calculator
#TakeAways:
print("Welcome to the Love Calculator!")
strHisName = input("What is his name ? \n ")
strHerName = input("What is her name ? \n ")
strCombinedName = strHisName + strHerName
strCombinedName = strCombinedName.lower()

intTCount = strCombinedName.count('t')
intRCount = strCombinedName.count('r')
intUCount = strCombinedName.count('u')
intECount = strCombinedName.count('e')

intTrueValue = (intTCount + intRCount + intUCount + intECount)

intLCount = strCombinedName.count('l')
intOCount = strCombinedName.count('o')
intVCount = strCombinedName.count('v')
intEECount = strCombinedName.count('e')

intLoveValue = (intLCount + intOCount + intVCount + intEECount)

intTotalSum = int(str(intTrueValue) + str(intLoveValue))

if intTotalSum < 10 or intTotalSum > 90:
    print(f"Your score is {intTotalSum}, you go together like coke and mentos")
elif 40 < intTotalSum < 50:
    print(f"Your score is {intTotalSum}, you are alright together.")
else:
    print(f"Your love score is {intTotalSum}")

#Main Exercise: Treasure Island
print("Welcome to Treasure Island.\n Your mission is to find the treasure.")
strInput = input("You're at a cross road. Where do you want to go ? type 'left' or 'right' ? ").lower()
print(strInput)
if strInput == "right":
    print("You fell into a hole. Game Over.")
else:
    strInput = input("You came to a lake. There is an island in the middle of the lake. Type 'wait' for a boat. Type "
                     "'swim' to swim across").lower()
    print(strInput)
    if strInput == 'swim':
        print("You got attacked by an angry trout. Game Over.")
    else:
        strInput = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, "
                         "and one blue. Which colour do you choose ? ")
        print(strInput)
        if strInput == 'red' or strInput == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
            print("You Win!")
'''
#Day 4: Rock Paper Scissors game
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock Paper Scissors Game!")
intUserChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors \n"))
listResult = [["Draw", "You Lose", "You Win"], ["You Win", "Draw", "You Lose"], ["You Lose", "You Win", "Draw"]]
if intUserChoice == 0:
    print("Your Choice: Rock", rock)
elif intUserChoice == 1:
    print("Your Choice: Paper", paper)
elif intUserChoice == 2:
    print("Your Choice: Scissors", scissors)
else:
    print("Wrong Input, Start over again. ")

if intUserChoice >=0 and intUserChoice < 3:
    intComputersChoice = random.randint(0, 2)
    if intComputersChoice == 0:
        print("Computer Choice: Rock", rock)
    elif intComputersChoice == 1:
        print("Computer Choice: Paper", paper)
    elif intComputersChoice == 2:
        print("Computer Choice: Scissors", scissors)

    print(listResult[intUserChoice][intComputersChoice])


