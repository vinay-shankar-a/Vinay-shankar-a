'''
Write a python program using if else condition where the inputs are age 
and gender should be accepted from the user,
apply discounts based upon the below criteria,
i)if gender is female give 30% discount,
ii)if age is greater than 60 apply 20% discount
if they belong to both the categories then apply i & ii conditions
Note:Ticket price must be Rs.1000.

Sample Input-Output1:

Enter your age:25                                                                         
Enter your gender:male                                                                   
Your ticket price is:$1000.00                                                            
                              
Sample Input-Output2:

Enter your age:65                                                                         
Enter your gender:female                                                                  
Your ticket price is:$500.00               



'''
age=int(input("Enter your age:"))
gender=input("Enter your gender:")
if (gender == "female"):
    if(age<60):
        amt=1000-((1000*30)/100)
        print("Your ticket price is:$%.2f"%amt)
    else:
        amt=1000-((1000*50)/100)
        print("Your ticket price is:$%.2f"%amt)
elif (gender == "male"):
    if(age<60):
        amt=1000
        print("Your ticket price is:$%.2f"%amt)
    else:
        amt=1000-((1000*20)/100)
        print("Your ticket price is:$%.2f"%amt)
        
# if (age<18):
#     print("Child")
# elif (age>=18 and age<=25):
#     print("Adult")
# elif (age>60 and age<=100):
#     print("Senior citizen")
# elif(age>100):
#     print("Free")
# else:
#     print("Adult")

