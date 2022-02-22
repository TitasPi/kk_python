class Computer:
  def __init__(self, cpu, gpu, ram_amount):
    self.cpu = cpu
    self.gpu = gpu
    self.ram_amount = ram_amount
  
  def info(self):
    print(f'CPU: {self.cpu}')
    print(f'GPU: {self.gpu}')
    print(f'RAM: {self.ram_amount}')

  def change_cpu(self, new_cpu):
    self.cpu = new_cpu

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def info(self):
    print(f'My name is {self.name} and I\'m {self.age} years old')

# New object
my_pc = Computer('potato', 'peciulis', '69GB')

# Using function in class
my_pc.info()
# Changing properties #1
my_pc.change_cpu('Solarpanel powered potato')
my_pc.info()
# Changing properties #2
my_pc.cpu = 'AA'
my_pc.info()

me = Person('Titas', 20)

me.info()

you = Person('Robertas', 69)

you.info()