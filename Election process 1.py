mc={"BJP":"ANISH","TRS":"ANIRUDH","CON":"AQUEEL"}
mr=[]
sc={"BJP":"SANTOSH","TRS":"VINAY","CON":"AKHIL"}
sr=[]

def Election_process():
        print("Voter:",k,"Details")
        print("WELCOME TO ELECTION CENTER")
        name=input("Enter your Name: ")
        age=int(input("Enter your Age: "))
        if age>18:
            print( name,"You are Eligible to Cast your Vote.")
            voterid=int(input("Enter your Voter id: "))
            if voterid in range(2000,4000):
                if voterid>=2000 and voterid<3000:
                    print("Welcome to Malkajgiri Constituency",name,"Garu.")
                    print("Canditates in Malkajgiri Constituency are:",mc)
                    ct=input("Cast your Vote:")
                    mr.append(ct)
                elif voterid>=3000 and voterid<4000:
                    print("Welcome to Sircilla Constituency",name,"Garu.")
                    print("Canditates in Sircilla Constituency are:",sc)
                    ct=input("Cast your Vote: ")
                    sr.append(ct)
               
            else:
                print("Your Voter id is out of Range",name,"Garu.")
         
        else:
            print(name,"Garu You are not Eligible to Cast your Vote.")
for k in range(4):
    Election_process()
print("*ELECTION RESULTS*")
print("Election Result of Malkajgiri Constituency: ")
if mr.count("BJP")> mr.count("TRS") and mr.count("BJP")>mr.count("CON"):
    print("BJP is Winner.")
elif mr.count("TRS")>mr.count("CON") and mr.count("TRS")>mr.count("BJP"):
    print("TRS is Winner")
else:
    print("CON is Winner")
print("Election Result of Sircilla Constituency:")
if sr.count("BJP")> sr.count("TRS") and sr.count("BJP")>sr.count("CON"):
    print("BJP is Winner.")
elif sr.count("TRS")>sr.count("CON") and sr.count("TRS")>sr.count("BJP"):
    print("TRS is Winner")
else:
    print("CON is Winner")
