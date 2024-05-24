n=input("Enter the word: ")
s=n.split()
l=len(s)

# if s[l-1]=='g'and s[l-2]=='n' and s[l-3]=='i':
#     s.remove[l-1]
#     s.remove[l-2]
#     s.remove[l-3]
s.remove('i')
s.remove('n')
s.remove("g")

print(s)
  
