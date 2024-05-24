
# ''' REMOVING DUPLICATES FROM A LIST '''
# def remove_duplicates(input_list):
#   unique_elements = []
#   for element in input_list:
#       if element not in unique_elements:
#           unique_elements.append(element)
#   return unique_elements
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# input_list = input("Enter a list of elements separated by space: ").split()
# print("List with duplicates removed:", remove_duplicates(input_list))

# '''SUM OF ALTERNATIVE ELEMENTS IN A LIST'''

# numbers = input("Enter a list of numbers separated by spaces: ")
# numbers_list = numbers.split()  
# sum_of_alternate_elements = 0
# for index, number in enumerate(numbers_list):
#     if index % 2 == 0:
#         sum_of_alternate_elements += int(number)
# print("Sum of alternate elements: ",sum_of_alternate_elements)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ''' MERGING TWO LISTS '''
# def merge_sorted_lists():
#     list1 = input("Enter the first sorted list separated by spaces: ").strip().split()
#     list2 = input("Enter the second sorted list separated by spaces: ").strip().split()
#     list1 = [int(i) for i in list1]
#     list2 = [int(i) for i in list2]
#     merged_list = sorted(list1 + list2)
#     return merged_list
# print("Merged sorted list:", merge_sorted_lists())
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# '''FINDING MINIMUM AND MAXIMUM IN A LIST'''
# def min_max(list):
#   minimum=maximum=list[0]
#   for item in list:
#       if minimum>item:
#           minimum=item


#   for item in list:
#       if maximum<item:
#           maximum = item

#   print("Minimum:",minimum)
#   print("Maximum:",maximum)


# list = [int(ele) for ele in input("Enter a list of numbers separated by spaces:").split()]
# min_max(list)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# '''COUNT OCCURENCES IN A LIST'''
# def count_occurrences(lst, element):
#   count = 0
#   for i in lst:
#       if i == element:
#           count += 1
#   return count
# input_lst = input("Enter a list of elements separated by spaces: ").split()
# element = input("Enter an element to count its occurrences in the list: ")
# input_lst = [int(i) for i in input_lst]
# result = count_occurrences(input_lst, int(element))

# print("The element",element,"occurs",result,"times in the list.")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# '''ROTATING IN A LIST'''
# def rotate_right(lst, k):
#   rot_index = len(lst) - k % len(lst)
#   rotated_lst = lst[rot_index:] + lst[:rot_index]
#   return rotated_lst
# lst_input = input("Enter a list of elements separated by spaces: ").split()
# lst_input = [int(i) for i in lst_input] 
# k = int(input("Enter the number of steps to rotate the list to the right: "))
# rotated_list = rotate_right(lst_input, k)
# print("The list after rotating",k,"steps to the right is: ",rotated_list)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# '''SPLITING A LIST'''
# def main():
#   lst = input("Enter elements for the list (separated by spaces): ").split()
#   k = int(input("Enter the index to split the list at: "))
#   list1, list2 = lst[:k], lst[k:]
#   print("List 1:", list1)
#   print("List 2:", list2)

# if _name_ == "_main_":
# main()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# '''ARMSTRONG NUMBER'''
# n=int(input("Enter a number: "))
# s=0
# temp=n
# while temp>0:
#     d = temp %10
#     s+= d**3
#     temp//=10
# if n==s:
#     print(n,"is an Armstrong number")
# else:
#     print(n,"is not an Armstrong number")
  
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# '''ARMSTRONG IN GIVEN RANGE'''
# def arms(num):
#   num_str =str(num)
#   num_digits=len(num_str)
#   armsum=sum(int(digit)**num_digits for digit in num_str)
#   return armsum==num
# n=int(input("Enter the starting number of the range: "))
# n1=int(input("Enter the ending number of the range: "))
# print("Armstrong numbers within the range ", n, "to", n1, "are:")
# for num in range(n,n1+1):
#   if arms(num):
#       print(num)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# boys={37}
# girls={23}
# chess={27}
# football={2}
# kabaddi={5}
# cricket={11}
# rest={15}
# outdoor=football.union(cricket.union(kabaddi))
# print("the students who are not interested in any sports =",sum(rest))
# print("the students interested in chess =",sum(chess))
# print("the students who like outdoor sports =",sum(outdoor))
# print("the division  between indoor and outdoor =",sum(chess),":",sum(outdoor))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# march={1:39.3,2:40.3,3:6.2,4:0,5:8.1,6:31.3,7:6.2}
# march.keys()
# march.values()
# print(march[3])
# march.pop(1)
# print(march)
# for date,rainfall in march.items():
#     if rainfall<50:
#         print(date)
#     elif rainfall<20 and rainfall>50:
#         print(date)
# l=march.values()
# h=len(march.values())
# for i in range(h):
#     s=sum(l)/h
# print(s)
# # -----------------------------------------------------------------------------------------------------------------------------------------------------------
# cse_a={}
# cse_a[101]=[90,66,77]
# cse_a[102]=[80,76,89]
# cse_a[103]=[40,88,63]
# cse_a[104]=[30,99,99]
# cse_a[105]=[66,77,88]
# for rollno,marks in cse_a.items():
#     cse_a[rollno]=round(sum(marks)/len(marks),2)
# print(cse_a)
# print(max(cse_a))
# print(min(cse_a))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# n=input("Enter the word: ")
# s=n.split()
# l=len(s)

# if s[l]=='g'and s[l-1]=='n' and s[l-2]=='i':
#     n.remove[l]
  
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# def prog1(txt):
#     l=txt.split(" ")
#     for i in range (len(l)):
#         m=l[i].strip()
#         l[i]=m
#     txt="".joins(l)
#     txt=txt.replace("not poor","good")
#     return txt
# print(prog1(input()))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# j="kmit rocks"
# k=j.split()
# print(k)
# for i in range (len(k)):
#     k[i]=k[i].capitalize()
# print(k)
# o=" ".join(k)
# print(j,o)
# print(j.title())
# v=k.casefold()
# print(v)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

k=input("Enter your email id")
if k.count("@")==1:
    print("VAlid")
k.center        


                                            