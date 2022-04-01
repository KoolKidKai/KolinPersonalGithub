# Datalists hack task -------------------------------
InfoDb = []

InfoDb.append({  
               "Name": "Nathan Shih",  
               "Birth": "November 12",
               "Siblings": "Yes",
               "Hobbies":["Coding", "Fishing", "Driving", "Gaming"]  
              })  

InfoDb.append({  
               "Name": "Noah Jeng",  
               "Birth": "February 14",
               "Siblings": "Yes",
               "Hobbies":["Soccer", "Driving", "Gaming", "Sleeping"] 
              })

InfoDb.append({  
               "Name": "Isaac Le",  
               "Birth": "December 3",
               "Siblings": "No",
               "Hobbies":["School", "Gaming", "Listening to Music", "Math"] 
              })

InfoDb.append({  
               "Name": "Tanay Rayavarapu",  
               "Birth": "October 14",
               "Siblings": "Yes",
               "Hobbies":["Basketball", "Anime", "YouTube", "Music"] 
              })

# Datalist to print using the three loops - for - while - recursion

InfoDbLoop = []

InfoDbLoop.append({  
               "Name": "Nathan Shih",  
               "Sport": "Tennis",
               "Age": "17",
               "Hobbies":["Coding", "Fishing", "Driving", "Gaming"]  
              })  

InfoDbLoop.append({  
               "Name": "Noah Jeng",  
               "Sport": "Soccer",
               "Age": "17",
               "Hobbies":["Soccer", "Driving", "Gaming", "Sleeping"] 
              })

InfoDbLoop.append({  
               "Name": "Isaac Le",  
               "Sport": "Soccer",
               "Age": "17",
               "Hobbies":["School", "Gaming", "Listening to Music", "Math"] 
              })

InfoDbLoop.append({  
               "Name": "Tanay Rayavarapu",  
               "Sport": "Swimming",
               "Age": "17",
               "Hobbies":["Basketball", "Anime", "YouTube", "Music"] 
              })

def print_data(n):
  print(InfoDbLoop[n]["Name"])  # print name
  print("\t", "Sport: ", end="")
  print(InfoDbLoop[n]["Sport"])
  print("\t", "Age: ", end="")  # \t is a tab indent, end="" make sure no return occurs
  print(InfoDbLoop[n]["Age"])
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

def main():
  print("THIS IS THE FOR LOOP PRINTING")
  for_loop()
  print("THIS IS THE WHILE LOOP PRINTING")
  while_loop(0)
  print("THIS IS RECURSION PRINTING")
  recursive_loop(0)