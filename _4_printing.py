name = "sars_cov_2"
disease = "covid19"

# This is simple print statement
print("The name of virus is ", name)

# This print statements works everywhere. if you want to add
# something in middle start or at the start of line
# you can use curly braces like i've mentioned in new print
print("The name of virus is {}".format(name))

# As you can see...
print("{} is the name of virus.".format(name))

# Now If you have multiple variables 
# So Lets See
print("The name of the virus is {} and it causes {}".format(name, disease))

# You can use the 2nd way too but this only work in python3 or higher
print(f"The name of the virus is {name} and it causes {disease}")

# One more way if you need it which is called concatination
print("The name of the virus is" + " "+ name)