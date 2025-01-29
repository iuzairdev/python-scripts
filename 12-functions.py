# # Defining Function

# def add(arg1, arg2):
#     total = arg1 + arg2
#     return total 

# out = add(2,3)
# print(out)

# def adder(arg1, arg2):
#     total = arg1 + arg2
#     print(total)  
    

# # adder(10,50)
# print(adder(10,30))

# # Another one 
# def summ(arg):
#     x=0
#     for i in arg:
#         x = x + i
#     return x
# out = summ([10,20,30])  
# print(out)  


# summ([10,20][30,45])

# # Default argument 
# # Approach 1
# def greetings(MSG = "Morning"):
#     print(f"Good {MSG}")
#     print("Welcome to the function")
# greetings()
# greetings("Evening")

# # Approach 2
# def greetings(MSG):
#     print(f"Good {MSG}")
#     print("Welcome to the function")
# greetings("Morning")

# # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# # Funtion that gives us feedback 
# def vac_feedback(vac, efficacy):
#     print(f"{vac} Vaccine is having {efficacy} % efficacy.")
#     if(efficacy > 50) and (efficacy <= 75):
#         print("Seems not so effective, Needs more trial.")
#     elif(efficacy > 75) and (efficacy < 90):
#         print("Can consider this vaccine.")
#     elif efficacy >= 90:
#         print("Sure, Will take the shot. ")
#     else:
#         print("Needs many more trials")
    
# # vac_feedback("Pfizer", 95)
# # vac_feedback("Unknown", 45) 
# # if you wrote it wrong it will not excute or you can mention as shown below
# vac_feedback(45,"Unknown") # Wrong Approach
# vac_feedback(efficacy=45,vac="Unknown")

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# VARIABLE LENGTH ARGUMENTS(Non keyword Argument)
# What if we want mention more than 3 functions
# def order_food(min_order):
#     print(f"You have ordered: {min_order}")
#     print("Your food will be deliverd in 30 mins:")
#     print("Enjoy the Party")

# order_food("Salad") # it needs one argument, what if we put more than 1

# # For putting orders more than 1 then we will add *args like this
# def multi_order_food(min_order, *args):
#     print(f"You have ordered: {min_order}")
#     for item in args:
#         print(f"You have ordered: {item}")
#     print("Your food will be deliverd in 30 mins:")
#     print("Enjoy the Party")

# multi_order_food("Salad", "Pizza", "Biryani", "Soup")

# # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# VARIABLE LENGTH ARGUMENTS *keywordargs(Keyword Arguments)
import random
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
