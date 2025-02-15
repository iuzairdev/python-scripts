# Now will call this module in another class which i named it 13.1-caller
import random

def vac_feedback(vac, efficacy):
    print(f"{vac} Vaccine is having {efficacy} % efficacy.")
    if(efficacy > 50) and (efficacy <= 75):
        print("Seems not so effective, Needs more trial.")
    elif(efficacy > 75) and (efficacy < 90):
        print("Can consider this vaccine.")
    elif efficacy >= 90:
        print("Sure, Will take the shot. ")
    else:
        print("Needs many more trials")
    

def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
    for item in args:
        print(f"You have ordered: {min_order}")
    print("Your food will be deliverd in 30 mins:")
    print("Enjoy the Party")

order_food("Salad")

def time_activity(*args, **kwargs):
  
  '''
  Input: Multiple values for minutes, keywords, key = value pair activity
  Output: Return sum of mminutes + random minute spect on a random activity
  '''
  print(args)
  print(kwargs)  
  min = sum(args) + random.randint(0,60) # it will pick any random number & will add it to numbers 
  print(min)
  choice = random.choice(list(kwargs.keys())) # will choose randomly any word from list
  print(choice)
  print(f"you have to spend {min} minutes for {kwargs[choice]}") # Proper Message

time_activity(10, 20, 30, hobby = "Reading", sport = "Football", fun = "drifting :)")
