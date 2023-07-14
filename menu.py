import os
import sys
from rich.console import Console
from rich.prompt import Prompt
import importlib

console = Console()

def menu():
    while True:
        console.clear()
        os.system('clear')
        console.print("Options are [bold green]ACTIVE[/bold green]""\nOptions that are work in [bold medium_violet_red]PROGRESS[/bold medium_violet_red]"
            "\n1. [bold green]Help[/bold green]\n2. [bold green]AI Analysis[/bold green]\n3. [bold medium_violet_red]Live trading[/bold medium_violet_red] \n4. [bold green]About us[/bold green] \n5. [bold red]Exit[/bold red]",
            soft_wrap=False,
        )
        choice = Prompt.ask('Choose a task (Enter the number)', choices=["1", "2", "3", '4', '5'], default='5')

        if choice == '1':
            help_menu()

        elif choice == '2':
            choice2()

        elif choice == '3':
            # choice3()
            pass

        elif choice == '4':
            # choice4()
            pass

        elif choice == '5':
            console.print('Exiting...')
            break

        else:
            console.print('Invalid choice. Please try again.')

def help_menu():
    console.clear()
    console.print('This will offer an overview of the program')
    console.print('Press Enter to go back to the main menu...')
    input()  

def choice2():
    day_choice = Prompt.ask('Choose [bold purple]30, 60, or 90 days[/bold purple] (Enter the number)', choices=["30", "60", "90"], default='30')
    option_choice = Prompt.ask('Choose a strategy Conservative (C), Risky (R), Beginner (B)', choices=["Conservative", "Risky", "Beginner", "C", "R", "B"], default='4')
    
    if option_choice.lower() == "Conservative" or option_choice.lower() == "c":
        option_choice_validated = "conservative"

    elif option_choice.lower() == "Risky".lower() or option_choice.lower() == "r":
        option_choice_validated = "risky"

    elif option_choice.lower() == "Beginner".lower() or option_choice.lower() == "b":
        option_choice_validated = "beginner"
    else:
        exit    

    console.print("Generating response...")

    user_input(day_choice, option_choice_validated)
    
def user_input(days, option):
    if days == "30" or days == "60" or days == "90":
        module_name = f"modules.gpt_controller"
        module = importlib.import_module(module_name)
        get_option = getattr(module, "get_option")
        get_option(days, option)
        end_programm()
    else:
        exit
    
def end_programm():
    input(console.print('Press "enter" to [red]exit[/red]'))
    exit

if __name__ == '__main__':        
    menu()