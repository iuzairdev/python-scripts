'''
# Break Statement
for i in "Devops":
    print(i)
    if i == "o":
        print("data found")
        break
print("Loop Finished!")
'''
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

'''
# Continue Statement
for i in "Devops":
    if i == "o":
        print("data found")
        continue
    print(f"Value of i is {i}")

print("Loop Finished!")
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
import random
Vaccines = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZaneca"]

random.shuffle(Vaccines)
print(Vaccines)

Lucky = random.choice(Vaccines)
print(Lucky)

for vac in Vaccines:
    print(f"************Testing Vaccines {vac}")
    if vac == Lucky:
        print("#######################")
        print(f"{Lucky} Vaccine, Test Successful")        
        print("#######################")
        break
    print("#######################")
    print("Test Failed")        
    print("#######################")
    print()


