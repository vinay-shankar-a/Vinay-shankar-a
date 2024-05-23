def Registration():
    al=["A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    num=['0','1','2','3','4','5','6','7','8','9']
    dun=[]
    x=0
    y=0
    uname=input("Enter the Username:")    
    for i in num:
            if i in uname:
                x+=1
                break
    for j in al:
            if j in uname:
                y+=1
                break
    if len(uname)>8 and uname.count("$")==1 or uname.count("#")==1 and x==1 and y==1:
        if uname not in dun:
            dun.append(uname)
            print("Username is Successfully Valid.")
        else:
            print("Username is Already Exist.")
    else:
        print("Invalid Username ID.")
    mail=input("Enter the mail-ID:")
    l=len(mail)
    d=mail.index("@")
    e=mail.index(".")
    ve=["@gmail",".in",".com",".edu",".ac.in",".co.in",".org"]
    p=0
    if mail[e:l:1]==ve[1] or mail[e:l:1]==ve[2] or mail[e:l:1]==ve[3] or mail[e:l:1]==ve[4] or mail[e:l:1]==ve[5] or mail[e:l:1]==ve[6]:
        p+=1
    if mail[d:e:1]=="@gmail" and p==1:
        print("Email-ID is Valid.")
    else:
        print("Email-ID is Invalid.")
    pwd=input("Enter the password:")
    a=[]
    x=0
    for i in  range(len(pwd)):
        a.append(pwd[i])
    print("List A is:",a)
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j] and a[i]==a[i-1]:
                x+=1
                break
    if len(pwd)<8 and pwd.count("^")>=1 or pwd.count("~")>=1 or pwd.count("!")>=1 or pwd.count("%")>=1 and x==1:
        print("Password is Valid..")
    else:
        print("Password is Invalid.")
    cnfmpwd=input("Enter the Confirm Password:")
    if cnfmpwd==pwd:
        print("Confirm Password is Successful.")
for n in range(1):
    Registration()