# This Script will implement our knowledge on
# conditions and different datatypes

print("This is IT Organization has various skills sets.")
print("Fins out you match")

print("Enter Capilalised Value:")

Devops = ["Jenkins", "Ansible", "Bash", "Python", "Puppet", "Dockers", "Kubernetes","Terraform"]
Development = ("Nodejs", "Angularjs", "Java", ".net", "Python")
contrctempl = {"Name" : "Ali", "Skills" : "Blockchain", "Code": 1439}
contrctemp2 = {"Name" : "Mehmood", "Skills" : "AI", "Code": 1695}

usr_skill = input("Enter Your desired skill: ") # this will take input from user
# print(usrskill)

# Check in the database if we have this skill
if usr_skill in Devops:
    print(f"We have {usr_skill} in Devops team")
elif(usr_skill in Development) : 
    print(f"We have {usr_skill} in Development team") 
elif(usr_skill in contrctempl.values()) or (usr_skill in contrctemp2.values()) : 
    print(f"We have Contract Employee wit {usr_skill} skills")
else:
    print("Skill not found")
    print("Please check if you have entered value in capitalize or check the spelling")
