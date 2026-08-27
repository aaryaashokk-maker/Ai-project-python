from textblob import TextBlob
import colorama
from colorama import Fore, Style
colorama.init()
ask1 = input("Enter your text : ")
a = TextBlob(ask1)
b  = a.sentiment.polarity
if b > 0:
    print(Fore.GREEN + f"Your sentence is positive with a polarity of {b}!")
elif b < 0 :
    print(Fore.RED + f"Your sentence is negative with the polarity of {b}")
else:
    print(Fore.BLUE + f"Your sentence is neutral with a polarity of {b}!")
