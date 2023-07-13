import os
import sys
from rich.console import Console
from rich.prompt import Prompt
from modules.GPTtest30 import get_option
from modules.GPTtest60 import get_option
from modules.GPTtest90 import get_option
console = Console()
# Read the API key from gpt_api.txt file
with open('gpt_api.txt', 'r') as file:
    gpt_api = file.read().strip()


# Define the menu function
def menu():
    while True:
        console.clear()
        os.system('clear')
        console.print(
            "\n1. Help\n2. Strategy\n3. Engage AI\n4. Historical Trends\n5. Sandbox\n6. Set It Loose\n7. Exit",
            soft_wrap=False,
        )
        choice = Prompt.ask('Choose a task (Enter the number)', choices=["1", "2", "3", "4", "5", "6", "7"], default='6')

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
    day_choice = Prompt.ask('Choose 30, 60, or 90 days (Enter the number)', choices=["30", "60", "90"], default='30')
    option_choice = Prompt.ask('Choose a strategy Conservative (C), Risky (R), Beginner (B)', choices=["Conservative", "Risky", "Beginner", "C", "R", "B"], default='4')
    option_choice_validated=None
    if option_choice.lower() == "Conservative" or option_choice.lower() == "C":
        option_choice_validated = "conservative"

    elif option_choice.lower() == "Risky".lower() or option_choice.lower() == "R":
        option_choice_validated = "risky"

    elif option_choice.lower() == "Beginner".lower() or option_choice.lower() == "B":
        option_choice_validated = "beginner"
    else:
        exit    

    console.print("Generating response...")
    
    if day_choice ==   '30':
        get_option(option_choice_validated)
        end_programm()
    elif day_choice == '60':
        get_option(option_choice_validated)
        end_programm()
    elif day_choice == '90':
        get_option(option_choice_validated)
        end_programm()
    else:
        exit
    
def end_programm():
    input(console.print('Press "enter" to [red]exit[/red]'))
    exit
        
menu()