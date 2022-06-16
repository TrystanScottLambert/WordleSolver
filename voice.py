"""Voice module to use on the wordle solver"""
import os 
from gtts import gTTS
import random

PHRASES = {
    'bad': ['Oh no', 'Dammit', 'Shucks', 'Lord have mercy', 'You are kidding me'],
    'good': ['not to bad', 'here comes the money', 'hey, thats pretty good'],
    'excellent': ['oh yeah', 'I am the greatest!', 'Thats how you play wordle', 'Excellent guess', 'amazing']
}

SALUTATIONS = [
    'I was literaly made for this',
    'wordle bot is my name and wordle is my game',
    'I am the best there has ever been',
    'Oh yeah boy, this is is where the fun begins',
    'Three or less, what is the bet?',
    'Let us do this quickly, I have got things to do and people to see', 
    'ahh wordle, my old nemesis, we meet again.', 
    'Trystan is too busy to do this so I will do it for him',
]

def speak(text: str) -> None:
    text_object = gTTS(text = text, lang = 'en', slow = False)
    text_object.save('temp.mp3')
    os.system('mpg321 temp.mp3')
    os.remove('temp.mp3')

def expression(expression_type: str) -> None:
    speak(random.choice(PHRASES[expression_type]))

def greet() -> None:
    speak(random.choice(SALUTATIONS))


if __name__ == '__main__':
    speak('hello everyone')
    expression('bad')
