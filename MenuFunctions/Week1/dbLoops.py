import os
InfoDb = []
InfoDb.append({  
 "FirstName": "Colin",  
 "LastName": "Howard",  
 "DOB": "March 14th",  
 "Residence": "Poway",  
 "Email": "colinh36220@stu.powayusd.com",  
 "Hobbies":["Cooking","Videogames","Woodworking","Sleeping"]  
}) 
def print_data(n):
  print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])
  print("\n")
  print(InfoDb[n]["DOB"])
  print("\n")
  print(InfoDb[n]["Residence"])
  print("\n")
  print(InfoDb[n]["Email"])
  print("\n")
  print("Hobbies: ", end="") 
  print(", ".join(InfoDb[n]["Hobbies"]))
  print()
#utilizes for loop
def for_loop():
  for n in range(len(InfoDb)):
    print_data(n)

#utilizes while loop while p is less than the length of the list infoDB, execute a series of steps
def while_loop(p):
  while p < len(InfoDb):
    print_data(p)
    p += 1
  return
#utilizes recursive loop in order to go backwards to execute code 
def recursive_loop(b):
  if b < len(InfoDb):
    print_data(b)
    recursive_loop(b + 1)
  return 
#returns back actual printed statements using previously defined functions
def program():
  print("----------------------------------------")
  print("For loop\n")
  for_loop()
  print("----------------------------------------")
  print("While loop\n")
  while_loop(0)
  print("----------------------------------------")
  print("Recursive loop\n")
  recursive_loop(0)
  print("----------------------------------------")
  program()

quit=input("Do you want to go back to the main menu? (yes/no) ")

if quit=="yes":
  os.system('clear')
  #replace with main function here#
else:
  print("Staying put")