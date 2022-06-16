"""Main module used to solve wordle completely"""

from matplotlib.style import available
import solver
import web_scraper
from voice import speak, expression, greet

def express(result):
    result_sum = sum(result)
    if result_sum < 2:
        expression('bad')
    elif result_sum < 5:
        expression('good')
    else:
        expression('excellent')

web_scraper.set_up()
results = web_scraper.get_latest_results()
guess = solver.CurrentGuess('crate', results)
word = guess.new_guess
express(results)
speak(f'Now I know that there are still {len(guess.available_words)} options')
speak(f'Lets be creative and try {word}')
for i in range(5):
    web_scraper.make_move(word)
    results = web_scraper.get_latest_results()
    express(results)
    if sum(results) == 5 * 2:
        break

    guess = solver.CurrentGuess(word, results)
    word = guess.new_guess
    if len(guess.available_words) == 1:
       speak(f'There is only one possible solution, {word}')
    else:
        speak(f'There are {len(guess.available_words)} possible options')
        speak(f'Lets try {word}')
