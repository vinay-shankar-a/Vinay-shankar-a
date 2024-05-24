child=["Finding Nemo","Ninja Turtles"]
above16=["Salaar","Guntur Karam","Hi Nana"]
above60=["Baghban","KKKG"]
Female=["Kahani","Mrs Chatterjee vs Nor"]
age=int(input("Enter your age:"))
gender=input("Enter your gender:")
if(age<18):
    print("Ticket Price is:$10")
    print("Movies You would like to watch: ",child,end="")
elif(gender=="female"):
    if(age>60):
        movie=1
        amt=1000-(1000*50)/100
        print("Your ticket price is:$%.2f"%amt)
        print("Movies You would like to watch: ",end="")
        for i in above60:
            if i in Female:
                print(i)
            else: movie=-1
        if(movie==-1): print("Your Not supossed to watch movie,PLs go home")
    else:
        amt=1000-(1000*30)/100
        print("Your ticket price is:$%.2f"%amt)
        print("Movies You would like to watch: ",Female,end="")
elif(gender=="male"):
    if(age>60):
        amt=1000-(1000*20)/100
        print("Your ticket price is:$%.2f"%amt)
        print("Movies You would like to watch: ",above60,end="")
    else:
        print("Your ticket price is:$%.2f"%1000)
        print("Movies You would like to watch: ",above16,end="")

