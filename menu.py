import os
import sys
# import requests
from rich.console import Console
from rich.prompt import Prompt


console = Console()

# Read the API key from gpt_api.txt file
with open('gpt_api.txt', 'r') as file:
    gpt_api = file.read().strip()

strategy = []

# Define the menu function
def menu():
    global user_input
    while True:
        console.clear()
        os.system('clear')
        console.print(
            "\n1. Help\n2. Strategy\n3. Engage AI\n4. Historical Trends\n5. Sandbox\n6. Set It Loose\n7. Exit",
            soft_wrap=False,
        )
        choice = Prompt.ask('Choose a task (Enter the number)', choices=["1", "2", "3", "4", "5", "6", "7"], default='6')
        console.print(user_input)

        if choice == '1':
            help_menu()

        elif choice == '2':
            # Add your code for choice 2 here
           choice2()

        elif choice == '3':
            # Add your code for choice 3 here
            pass

        elif choice == '4':
            # Add your code for choice 4 here
            pass

        elif choice == '5':
            # Add your code for choice 5 here
            pass

        elif choice == '6':
            # set_it_loose(btc_data, eth_data)
            pass

        elif choice == '7':
            console.print('Exiting...')
            break

        else:
            console.print('Invalid choice. Please try again.')

# Define the help menu function
def help_menu():
    console.clear()
    console.print('This will offer an overview of the program')
    console.print('Press Enter to go back to the main menu...')
    input()  # Wait for user to press Enter

def choice2():
    day_choice = Prompt.ask('Choose 30, 60, or 90 days (Enter the number)', day_choice=["1", "2", "3"], default='4')
    option_choice = Prompt.ask('Choose a strategy Conservative (C), Risky (R), Beginner (B) (Enter the number)', option_choice=["C", "R", "B"], default='4')
    

    call_gpttest(day_choice, option_choice)
    
    # if day_choice == '30':
    #     pass
    # elif day_choice == '60':
    #     pass
    # elif day_choice == '90':
    #     pass
    # elif day_choice == '4':
    #     exit

def call_gpttest(days, option):
      


      from modules.GPTtest30 import eth_data, btc_data
      console.print('Press Enter to go back to the main menu...')
      # console.print('choice 2')
      input()

menu()