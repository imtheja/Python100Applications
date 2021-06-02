#/c/Users/imthe/PycharmProjects/RealWorldProjects
import random

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

#Day 4: Rock Paper Scissors game
#Ansi's for rock paper scissors were removed.

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



#Day5: Password Generator

listLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
listNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
listSymbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
intNumOfletters= int(input("How many letters would you like in your password?\n"))
intNumOfsymbols = int(input(f"How many symbols would you like?\n"))
intNumOfnumbers = int(input(f"How many numbers would you like?\n"))
strPassword = ""

for i in range(intNumOfnumbers):
    intRandomIndex = random.randint(0, 9)
    strPassword += str(listNumbers[intRandomIndex])

for i in range(intNumOfletters):
    intRandomIndex = random.randint(0, 52)
    strPassword += str(listLetters[intRandomIndex])

for i in range(intNumOfsymbols):
    intRandomIndex = random.randint(0, 8)
    strPassword += str(listSymbols[intRandomIndex])

listPassword = []
listPassword[:0] = strPassword
random.shuffle(listPassword)
strUPassword = ''.join(listPassword)
print(f"Your password is: {strUPassword}")


#Day6: Escaping the maze using while loops
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        

#Day7: HangMan-Guess a word game
import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    # Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])


#Day8: Cipher Decode or Encode Logic
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
#from art import logo
#print(logo)

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    # Hint: Think about how you can use the modulus (%).
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")


#Day9: Grading Program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
dictGrades = {}


# TODO-2: Write your code below to add the grades to student_grades.
for key in student_scores:
    if 91 <= student_scores[key] <= 100:
        dictGrades[key] = "Outstanding"
    elif 81 <= student_scores[key] <= 90:
        dictGrades[key] = "Exceeds Expectation"
    elif 71 <= student_scores[key] <= 80:
        dictGrades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        dictGrades[key] = "Fail"

# 🚨 Don't change the code below 👇
print(dictGrades)


#Main Exercise: Secret Bidding
from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()


#Day10: Calculator Application
from replit import clear
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()


#Day11: Capstone Project Black Jack
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from replit import clear
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()


#Day12: Guess-The-Number Game
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

'''
#Day13: CoffeeMachine

class CoffeeMaker:
  """Models the machine that makes the coffee"""

  def __init__(self):
    self.resources = {
      "water": 300,
      "milk": 200,
      "coffee": 100,
    }

  def report(self):
    """Prints a report of all resources."""
    print(f"Water: {self.resources['water']}ml")
    print(f"Milk: {self.resources['milk']}ml")
    print(f"Coffee: {self.resources['coffee']}g")

  def is_resource_sufficient(self, drink):
    """Returns True when order can be made, False if ingredients are insufficient."""
    can_make = True
    for item in drink.ingredients:
      if drink.ingredients[item] > self.resources[item]:
        print(f"Sorry there is not enough {item}.")
        can_make = False
    return can_make

  def make_coffee(self, order):
    """Deducts the required ingredients from the resources."""
    for item in order.ingredients:
      self.resources[item] -= order.ingredients[item]
    print(f"Here is your {order.name} ☕️. Enjoy!")


class MenuItem:
  """Models each Menu Item."""

  def __init__(self, name, water, milk, coffee, cost):
    self.name = name
    self.cost = cost
    self.ingredients = {
      "water": water,
      "milk": milk,
      "coffee": coffee
    }


class Menu:
  """Models the Menu with drinks."""

  def __init__(self):
    self.menu = [
      MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
      MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
      MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
    ]

  def get_items(self):
    """Returns all the names of the available menu items"""
    options = ""
    for item in self.menu:
      options += f"{item.name}/"
    return options

  def find_drink(self, order_name):
    """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
    for item in self.menu:
      if item.name == order_name:
        return item
    print("Sorry that item is not available.")


class MoneyMachine:
  CURRENCY = "$"

  COIN_VALUES = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
  }

  def __init__(self):
    self.profit = 0
    self.money_received = 0

  def report(self):
    """Prints the current profit"""
    print(f"Money: {self.CURRENCY}{self.profit}")

  def process_coins(self):
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    for coin in self.COIN_VALUES:
      self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
    return self.money_received

  def make_payment(self, cost):
    """Returns True when payment is accepted, or False if insufficient."""
    self.process_coins()
    if self.money_received >= cost:
      change = round(self.money_received - cost, 2)
      print(f"Here is {self.CURRENCY}{change} in change.")
      self.profit += cost
      self.money_received = 0
      return True
    else:
      print("Sorry that's not enough money. Money refunded.")
      self.money_received = 0
      return False


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
  options = menu.get_items()
  choice = input(f"What would you like? ({options}): ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
    is_payment_successful = money_machine.make_payment(drink.cost)
    if is_enough_ingredients and is_payment_successful:
      coffee_maker.make_coffee(drink)
