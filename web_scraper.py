"""Module to scrap the wordle site."""

import webbrowser
import time
import pyautogui
import numpy as np

WORDLE_SITE = 'https://www.nytimes.com/games/wordle/index.html'
close_click = (1215, 372)
grey = (120, 124, 126)
orange = (198, 189, 78)
green = (79, 183, 96)
white = (255, 255, 255)
y_pixels = (345, 415, 484, 548, 617, 684) # top to bottom
x_pixels = (872, 942, 1011, 1075, 1137) #left to right

colors = {
    120: 0,
    198: 1,
    79: 2
}

def set_up():
    """Open the browser and play the first move."""
    webbrowser.open(WORDLE_SITE, new=2) # open the browser to the wordle game site
    time.sleep(2)

    pyautogui.moveTo(close_click[0], close_click[1], duration=0.3)
    pyautogui.click()
    time.sleep(0.5)
    make_first_move()

def make_move(word):
    """Enter a given word."""
    pyautogui.typewrite(word + '\n', interval = 0.25)
    time.sleep(3)

def make_first_move():
    """Play 'crate' the very first move."""
    make_move('crate')

def get_y_pixel():
    """Get the y pixel value of the last move."""
    time.sleep(3)
    red_color = 255
    x_pixel = x_pixels[0]
    for i, y_pixel in enumerate(y_pixels):
        pix = pyautogui.pixel(x_pixel, y_pixel)
        #pyautogui.moveTo(x_pixel, y_pixel, duration = 0.3)
        #print(pix)
        red_color = pix.red
        if red_color == 255:
            return y_pixels[i-1]
    return None


def get_results(y_pixel):
    """Take a y_pixel and convert the colors into results of that move."""
    last_results = []
    for x_pixel in x_pixels:
        pix = pyautogui.pixel(x_pixel, y_pixel)
        #pyautogui.moveTo(x_pixel, y_pixel, duration=0.3)
        red_color = pix.red
        last_results.append(colors[red_color])
    return np.array(last_results)

def get_latest_results():
    """Get the results of the last move."""
    latest_y_pixel = get_y_pixel()
    #print(latest_y_pixel)
    return get_results(latest_y_pixel)

if __name__ == '__main__':
    set_up()
    get_latest_results()
