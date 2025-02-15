# Arithematic operators
x = 2
y = 7

total = x + y
print(total)

total = x - y
print(total)

total = x * y
print(total)

total = y / x
print(total)

total = y % x # modulus operator will give you the reminder value
print(total)

total = y**x # it means y power x y^x
print(total)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Comparison Operator
a = 30
b = 60

out = a < b
print (out)

out = a > b
print (out)

out = a == b
print (out)

out = a != b
print (out)

out = a <= b
print (out)

out = a >= b
print (out)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Assignment Operators

c = 0
d = 1

c += d # c = c+d
print(c)

c -= d # c = c-d
print(c)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Logical Operators

# AND
# OR

a = 40
b = 60

x = 2
y = 3

out = (a < b) or (x > y) # If any of them is false value will be false
print(out)

out = (a < b) and (x > y) # If any of them is true value will be true
print(out)

out = not(x > y) # If it is false it will return true. true will false 
print(out)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Membership Operator
tuple1 = ("IOT", "Devops", 47, 12, 1.5)
ans = "Devops" in tuple1 # help you to find something from the list
print(ans)

ans = "Devops" not in tuple1
print(ans)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Identity Operators
a = 12
b = 12

result = a is b
print(result)

result = a is not b
print(result)


