import pandas as pd
from rich.tree import Tree
from rich.console import Console
from rich.table import Table
from rich.progress import track
import rich.prompt

q = pd.read_csv('questions.csv')

print(q)



# range_str = range(1,7)
# while True:
#     answer = rich.prompt.IntPrompt.ask('Guess a number between 1 and 100: ', choices=range_str, show_choices=False)
#     if answer == secret_number:
#         print('Congratulations, you guessed the secret number!')
#         break
#     elif answer > secret_number:
#         print('A little high')
#     else:
#         print('a little low')
# play_again = rich.prompt.Confirm.ask('Play again?')

#spara mean i kategorier 