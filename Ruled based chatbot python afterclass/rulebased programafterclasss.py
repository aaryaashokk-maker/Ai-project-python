import random
import pytz
import datetime
import colorama
from colorama import *
colorama.init(autoreset=True)
places = {
    "beach": ["mariana beach", "maldives", "bali", "bondi beach", "copacabana", "waikiki beach", "whitehaven beach", "siargao island", "navagio beach", "seven mile beach"],
    "mountaion":["mount everest","mount kilimanjaro","mount fuji","mount denali","mount elbrus","mount aconcagua","mount matterhorn","mount blanc","mount olympus","mount shasta","himalayas"],
    "city":["new york city","los angeles","chicago","houston","phoenix","philadelphia","san antonio","san diego","dallas","san jose","lusaka","tokyo","paris","london","berlin","madrid","rome","moscow","beijing","sydney", "cape town","rio de janeiro","dubai","singapore","hong kong","bangkok","istanbul","seoul","toronto","vancouver","melbourne","auckland","chennai","delhi","mumbai","kolkata","bengaluru","hyderabad","chennai","pune","ahmedabad","jaipur","lucknow","kanpur","nagpur","indore","bhopal","patna","ludhiana","agra","varanasi","amritsar","jodhpur","udaipur"]
}
jokes = [
    "Why did the tomato turn red? Because it saw the salad dressing!", "Why don't scientists trust atoms? Because they make up everything!", "What do you call a fake noodle? An impasta!",
     "Why did the scarecrow win an award? Because he was outstanding in his field!", "Why did the bicycle fall over? Because it was two-tired!", "What do you call a bear with no teeth? A gummy bear!", "Why did the chicken cross the playground? To get to the other slide!", "Why did the math book look sad? Because it had too many problems!", "What do you call a snowman with a six-pack? An abdominal snowman!", "Why did the coffee file a police report? It got mugged!"]
def recommend():
    in1re = input("Where do you want to go to a city, beach or mountain?")
    if in1re.lower() in places:
        global rec_chose
        rec_chose = random.choice(places[in1re.lower()])
        print(Fore.GREEN + f"Recommended destination: {rec_chose}")
    else:
        print(Fore.RED + "Invalid choice!")
    return rec_chose
def packing():
    global placea
    placea = input("Where are you going : ")
    global days
    days = int(input("How many days : "))
    print(Fore.BLUE + f"Packing for {days} in {placea}")
    return placea, days
while True:
    choice = input("What do you want to do?Destination, Paking, Joke, Time and Date , Time and Date of UTC or a destination? (Type 'exit' to quit): ")
    if choice.lower() == "destination":
        recommend()
    elif choice.lower() == "packing":
        packing()
    elif choice.lower() == "joke":
        joke = random.choice(jokes)
        print(joke)
    elif choice.lower() == "time and date":
        print(Fore.GREEN + f"Current time and date: {datetime.datetime.now()}")
    elif choice.lower() == "time and date of utc":
        utc_time = datetime.datetime.now(pytz.utc)
        print(Fore.GREEN + f"Current time and date in UTC: {utc_time}")
    elif choice.lower() == "exit":
        break
    else:
        print(Fore.RED + "Invalid choice!")
        exit()
    with open(r"C:\Users\Aarya\OneDrive\Documents\code\python\Ruled based chatbot python afterclass\travel_logchat.txt", "a") as file:
        file.write("------------------------------")
        file.write(f"\n\nTime : {datetime.datetime.now()}\n")
        file.write(f"Choice: {choice}\n")
        if choice.lower() == "destination":
           file.write(f"Destination is : {rec_chose}\n")
        elif choice.lower() == "packing":
            file.write(f"Packing for {days} in {placea}\n")
        elif choice.lower() == "joke":
            file.write(f"Joke: {joke}\n")
        elif choice.lower() == "time and date of utc":
            file.write(f"Current time and date in UTC: {utc_time}\n")
        elif choice.lower() == "exit":
            file.write("Exit\n")
        elif choice.lower() == "time and date":
            file.write(f"Current time and date: {datetime.datetime.now()}\n")
        else:
            file.write(f"Invalid choice: {choice}\n")
        pass