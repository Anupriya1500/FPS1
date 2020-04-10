"""
# Assignments - 1
"""
"""
Name: 
    Adult Body Mass Index Calculator         

Problem Statement:
    Assuming your weight in kilogram and height in meters  
    Calculate your BMI value and print it ?
    Take the height and weight of the user from input 
Hint: 
    Divide your weight in kilograms (kg) by your height in metres (m)
    Then divide the answer by your height again to get your BMI
"""   


Height=float(input("Enter your height in meters : "))
Weight=float(input("Enter your weight in kilogram : "))
BMI= Weight/(Height*Height)
print("your Body Mass Index Is : ",round(BMI,2), "kg/m²")
 
# round is to round figure the value by 2


 




