# Slicing is getting a Slice from DATA
# OR
# Subdata from Your DATA

# IF you want to fetch data from string/List/tuple
# that will be called slicing

# First lets talk about slicing
planet1 = "Closest to Sun"
print(planet1)

'''
# Now i want to access o from the Closet 
# for that i will use the index which start from 0
# like the "o" on 2nd position [0,1,2]
print(planet1[2])

#For "t" from planet we use 6 and so on...
print(planet1[6])

# we can use negative integars too like
print(planet1[-1])
# negative integers represent the string from right side likewise

# We can give a range too like 1-5 
print(planet1[1:5])

# if I didn't used the number it will be from 0:-1
print([planet1[:]])

# also if i can mention :7 which represets from 0:7 and also can use 11:
print(planet1[:7])
print(planet1[11:])

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# Above all was about STRING we can use Slicing in Tuple too, like...
devops = ("Linux", "vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")
print(devops[0])
print(devops[1])
print(devops[-1]) # we have linux 0th position, vagrant on 1 and so on... and -1 is from the last of tuple

# we can also use range in this too
print(devops[2:5])

# we can go more in-depth too
print(devops[2:4][0])

# Now i want to go further more in-depth and i need onlly Scripting
print(devops[2:5][0][5:11]) # The output of the last will be Script because of Script starts from 5th position 

# we can go more deeper like
print(devops[2:5][0][5:11][-1]) # from Script we only get 't' because we used -1

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Now its Time to do these things in List the thing is same in List we only change the brackets
devops = ["Linux", "vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]
print(devops[0])
print(devops[1])
print(devops[-1]) # we have linux 0th position, vagrant on 1 and so on... and -1 is from the last of tuple

# we can also use range in this too
print(devops[2:5])

# we can go more in-depth too
print(devops[2:4][0])

# Now i want to go further more in-depth and i need onlly Scripting
print(devops[2:5][0][5:11]) # The output of the last will be Script because of Script starts from 5th position 

# we can go more deeper like
print(devops[2:5][0][5:11][-1]) # from Script we only get 't' because we used -1
'''

# Now It's Time to do things done for dictionary
Skills = {"devops": ("AWS","Jenkins", "Python", "Ansible"), "development":["Java", "Python", "C++"]}
print(Skills["devops"]) # In Dictionary we mentions the key name like we have 2 keys here  
print(Skills["development"])    # devops is Tuple and development is List
print(Skills["devops"][-1])
print(Skills["development"][2])
print(Skills["devops"][-1][:3]) #Range