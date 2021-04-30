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
'''