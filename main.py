import math

# Comments

'''
Multi-line
comments
'''

# Basic print
print('Hello world')
print(1+3)

# Variables & adv print
vardas = 'Titas'
amzius = 20

# Method #1
print('Mano vardas ' + vardas)
print('Man yra ' + str(amzius))

# Method #2
print(f'Mano vardas {vardas}')
print(f'Man yra {amzius}')

# Method #3 (not recommended)
print('Mano vardas {}'.format(vardas))
print('Man yra {}'.format(amzius))

# Method #4
print('Mano vardas', vardas)
print('Man yra', amzius)

# str() | int -> str
# int() | str -> int

amzius = '20'

# ~Conversion
print(int(amzius) + 2)

# String multiplication
print('-'*20)

# No new line
print('Helo word. ', end='')
print('It prints on same line')

# Mixing ' "
# print(f'Mano vardas yra {vardas} ir as noriu pasakyti {echo("")}')

# Math
print('2 + 2 = ', 2 + 2)
print('2 - 2 = ', 2 - 2)
print('2 * 2 = ', 2 * 2)
print('2 / 2 = ', 2 / 2)
print('3 ^ 2 = ', math.pow(3, 2))
print('5 % 3 = ', 5 % 3)

# Functions

# Simple function without args
def hello_world():
  print('Hello world from func')
hello_world()

# Simple function with args
def hello(name):
  print(f'Hello, {name}')
hello('Robertas')

def sum(a, b):
  print(f'{a} + {b} = {a+b}')
sum(2, 3)

# User input
a = input('Pasirink pirma skaiciu: ')
b = input('Pasirink antra skaiciu: ')

# Function with return
def parse(input_string):
  return int(input_string)

sum(parse(a), parse(b))

# Comments or some code
# Comments or some code
# Comments or some code
# Comments or some code
# Comments or some code
# Comments or some code
# Comments or some code



