import os
from rich.console import Console
from rich.prompt import Prompt
import shutil
import sys

while True:
    os.system('clear')
    Console.print('\n1. Help\n2. Strategy\n3. Engage AI\n4. Historical Trends\n5. Sandbox\n6. Set It Loose\n7. Exit')
    choice = Prompt.ask('Choose a task (Enter the number)', choices=["1", "2", "3", "4", "5", "6"], default='6')

    # def prompt_choice(message, choices, default=None):
    # while True:
    #     choice = Prompt.ask(message, choices=choices, default=default)
    #     if choice in choices:
    #         return choice
    #     Console.print("Invalid choice. Please try again.")

    if choice == '1':
        help = Prompt.ask('Would you like Help?: ', choices=['Yes', 'No'], default='No')
        if help == 'Yes':
            Console.print('This will offer an overiew of the program')
        elif help == 'No':
            Console.print('This will not offer an overview of the program')

    elif choice == '2':
        strategy = Prompt.ask('Which trading strategy would you like to use? ', choices=['Dollar Cost Averaging', 'Buy the Dip', 'Buy the Low', 'Buy the Dip and Low', 'Buy the Dip, High, and Low'], default='Dollar Cost Averaging')
        if strategy == 'Dollar Cost Averaging':
            Console.print('This strategy will buy a fixed amount of crypto at a fixed interval')
        elif strategy == 'Buy the Dip':
            Console.print('This strategy will buy crypto when the price dips below a certain threshold')
            dip = Prompt.ask('What is the threshold? ', default='0.00')
            Console.print('The threshold is: ', dip)
        elif strategy == 'Buy the Low':
            Console.print('This strategy will buy crypto when the price is lower than the previous price')
            low = Prompt.ask('What is the threshold? ', default='0.00')
            Console.print('The threshold is: ', low)
        elif strategy == 'Buy the Dip and Low':
            Console.print('This strategy will buy crypto when the price dips below a certain threshold and is lower than the previous price')
            dip = Prompt.ask('What is the threshold? ', default='0.00')
            Console.print('The threshold is: ', dip)
            low = Prompt.ask('What is the threshold? ', default='0.00')
            Console.print('The threshold is: ', low)
        elif strategy == 'Buy the Dip, High, and Low':
            
            
        

      elif choice == '3':
          engage_ai = Prompt.ask('Would you like to engage the AI?: ', choices=['Yes', 'No'], default='No')

      elif choice == '4':
          warning()

      elif choice == '5':
          count_file_types()

      elif choice == '6':
          do_exit('Thank you for using the menu')

      else:
          console.print('Invalid choice. Please try again.')