from math import *  # Importing math functions (not used in the code currently)
from random import *  # Importing random functions
from random import randrange  # Importing specific function for random number generation

print('24 Game ')  # Print the game title

# Generate four random numbers between 1 and 10
a = randrange(1, 11)
b = randrange(1, 11)
c = randrange(1, 11)
d = randrange(1, 11)

# Create a list of the generated numbers
numbers_list = [a, b, c, d]
print(numbers_list)  # Display the list of numbers to the player

# Function to get a valid number input from the user
def numbers(x):
    while x not in numbers_list:  # Keep asking until the input number is in the list
        x = int(input("Angka: "))  # Prompt the user for a number
    return x  # Return the valid number

# Function to apply the selected operator on two numbers
def operators(x, y):
    ulangoperator = True  # Flag to control the loop
    while ulangoperator:  # Continue until a valid operator is selected
        operator_choice = str(input('Harus diapain biar jadi 24? (+, -, *, /, **): '))  # Ask for operator
        if operator_choice == "+":  # Check for addition
            hasil1 = x + y
            ulangoperator = False  # Exit loop if valid operator is found
        elif operator_choice == "-":  # Check for subtraction
            hasil1 = x - y
            ulangoperator = False
        elif operator_choice == "/":  # Check for division
            hasil1 = x / y
            ulangoperator = False
        elif operator_choice == "*":  # Check for multiplication
            hasil1 = x * y
            ulangoperator = False
        elif operator_choice == "**":  # Check for exponentiation (not typically used in 24 game)
            hasil1 = x ** y
            ulangoperator = False
        else:
            print("Coba lihat lagi operatornya!")  # Prompt for valid operator if input is invalid

    hasil1 = int(hasil1)  # Convert the result to integer (this will truncate any decimal)
    return [hasil1, operator_choice]  # Return the result and the operator used

# Main game loop
while True:
    angka1 = None
    angka2 = None

    # Get first pair of numbers from the user
    i1 = numbers(angka1)
    i2 = numbers(angka2)
    op1 = operators(i1, i2)  # Apply the operator on the two numbers
    numbers_list.append(op1[0])  # Append the result to the list of numbers
    numbers_list.remove(i1)  # Remove the first selected number
    numbers_list.remove(i2)  # Remove the second selected number
    operator = op1[1]  # Store the last operator used

    # Print the result of the first operation
    print(i1, operator, i2, "=", op1[0])
    print(numbers_list)  # Display current numbers

    # Repeat for the second pair of numbers
    angka3 = None
    angka4 = None
    i3 = numbers(angka3)
    i4 = numbers(angka4)
    op2 = operators(i3, i4)
    numbers_list.append(op2[0])
    numbers_list.remove(i4)
    numbers_list.remove(i3)
    operator = op2[1]

    # Print the result of the second operation
    print(i3, operator, i4, "=", op2[0])
    print(numbers_list)

    # Repeat for the third pair of numbers
    angka5 = None
    angka6 = None
    i5 = numbers(angka5)
    i6 = numbers(angka6)
    op3 = operators(i5, i6)
    numbers_list.append(op3[0])
    numbers_list.remove(i6)
    numbers_list.remove(i5)
    operator = op3[1]

    # Print the result of the third operation
    print(i5, operator, i6, "=", op3[0])
    print(numbers_list)

    # Check if the final result is 24
    if op3[0] == 24:  # Check if the last result equals 24
        print("you win!")  # Player wins
    else:
        print("wrong!")  # Player did not reach 24

    # Ask if the player wants to play again
    playAgain = None
    while playAgain not in ["Y", "N"]:
        playAgain = input("Play again? Y/N ")  # Prompt for replay
        playAgain = playAgain.upper()  # Convert input to uppercase
    if playAgain != "Y":  # Exit if the player does not want to continue
        break





