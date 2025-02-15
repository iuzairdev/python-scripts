# If you want to execute something repetitively so 
# for that we use loops 


# FOR LOOP
planet = "Earth"
for i in planet:
    print("Value of i is now, "+i)

print("Rest of the Code") #It will keep running till h like will start from E then a then r and so on.


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Now lets try to do it in Tupples 
Vaccines = ("Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZaneca")

for vac in Vaccines:
    print(f"{vac} provides immunization against covid19")

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# Now Array/List samething for the list  
Vaccines = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZaneca"]

for vac in Vaccines:
    print(f"{vac} provides immunization against covid19")



# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# It's Time to do it in WHILE LOOP
x = 0
while x <= 10:
    print("Value of x is:", x)
    print("Looping")
    x +=1

print("Rest of the code.")


# I want to do it slowly
import time
x = 2
while True:
    print("Value of x is:", x)
    print("Looping")
    x *=2
    time.sleep(1) # It will increase the value by 1 sec