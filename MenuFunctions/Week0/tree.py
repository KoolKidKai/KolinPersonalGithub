# Generating Pole Shape
def poleShape(n):
  for i in range(n):
      for j in range(n-1):
          print(' ', end=' ')
      print('* * *')

def triangleShape(n):
  for i in range(n):
      for j in range(n-i):
          print(' ', end=' ')
      for k in range(2*i+1):
          print('*',end=' ')
      print()

row = int(input('Enter number of rows: '))
      
triangleShape(row)
triangleShape(row)
poleShape(row)