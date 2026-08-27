def con():
  favhob =input(f"{name} what is your favorite hobby : ")
  print(f"Nice {name} thats a great hobby ! {favhob}")
  print("Do you want to continue talking ? Yes or No : ")
  askcon2 = input()
  asckcon2 = askcon2.lower()
  if askcon2 == "yes":
    print("What is your favorite activity : ")
    favact = input()
    print(f"Nice you like {favact} {name} !")
  else:
    print("Nice talking to you.")
    exit()
print("Welcome, whats your name : ")
name = input()
print(f"{name} how are you feeling today ?")
feeling = input("How are you feeling Good or Bad : ")
feeling = feeling.lower()
if feeling == "good":
  print(f"I am happy to hear that {name} !")
  print("Do you want to continue talking ? Yes or No : ")
  goodwanttotalk = input()
  goodwanttotalk = goodwanttotalk.lower()
  if goodwanttotalk == "yes":
    con()
  else:
    print("Nice talking to you.")
    exit()
elif feeling == "bad":
  print(f"Sorry to hear that {name} >:(")
  print("Nice talking to you hope you get better.")
  print("Do you want to continue talking ? Yes or No : ")
  goodwanttotalk = input()
  goodwanttotalk = goodwanttotalk.lower()
  if goodwanttotalk == "yes":
    con()
  else:
    print("Nice talking to you.")
    exit()
else:
  print("That is not an input ERROR!")
  exit()
