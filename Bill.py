import os
n = int(input("Enter the number of customers: "))
for i in range(1, n + 1):
    print("WELCOME TO RED CHILLI RESTAURANT")
    print("Choose which would you like to have")
    a = int(input("1.Breakfast\n2.Lunch\n3.dinner\n "))
    menu = {
        1: 'Breakfast.txt',
        2: 'Lunch.txt',
        3: 'Dinner.txt'
    }
    if a in menu.keys():
        b = menu[a]
        f = open("restaurant\\" + b)
        l = f.read()
        print(l)
        while(1):
            s = int(input("Please select the dish you want to have: "))
            if(s > 3 or s < 0):
                print("Please select from given options only.")
            else:
                break
        p = open("restaurant\\menu.txt")
        r = p.readlines()
        item = (r[a - 1].split(","))[2 * s - 1]
        cost = (r[a - 1].split(","))[2 * s]
        g = os.getcwd()
        os.chdir(g + "\\restaurant")
        os.makedirs("Customer_bill", exist_ok=True)
        h = open("Customer_bill\\Bill.txt", "a")
        h.write(f"\n{i}).The Ordered item is {item} and Bill is Rs.{cost}")
        h.close()
        print("Data has been added successfully.\n")
        os.chdir(g)
    else:
        print("Please select from the options given in menu.")