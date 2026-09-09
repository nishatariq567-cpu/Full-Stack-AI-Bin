#Part A — Python Lists (10 Intermediate-Level Questions)

#Create a list comprehension that returns the squares of only the even numbers
#from 0–20.

squares_of_evens=[]
for x in range(21):
 if x % 2==0:
    square=x**2
    squares_of_evens.append(square)
print(squares_of_evens)

#Given nums = [3, 1, 4, 1, 5, 9], sort the list without modifying the original.
#Tip: Use sorted() instead of .sort().

Numbers=[3,1,4,1,5,9]
print(Numbers)
Numbers.sort()
print(Numbers)

#Remove duplicates from a list while preserving the original order.
#Tip: Track seen values in a new list.

Original_List=(input("Enter number like list ="))
my_list=eval(Original_List)
results=[]
for items in my_list:
  if items not in results:
    results.append(items)
print(results)

#Flatten the nested list [[1, 2], [3, 4], [5]] into a single list using a list comprehension.
nested_list = [[1, 2], [3, 4], [5]]
print(nested_list)
flate_list=[]
for sublist in nested_list:
  for number in sublist:
    flate_list.append(number)
print("Proper Data =",flate_list)

#Given names = ['alice', 'Bob', 'charlie', 'DAVID'], sort them alphabetically but ignore
#case.

names = ['charlie', 'Bob', 'alice', 'DAVID']
print(names)
names.sort(key=str.lower)
print(names)

#Replace items from index 2–4 in a list with [100, 200] using slice assignment.
#Tip: Use a[2:5] = [...].

Values=[100,200,67,90]
print(Values)
Values[0:2]=[20,60]
print(Values)

#Write a program to find all indices of a value in a list (e.g., all indices of 7).
#Tip: Use enumerate.

my_list = [10, 7, 20, 7, 30, 7, 40]
print(my_list)
indices_of_7=[]
for index,number in enumerate(my_list):
  if number==7:
    indices_of_7.append(index)
print(indices_of_7)

#Create a new list containing only elements that appear exactly once in the original
#list.

original_list = [1, 2, 2, 3, 4, 5, 5, 6]
unique_items = []
for item in original_list:
    if original_list.count(item) == 1:
        unique_items.append(item)
print(unique_items)

#Rotate a list right by one position (e.g., [1,2,3,4] → [4,1,2,3]).
#Tip: Use slicing: lst[-1:] + lst[:-1].

Rotate_list=[1,2,3,4]
print(Rotate_list)
final=Rotate_list[-1:]+Rotate_list[:-1]
print(final)

#Split a list into two lists: one with even numbers, one with odd numbers.
#Tip: Create two comprehensions.

lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst)
Even_Number=[x for x in lst if x % 2== 0]
Odd_Number=[x for x in lst if x % 2 != 0]
print("Even",Even_Number)
print("Odd",Odd_Number)


#Part B — Python Tuples (10 Intermediate-Level Questions)

#Convert the list [1, 2, 3, 4] into a tuple and then unpack it into four variables.
#Tip: Use tuple() and simple unpacking.

my_newList=[1,2,3,4]
print(my_newList)
new_tuple=tuple(my_newList)
print(new_tuple)
a,b,c,d=new_tuple
print("a :",a)
print("b :",b)
print("c :",c)
print("d :",d)

#Given t = (('a', 1), ('b', 2), ('c', 3)), create a list of all second elements.
#Tip: Use a comprehension: x[1].

t = (('a', 1), ('b', 2), ('c', 3))
print(t)
second_elements=[x[1] for x in t]
print(second_elements)

#Write a function that returns multiple values (sum, min, max) using a tuple.
#Tip: Return (..., ..., ...) and unpack later.

def get_stats(lst):
    return (sum(lst), min(lst), max(lst))
numbers = [10, 20, 30, 40]
Sum, Min, Max = get_stats(numbers)
print("Sum:", Sum)   
print("Min:", Min)   
print("Max:", Max)    

#Combine two tuples (1, 2, 3) and (4, 5) then convert the result to a list.
#Tip: Use + to join them.

tuple1=(1,2,3)
tuple2=(4,5)
print(tuple1)
print(tuple2)
tuple3=tuple1+tuple2
convert_list=list(tuple3)
print(convert_list)

#Given a tuple of numbers, find the element with the highest frequency.
#Tip: Loop through unique items using set(t).

t = (1, 3, 2, 3, 4, 3, 2, 1, 3)
highest_frequency_element = max(set(t), key=t.count)
print(highest_frequency_element) 

#Check if two tuples contain the same elements regardless of order.
#Tip: Compare sorted(tuple) values.

tp1 = (1, 3, 2)
tp2= (3, 1, 2)
Final_result=sorted(tp1)==sorted(tp2)
print(Final_result)

#Extract the last three items from a tuple using slicing.
#Tip: Use negative indexing: t[-3:].

T_var=(1,6,8,9.0,2)
Three_values=T_var[-3:]
print(Three_values)

#Concatenate a tuple with itself three times (repeat operation).
#Tip: Use tuple * 3.

op=("Pakistan")
Repeat_op=op*3
print(Repeat_op)

#Convert a nested tuple ((1,2),(3,4)) into a flat tuple (1,2,3,4).
#Tip: Use a comprehension inside tuple().

nested = ((1, 2), (3, 4))
flate_tuple=tuple(num for items in nested for num in items)
print(flate_tuple)

#Store coordinates in tuples and calculate the Manhattan distance.
#Tip: Use absolute difference formula: abs(x1-x2) + abs(y1-y2).

point1 = (10, 20)
point2 = (15, 25)
x1,x2=point1
y1,y2=point2
Distance=abs(x1-x2)+abs(y1-y2)
print(Distance)

#Part C — Python Sets (10 Intermediate-Level Questions)

#Given two sets, find elements that are in the first set but not the second.
#Tip: Use the - operator.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
result = set1 - set2
print(result) 