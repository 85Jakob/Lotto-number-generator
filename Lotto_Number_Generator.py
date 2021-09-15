# Program 7PE2 
# Description: 
# 	Lottery Number Generator
#       Design a program that generates a seven-digit lottery number.
#       The program should generate seven random numbers, each in the range of 0 through 9, and assign each number to a list element.
#       Pass this list to a function that displays the contents of the list.
#
# Author: Jacob Doney, Alexandria Chung, Connor Evans
# Date: <today’s date>
# Revised: 
# 	<revision date> 

# import library modules here
import random

# Declare global constants (name in ALL_CAPS)

def main():

    # Declare Variable types (EVERY variable used in this main program)
    lottery_numbers = []

    answer = input('Generate lotto numbers?(Y or N) ')
    while answer.lower() == 'y':

        # "grow" a list using the append() method
        for number in range(7):
            num = random.randint(0, 69)
            lottery_numbers.append(num)

        display(lottery_numbers)

        lottery_numbers=[]
        answer = input('\nDo you want new numbers?(Y or N) ')
        

# End Program
# Function display()
# Description:
#   displays the contents of the list.
# Calls:
#   none
# Parameters:
#   lottery_numbers
# Returns:
#   none

def display(lottery_numbers):

    # Declare Local Variable types (NOT parameters)
    for number in lottery_numbers:
        print(number, end=' ')
        
    # Return the return variable, if any

#} Function display()

main()
