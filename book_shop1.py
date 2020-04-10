# Day 4

# Assignments - 8
"""
Code Challenge
  Name: 
    Book Shop
    
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number    Book Title              Author      Quantity    Price per Item
    34587           Learning Python         Mark Lutz   4           40.95
    98762           Programming Python      Mark Lutz   5           56.80
    77226           Head First Python       Paul Barry  3           32.95
    88112           Einführung in Python3   Bernd Klein 3           24.99    
    
    
    Write a Python program, 
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 

    Output:
    [('34587', 163.8), ('98762', 284.0), ('77226', 98.85), ('88112', 74.97)]
    
    The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.
    
    Output:
    [('34587', 163.8), ('98762', 284.0), ('77226', 108.85), ('88112', 84.97)]    
 Hint: 
    Write a Python program using lambda and map.
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
      ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
      ["77226", "Head First Python, Paul Barry", 3,32.95],
      ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
    ]

"""
# using for loop 
print("USING FOR LOOP - ")
orders= [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
      ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
      ["77226", "Head First Python, Paul Barry", 3,32.95],
      ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
     ]
list1=[]

for item in orders:
    list1.append((item[0],round((item[-1]*item[-2]),2)))
print("Order summary :",list1)
print()
# The product should be increased by 10 INR if the value of the order is smaller than 100.00 INR. 
list2=[]  
for item in orders :
    if item[-1]*item[-2]<100 :
        list2.append((item[0],round((item[-1]*item[-2]+10),2)))
    else :
         list2.append((item[0],round((item[-1]*item[-2]),2)))        
print("Order summary :",list2)
print()
print()


# with list comprehension
print('USING LIST COMPREHENSION - ')
orders= [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
      ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
      ["77226", "Head First Python, Paul Barry", 3,32.95],
      ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
     ]
print("Order summary : ",[(item[0],round((item[-1]*item[-2]),2))for item in orders])
print()
# when the value of order is < 100 value increased by 10
print("Order summary : ", [(item[0],round((item[-1]*item[-2]+10),2)) if item[-1]*item[-2] < 100 else (item[0],item[-1]*item[-2]) for item in orders])
print()
print()


# with lambda and map
print("USING MAP AND LAMBDA - ")
orders= [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
      ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
      ["77226", "Head First Python, Paul Barry", 3,32.95],
      ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
     ]
print("Order summary : " , list(map(lambda x :(x[0],round((x[-1]*x[-2]),2)) , orders)))
print()
# when the value of order is < 100 value increased by 10

print("Order summary : ",list(map(lambda x :(x[0],round((x[-1]*x[-2]+10),2)) if x[-1]*x[-2]<100  else (x[0],round((x[-1]*x[-2]),2)) , orders)))









