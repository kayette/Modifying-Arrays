from array import array

def firstOption():
    print("You have chosen to \033[0;34madd an element to the array. \033[0m")
    firstInput = int(input("\nEnter an element to add to the array: "))
    array.append(firstInput)
    print(f"\nHere is your updated array: {array}")

def secondOption():
    print("You have chosen to \033[1;33minsert an element to the array. \033[0m")
    secondInput = int(input("\nEnter an element to insert in the array: "))
    inputPosition = int(input("\nPlease indicate which position (0-9) you would like the element to be inserted: "))
    array.insert(inputPosition, secondInput)
    print(f"\nHere is your updated array: {array}")

def thirdOption():
    print("You have chosen to \033[0;32mmodify an element in the array. \033[0m")
    modifyPosition = int(input("\nPlease indicate the current position of the element (0-9) which you wish to modify: "))
    thirdInput = int(input("\nEnter a new element to replace the previous element with: "))
    array [modifyPosition] = thirdInput
    print(f"\nHere is your updated array: {array}")

def fourthOption():
    print("You have chosen to \033[1;31mdelete an element in the array. \033[0m")
    fourthInput = int(input("\nEnter the element which you wish to remove from the array: "))
    array.remove(fourthInput)
    print(f"\nHere is your updated array: {array}")

def fifthOption():
    print("\nYou have chosen to \033[0;33marrange the array in ascending order. \033[0m")
    array.sort()
    print(f"\nHere is your updated array: {array}")

def sixthOption():
    print("\nYou have chosen to \033[0;34marrange the array in descending order. \033[0m")
    array.sort(reverse=True)
    print(f"\nHere is your updated array: {array}")
    
print("\nWelcome to \033[3mArray of Sun \033[0mwhere you can freely modify and arrange elements!\nSelect a number from the menu below and see the magic.")
array = [1,5,4,3,2,10,7,9,8,6]
print(f"\nCurrent array: {array}")
print("""
        1 -> \033[1;33mAdd an element\033[0m
        2 -> \033[1;35mInsert an element\033[0m
        3 -> \033[0;32mModify an element\033[0m
        4 -> \033[1;31mDelete an element\033[0m
        5 -> \033[0;33mArrange in ascending order\033[0m
        6 -> \033[0;34mArrange in descending order\033[0m
        """)

while True:
    userInput = int(input("Select an option to perform on the current array: "))
    if userInput >= 1 and userInput <=6:
        break

    else: 
        print("\nYou have chosen an invalid option. \033[3mPlease select an option from \033[4m1-6\033[0m in the menu.\033[0m\n")

if userInput == 1:
    firstOption()
elif userInput == 2:
    secondOption()
elif userInput == 3:
    thirdOption()
elif userInput == 4:
    fourthOption()
elif userInput == 5:
    fifthOption()
elif userInput == 6:
    sixthOption()