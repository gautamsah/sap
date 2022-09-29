# swap using Extra variable

x = 100
y = 200
temp = x  # storing x value to temp ,so that we don't loose x
x = y
y = temp

print(x)
print(y)



# swap using Comma Assignment

x = 100
y = 200

x, y = y, x

print(x)
print(y)


# using comma to assign multi values to multi variables

x, y, z = 100, "geeks", 10.5
print(x)
print(y)
print(z)

# writing expression

x, y = x - 5, y + "for"

print(x)
print(y)