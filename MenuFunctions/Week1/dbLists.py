import os
print("\nDisplaying InfoDB List now.\n")
InfoDb = []
#Append firstname, lastname, birt month, residence, and email all appended
#list within list called fav nba players, with more than 4 items
InfoDb.append({  
 "FirstName": "Colin",  
 "LastName": "Howard",  
 "DOB": "March 14th",  
 "Residence": "Poway",  
 "Email": "colinh36220@stu.powayusd.com",  
 "Hobbies":["Cooking","Videogames","Woodworking","Sleeping"]  
}) 
#Function to print data stored in InfoDb list
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
  print_data(0)
quit=input("Do you want to go back to the main menu? (yes/no) ")

if quit=="yes":
  os.system('clear')
  #Run main here#
else:
  print("Staying put")