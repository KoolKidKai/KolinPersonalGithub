# Datalists hack task -------------------------------
InfoDb = []

InfoDb.append({  
               "Name": "Colin Howard",  
               "Birthdate": "March 14th",
               "Location": "Poway",
               "Hobbies":["Cooking", "Instruments", "Volunteering", "Gaming"]  
              })  

InfoDb.append({  
               "Name": "Lucas Huang",  
               "Birthdate": "August 28th",
               "Location": "4S Ranch",
               "Hobbies":["Basketball", "Pokemon", "Cats & Soup", "Eating"] 
              })

InfoDb.append({  
               "Name": "Timmy Lin",  
               "Birthdate": "November 10th",
               "Location": "Hayden Lake Place",
               "Hobbies":["Gaming", "Anime", "Hanging out with Colin <3", "Fishing"] 
              })

# Datalist to print using the three loops - for - while - recursion

InfoDbLoop = []

InfoDbLoop.append({  
               "Name": "Colin Howard",  
               "Birthdate": "March 14th",
               "Location": "Poway",
               "Hobbies":["Cooking", "Gaming", "Volunteering", "Instruments"]  
              })  

InfoDbLoop.append({  
               "Name": "Lucas Huang",  
               "Birthdate": "August 28th",
               "Location": "4S Ranch",
               "Hobbies":["Basketball", "Pokemon", "Cats & Soup", "Eating"] 
              })

InfoDbLoop.append({  
               "Name": "Timmy Lin",  
               "Birthdate": "November 10th",
               "Location": "Hayden Lake Place",
               "Hobbies":["Gaming", "Anime", "Hanging out with Colin <3", "Fishing"] 
              })

def print_data(n):
  print(InfoDbLoop[n]["Name"])  # print name
  print("\t", "Birthdate: ", end="")
  print(InfoDbLoop[n]["Birthdate"])
  print("\t", "Location: ", end="")  # \t is a tab indent, end="" make sure no return occurs
  print(InfoDbLoop[n]["Location"])
  print("\t", "Hobbies: ", end="")
  print(", ".join(InfoDbLoop[n]["Hobbies"]))  # join allows printing a string list with separator
  print()


# Dataloops hack task ------------------------------------

# For Loop
def for_loop():
  for n in range(len(InfoDbLoop)):
    print_data(n)

# While Loop
# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
  while n < len(InfoDbLoop):
    print_data(n)
    n += 1
  return

# Recursion
# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
  if n < len(InfoDbLoop):
    print_data(n)
    recursive_loop(n + 1)
  return # exit condition

def __init__(self, n):
  self.n = n

def databases():
  print("Printing for loop")
  print(" ")
  for_loop()
  print("Printing while loop")
  print(" ")
  while_loop(0)
  print("Printing recursive loop")
  print(" ")
  recursive_loop(0)