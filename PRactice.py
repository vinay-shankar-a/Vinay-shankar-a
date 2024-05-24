# def add(a,b):
#     print(a+b)
# def printhello(count):
#     for i in range(count):
#         if count == 5:
#             return "GoodBye"
#         print("Hello ",i)

# k=printhello(10)
# print (k)
# if k==None
#     print("NO value being returned")
# else :
#     print(k)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def playgame():
#     import random
#     magicnumber=random.randint(1,100)
#     attempt=0
#     while True:
            
#                 uc=int(input("Enter your choice: "))
#                 attempt+=1
#                 if magicnumber==uc:
                    
#                     # print("Correct guess!!! I will buy you a chicken dinner.")
#                     # print("You've taken", attempt ,"attempts to guess the correct one")
#                     return attempt
#                     break
#                 elif magicnumber>uc: 
#                     print("Vlaue is too low.. Guess a higher number")
                    
#                 elif magicnumber<uc:
#                     print("Vlaue is too high.. Guess a Lower number")
# l = playgame()
# if l<7:
#       print("You are Genious.. You just took only", l, "attempts to guess the number.")
# else:
#       print("You are useless dumb.. You took", l, "attempts to guess the number.")        
#---------------------------------------------------------------------------------------------------------------------------------------------------
# k=input("Enter your name: ")
# l=len(k)
# for i in range (l,0):
#     a=k[i]
#     b=[a]
#     print(b)
#     i=i-1
#---------------------------------------------------------------------------------------------------------------------------------------------------

# def splitlist(l):
#     number=
#     for i in range(0, len(l),number):
    
#         d=(l[i:i+number])
        
# l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# splitlist(l)
print("Enter the list")
l=input().split(" ")
h= len(l)
l1=l[0:h:2]
print(l1)
l2=l[1:h:2]
print(l2)

