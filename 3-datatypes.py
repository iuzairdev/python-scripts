# String's
str1 = "alpha"
str2 = 'beta'
str3 = '''gamma string'''
str4 = """delta string"""

# Numbers 
num1 = 125
flt1 = 1.2

# List/Array(Collection of multi datatype, enclosed in square brackets)
list1 = [str1, "Devops", 47, num1, 1.5]

# Printing the above List/Array
print(list1) 

# Another same like list which is called Tupple.
# But Tuple is immutable and list mutable
# it means you can edit list but not Tuple
 
tuple1 = (str1, "Devops", 47, num1, 1.5)

# Printing the above Tuple
print(tuple1) 

# The next is Dictionary
# Elements in the Dictionary are always in pairs
# like (Key:Value), curly brackets
dictionary1 = {"Name" : "Ali", "Weight":"62", "Exercise":["Pushups", "Chin-ups", "Set-ups"]}

# Printing the above Tuple
print(dictionary1)

# Lists and Their Types
print("Variables List is a:", type(list1))
print("Variables Tuple is a:", type(tuple1))
print("Variables Dictionary is a:", type(dictionary1))

# Booleans
x = True
y = False

print("x is a", type(x))
print("y is a", type(y))