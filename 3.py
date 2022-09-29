print(id(5))

a = 10

print('id of a',id(a))

b = a

print('id of b',id(b))

##################

# same value literals stored at same location

a=10
b=10
print(id(a))
print(id(b))

c= "geek"
d="geek"

print('id c',id(c))
print('id of d',id(d))








a = 10
b = 10
print(a is b)

c = a
print(c is b)

c = 20
print(c is b)
