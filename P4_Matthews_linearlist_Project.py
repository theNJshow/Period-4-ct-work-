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
    #build our while loop 
    while True:
        print("Hello, there! Let's work with lists!")
        print("Choose one of the following options.  Type the number of the choice")
        choice = input("""1. Add to list,
2. Add a bunch of numbers 
3. Return the value at an index position
4. Print contents of list
5. Random choice
6. Linear search
7. Recursive Binary Search
8. Iterative Binary Search 
9. Print lists 
10. Quit   """)
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
            elif choice == "7":
                binSearch = input("What number are you looking for?  ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "8":
                binSearch = input("What number are you looking for?  ")
                result = iterativeBinarySearch(unique_list, int(binSearch))
                if result != -1:
                    print("Your number is at index position {}".format(result))
                else:
                    print("Your number is not found in that list, bud!")
            elif choice == "9":
                printLists()
            else:
                break
        except:
            print("An error occurred")
                      
def addToList():
    print("Adding to a list! Great choice!")
    newItem = input ("Please type in integer!  ")
    myList.append(int(newItem))
    #we need th about errors 

def addABunch():
    print("We're gonna add a bunch of numbers!")
    numToAdd = input("How many integers would you like to add? ")
    numRange = input("And how high would you like these numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete!") 


def sortList(myList):
    #note that this is the first function we've built here that takes ARGUMENTS
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new list?  Y/N   ")
    if showMe.lower() == "y":
        print(unique_list)


def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("At what index position would you like to look?  ")
    print(myList[int(indexPos)])

def randomSearch():
    print("Here's a rondon value from your list!")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're going to search through the list IN THE WORST WAY POSSIBLE")
    searchItem = input("What are you looking for? Number-wise?  ")
    indexCount = 0
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            indexCount = indexCount + 1
            print("Your item ia at index {}".format(x))
    print(indexCount)

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] == x:
            print("Oh what luck. your number is at position {}".format(mid))
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        else:
            return recursiveBinarySearch(unique_list, mid, + 1, high, x)
    else:
        print("Your number isn't here!")

def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list [mid] < x:
            low = mid + 1

        elif unique_list [mid] >x:
            high = mid -1
        else:
            return mid
    return -1 



        
            
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
