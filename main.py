# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
# imports from other .py files
from MenuFunctions.Week0.ship import ship
from MenuFunctions.Week1.database import for_loop, while_loop, recursive_loop


# Main Menu
main_menu = []

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
math_sub_menu = [
    ["Lists", "MenuFunctions/Week1/dbLists.py"],
    ["Loops", "MenuFunctions/Week1/dbLoops.py"],
    ["For Loop", for_loop],
    ["While Loop", while_loop],
    ["Recursive Loop", recursive_loop],
    ["Fibonacci", "MenuFunctions/Week1/fibonacci.py"],
    ["Factorial", "MenuFunctions/Week2/factorial.py"],
    ["Palindrome", "MenuFunctions/Week2/mathFunction.py"],
    ["Greatest Common Denominator", "MenuFunctions/Week2/mathFunction.py"],
]

fun_sub_menu = [
    ["Swap", "MenuFunctions/Week0/swap.py"],
    ["Tree", "MenuFunctions/Week0/tree.py"],
    ["Ship", ship],
    ["Keypad", "MenuFunctions/Week0/keypad.py"],
]

#weekly menu
week0_sub_menu = [
    ["Swap", "MenuFunctions/Week0/swap.py"],
    ["Tree", "MenuFunctions/Week0/tree.py"],
    ["Ship", ship],
    ["Keypad", "MenuFunctions/Week0/keypad.py"],
]

week1_sub_menu = [
    ["Lists", "MenuFunctions/Week1/dbLists.py"],
    ["Loops", "MenuFunctions/Week1/dbLoops.py"],
    ["Fibonacci", "MenuFunctions/Week1/fibonacci.py"],
]

week2_sub_menu = [
    ["Factorial", "MenuFunctions/Week2/factorial.py"],
    ["Palindrome", "MenuFunctions/Week2/palindrome.py"],
    ["Greatest Common Denominator", "MenuFunctions/Week2/mathFunction.py"],
]



border = "=" * 25
banner = f"\n{border}\nChoose one of the options: \n{border}"



def menu():
    title = "Welcome to Colin's Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", math_submenu])
    menu_list.append(["Fun", fun_submenu])
    menu_list.append([ "----------" ])
    menu_list.append(["Week 0", week0_submenu])
    menu_list.append(["Week 1", week1_submenu])
    menu_list.append(["Week 2", week2_submenu])
    buildMenu(title, menu_list)

def math_submenu():
    title = "Math Submenu" 
    buildMenu(title, math_sub_menu)

def fun_submenu():
    title = "Fun Submenu"  
    buildMenu(title, fun_sub_menu)
  
def week2_submenu():
    title = "Week 2 Submenu" 
    buildMenu(title, week2_sub_menu)
    
def week1_submenu():
    title = "Week 1 Submenu" 
    buildMenu(title, week1_sub_menu)

def week0_submenu():
    title = "Week 0 Submenu"
    buildMenu(title, week0_sub_menu)

  
def buildMenu(banner, options):

    print(banner)

    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op


    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("Type your choice> ")
    print ()

    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try: 
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")
    print ()
    buildMenu(banner, options)  

if __name__ == "__main__":
    menu()


# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
# imports from other .py files
from MenuFunctions.Week0 import ship
from MenuFunctions.Week1 import dbLoops

# Main Menu
main_menu = [
    ["Factorial", "MenuFunctions/Week2/factorial.py"],
    ["Palindrome", "MenuFunctions/Week2/palindrome.py"],
    ["Greatest Common Denominator", "MenuFunctions/Week2/mathFunction.py"]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Swap", "MenuFunctions/Week0/swap.py"],
    ["Tree", "MenuFunctions/Week0/tree.py"],
    ["Ship", ship.ship],
    ["Keypad", "MenuFunctions/Week0/keypad.py"],
    ["Database", "MenuFunctions/Week1/dbLoops.py"],
    ["Fibonacci", "MenuFunctions/Week1/fibonacci.py"],

]

border = "=" * 25
banner = f"\n{border}\nChoose one of the options: \n{border}"


def menuc():
    title = "Class Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Submenu", submenuc])
    m = questy.Menu(title, menu_list)
    m.menu()  


def submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, sub_menu)
    m.menu()


def menu():
    title = "Welcome to Colin's Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Old Functions", submenu])
    buildMenu(title, menu_list)


def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)

def buildMenu(banner, options):

    print(banner)

    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op


    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("Type your choice> ")

    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try: 
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")

    buildMenu(banner, options)  

if __name__ == "__main__":
    menu()