
 these functions are helpful in
 data validation
 find your string
 combinig them


message = "most ot the people good enough"

message = "most ot the people good enough"
print(message)
print(message.capitalize()) #if you to capitalize the first word you can use both
Message = message.capitalize() #if you to capitalize the first word you can use both
print(Message)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxx

#dir() function

# dir function will give you all the available built-in methods for you
print(dir("")) 
print(dir([]))
print(dir(()))
print(dir({}))

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

print(message.upper())
print(message.islower()) 
print(message.isupper) # and many more. these are good for data validation 

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

print(message.find("good"))
print(message[18:23])
print(message.find("many")) # -1 because it will reach till if didn't find will give you -1 data not found

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

seq1 = ("192","168","40", "29")
print(".".join(seq1))
print("/".join(seq1)) 
print("-".join(seq1)) 

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# It's Time change the list how we can change it (mutable) we can't do this in tupple(Immutable)

mountains = ["K2", "Mount everest", "Himalaya","Alps"]
print(mountains) # now i would like to add/edit this 
mountains.append("Oregan mount")
print(mountains)
mountains.extend(["Mt rainer", "Satpuda"]) #Combinig it with other list
print(mountains)
mountains.insert(2, "Mt Abu") # 2 for index where i want to put my string 
print(mountains)
mountains.pop() #use to delete the last string from list
print(mountains)
mountains.pop(1) #use to delete specific string from list on this number
print(mountains) 

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

employee = {"Name":"Ali", "Skill": "Blockchain", "Code": "1025"}
print(employee)
print(employee.keys())
print(employee.values())
employee.clear()
print(employee)