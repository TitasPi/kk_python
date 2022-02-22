# If
a = 10
b = input('B: ')
b = int(b)

if a > b:
  print('A > B')
else:
  print('A < B')

if a > b:
  print('A > B')
elif a == b:
  print('A == B')
else:
  print('A < B')

# If with bools
c = True

if c:
  print('C is True')

# If negation
d = False

if not d:
  print('D is not True')

# If and

a1 = 6
a2 = True

if a1 < 5 and a2:
  print('Trigger')

# > < == != >= <=

b1 = 5
b2 = 10

if b1 > 10 or b2 > 5:
  print('Trigger2')

# ----------------------------------------

# While loop
i = 0

while i < 10:
  print(i)
  i += 1 # i = i + 1

# For loop

grades = [10, 8, 7, 5, 10]

sum = 0

for grade in grades:
  sum += grade
  print(grade)

print(sum)

# For loop with range

for i in range(3):
  print(i)

# Custom min value
for i in range(1, 3):
  print(i)

# Custom step
for i in range(1, 10, 2):
  print(i)

# Reverse
for i in range(10, 0, -1):
  print(i)

# List

list = [10, 8, 7, 5, 10]

list = ['Abrikosas', 'taskas', 'serveriai.lt']

for element in list:
  print(element)

print(list[0])

# Dict

obj = {
  'name': 'Titas',
  'age': 20,
  'friends': ['none', None, 2]
}

print(obj['friends'])





