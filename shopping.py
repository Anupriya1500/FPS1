#  ek ek word input lena hai , infinte loop asking for input 
# when written done it will quit the loop and then items returned as list 

# Assignments - 7
"""
Name: 
    Shopping List        
Problem Statement:
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT the program
    And once i quit, I want the app to show me everything thats on my list.

Hint:
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE

    Step 6: print out the list
"""

  
ShoppingList = []  
print("Instructions to use the use the app : ")  
 
def help_ins():    
    print("1) Enter items you wish to add to list")
    print("2) Type DONE/done to finish the list ")
    print("3) Type SHOW/show to show the list  ")
    print("4) Type HELP/help for instructions ")
    
def add_item(item):
    ShoppingList.append(item)
    print("Added {} to shopping list. List now has {} items".format(item, len(ShoppingList)))
    
       
def show_list():
    
    print("Shopping List :")
   
    for item in ShoppingList:
        print(" -> " + item)
        
def final_list():
    print("Final list is ")
    for item in ShoppingList:
        print(">>" +item)
                                     
def main():   
    help_ins()
    while True:
        item = str(input("Enter an item : "))
        if item == 'DONE' or item == 'done':
            final_list()
            break
        elif item == 'SHOW' or item == 'show':
            show_list()
        elif item == 'HELP' or item == 'help':
            help_ins()
        else:
            add_item(item)
            
main()

