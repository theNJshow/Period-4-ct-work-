"""
Program Goals:
1. get the input from the user!
2. Convert that input to an INT
3. Add that input to a list
4. Pull values from specific index positions    
"""

#create funtions that will perform those actions above
import random 
myList = []
unique_list = []

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose one of the following options. Type a number ONLY!")
            choice = input("""1. Add to list,
2. Add a bunch o' numbers 
3. Return the value at an index position
4. Print contents of list
5. Random choice
6. Linear search
7. Print lists 
8. End Program   """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch() 
            elif choice == "3":
                indexValues()
            elif choice == "4":
                sortList(myList)
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch()
            elif choice == "7"
                printLists()
            else:
                break
        except:
            print("An error occurred")
                      
def addToList():
    newItem = input ("Please type in integer!  ")
    myList.append(int(newItem))
    print(myList)

def addABunch():
    print("We're gonna add a bunch of numbers!")
    numToAdd = input("How many integers would you like to add? ")
    numRange = input("And how high would you like these numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete!") 


def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new list?  Y/N   ")
    if showMe.lower() == "y":
        print(unique_list)


def indexValues():
    indexPos = input("At what index position would you like to look?  ")
    print(myList[int(indexPos)])

def randomSearch():
    print("Here's a rondon value from your list!")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're going to search through the list IN THE WORST WAY POSSIBLE")
    searchItem = input("What are you looking for? Number-wise?  ")
     for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item ia at index {}".format(x))

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        wichOne = input("Which list? sorted or un-sorted?  ")
        if wichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)
        
if __name__ == "__main__": 
    mainProgram() 
