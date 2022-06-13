"""Main module used to solve wordle completely"""

import solver
import web_scraper

web_scraper.set_up()
results = web_scraper.get_latest_results()
guess = solver.CurrentGuess('crate', results)
word = guess.new_guess

for i in range(5):
    web_scraper.make_move(word)
    results = web_scraper.get_latest_results()
    guess = solver.CurrentGuess(word, results)
    word = guess.new_guess
