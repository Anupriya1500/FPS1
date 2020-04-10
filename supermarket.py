# Day 5

# Assignments - 9
# ifinitely user se input
# blank entry means exit finish

"""
Name: 
    Supermarket      
Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User   
Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict 
Sample Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
Sample Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20
"""    
  
dict1 = {}
while True:
    str1 = input("enter the item with the respective price :- ")
    if str1 == "":
        break
    list1 = str1.split()
    
    price = int(list1[-1])              # price is the value for dict1    
    
    Item = " ".join(list1[:-1])         # Item is the key for dict1    
    
    if Item not in dict1:
        dict1[Item] = int(price)
    else:
        dict1[Item] = dict1[Item] + int(price)
       
print("your orders are with total price are  : ",dict1)      
              
     



