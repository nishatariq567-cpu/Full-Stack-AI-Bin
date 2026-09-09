#Part A — Python Lists (10 Beginner Questions)

#Create a list nums = [3, 1, 4, 1, 5] and print the first and last elements.

List_nums=[3,1,4,1,5]
print(List_nums)
print("First Number =",List_nums[0])
print("Last Number =",List_nums[-1])

#Find the length of the list colors = ['red', 'blue', 'green'].

List_Colour=["red","Blue","Green"]
print(List_Colour)
print("Length of the List =",len(List_Colour))

#Append 'yellow' to the list colors = ['red', 'blue'].

Add_item_list=["red","blue"]
print(Add_item_list)
Add_item_list.append("Yellow")
print("After Append Item =",Add_item_list)

#Insert 'orange' at index 1 in fruits = ['apple', 'banana'].

Insert_item_list=["apple","banana"]
print(Insert_item_list)
Insert_item_list.insert(1,"Orange")
print("After Insert Item =",Insert_item_list)

#Remove 'banana' from fruits = ['apple', 'banana', 'grapes'].

Remove_Item_list=["apple","banana","grapes"]
print(Remove_Item_list)
Remove_Item_list.remove("banana")
print("after removing item =",Remove_Item_list)

#Pop the last element from items = [10, 20, 30] and print the popped value.

Items=[10,20,30]
print(Items)
Items.pop(1)
print("Ater poped the item =",Items)

#Check if 3 is in the list nums = [1, 2, 3, 4].

Nums=[1,2,3,4]
print(Nums)
if 3 in Nums:
    print("3 is in the list")
else:
    print("3 is not in the List")

#Print the slice [2, 3] from the list [0, 1, 2, 3, 4].

Slice_list=[0,1,2,3,4]
print(Slice_list)
print("Sub value of given value =",Slice_list[2:4])

#Replace the element at index 1 in a = [5, 10, 15] with 12.

a=[5,10,15]
print(a)
a[1]=12
print("After Replacing value =",a)

#Count how many times 2 appears in [1, 2, 2, 3, 2].

For_Count=[5,8,8,3,6]
print(For_Count)
totall=For_Count.count(8)
print("Total repitation of 8 =",totall)

#Part B — Python Tuples (10 Beginner Questions)

#Create a tuple t = (10, 20, 30) and print the second element.

Tuple_element=(10,20,30)
print(Tuple_element)
print("SEcond Element is here =",Tuple_element[1])

#Find the length of tuple ('a', 'b', 'c').

Find_len=("a","b","c")
print(Find_len)
print("length of tuple =",len(Find_len))

#Unpack the tuple (4, 5) into variables x and y.
#Tip: x, y = (4, 5).

x,y=(4,5)
print("Value of x =",x)
print("value of y =",y)

#Check if 'b' is in the tuple ('a', 'b', 'c').

Character=("a","b","c")
if "b" in Character:
    print("Yes B in the Tuple")
else:
    print("B is not in Tuple")

#Create an empty tuple and print its type.

Empty_tuple=()
print(type(Empty_tuple))

#Concatenate (1, 2) and (3, 4) into a new tuple.

touple1=(1,2)
touple2=(3,4)
tuple3=touple1+touple2
print("After Adding two tuples",tuple3)

#Repeat (7,) three times.

Repeat_item=(7,)
result=Repeat_item*3
print("After Applying repeated method =",result)

#Find the index of 2 in (1, 2, 3, 2).

Index_tuple=(1,2,3,2)
print(Index_tuple)
position=Index_tuple.index(2)
print("Index of 2 is =",position)

#Count how many times 2 appears in (1, 2, 3, 2).

Tuple_Appears=(1,2,3,2)
print(Tuple_Appears)
resuls=Tuple_Appears.index(2)
print("Total repitation of 2 is =",resuls)

#Create a single‑ element tuple containing the value 5.
#Tip: Remember to use a comma: (5,).

single_tuple = (5,)
print(single_tuple)
print(type(single_tuple))
print("Next ......")

#2nd method 

single_tuple2 = (5)
print(single_tuple2)
print(type(single_tuple2))

#Part C — Python Sets (10 Beginner Questions)

#Create a set from [1, 2, 2, 3] and print it.
#Tip: Use set(list)

My_list=[1,2,2,3]
print(My_list)
my_set=set(My_list)
print(my_set)

#Add element 4 to the set {1, 2, 3}.
set_add={1,2,3}
print(set_add)
set_add.add(4)
print("After addition =",set_add)

#Remove element 2 from the set {1, 2, 3}.
set_remove={1,2,3}
print(set_remove)
set_remove.discard(2)
print("After Removing =",set_remove)

#Check if 5 is in the set {1, 3, 5}.
set_check={1,3,5}
print(set_check)
if 5 in set_check:
    print("5 is in the set")
else:
    print("5 is not in the set")

#Find the length of set {10, 20, 30}.
set_length={10,20,30}
print(set_length)
print('Length of the Set is =',len(set_length))

#Clear all elements from the set {1, 2, 3}.
set_clean={1,2,3}
print(set_clean)
set_clean.clear()
print("After clean the set is =",set_clean)

#Create a set {'a', 'b'} and add 'c' only if it’s missing.
#Tip: Check membership first: if 'c' not in s:.

Set_c={"a","b"}
print(my_set)
if "c" not in Set_c:
    Set_c.add("c")
print("After checking",Set_c)

#Convert list ['a', 'a', 'b'] into a set to remove duplicates.
#Tip: Casting removes duplicates automatically.

List_to_set=["a","a","b"]
print(List_to_set)
coverted=set(List_to_set)
print("Convert list to set :",coverted)

#Create two sets and print their union.
#Tip: Use set1 | set2.

set1={1,2,5,6}
set2={2,3,9,0,6}
print("SET 1",set1,"SET 2",set2)
final=set1|set2
print(final)

#Create two sets and print their intersection.
#Tip: Use set1 & set2.

setno1={2,3,4,6,7}
setno2={1,3,6,5,7,9}
print("SET 1",setno1,"SET 2",setno2)
final_result=setno1&setno2
print(final_result)

#Part D — Python Dictionaries (10 Beginner Questions)

#Create a dictionary {'name': 'Ali', 'age': 25} and print the name.
#Tip: Use d['name'].

New_dict={"name":"Husnain","age":25}
print(New_dict)
print("Name is here :",New_dict["name"])

#Add key 'city': 'Lahore' to a dictionary.
#Tip: Use assignment: d['city'] = 'Lahore'.

Add_dict={"age":25}
print(Add_dict)
Add_dict["City"]="lahore"
print("after addition =",Add_dict)

#Change 'age' in {'name': 'Ali', 'age': 25} to 30.
#Tip: Assign a new value: d['age'] = 30.

replace_dict={'name':'ali','age':25}
print(replace_dict)
replace_dict["age"]=30
print("After replace age :",replace_dict)

#Delete key 'age' from a dictionary.
#Tip: Use del d['age'].

Delete_dict={'name':'awais','age':29}
print(replace_dict)
del Delete_dict["age"]
print("after deleting :",Delete_dict)

#Check if key 'salary' exists in a dictionary.
#Tip: Use in operator.

Check_dict={'salary':2300,'age':56}
print(Check_dict)
if 'salary' in Check_dict:
    print("Salary is in dictionary")
else:
    print("Salary not in Dictionary")

#Print all keys from {'a': 1, 'b': 2}.
#Tip: Use d.keys().

my_dict={'a':1,'b':3,'c':2}
print(my_dict)
print("Only Keys here =",my_dict.keys())

#Print all values from a dictionary.
#Tip: Use d.values().

your_dict={'w':7,'q':2,'f':1}
print(your_dict)
print("Values is here =",your_dict.values())

#Iterate and print key‑ value pairs from {'x': 10, 'y': 20}.
#Tip: Use for k, v in d.items().

hlo_dict = {'x': 10, 'y': 20}
for k, v in hlo_dict.items():
    print(f"Key: {k}, Value: {v}")

#Use get() to safely read key 'score' from an empty dictionary.
#Tip: Use d.get('score', default_value).

game_data = {}
current_score = game_data.get('score', 0)
print(current_score)

#Create a dictionary from two lists: keys = ['a','b'], values = [1,2].
#Tip: Use dict(zip(keys, values)).

keys = ['a', 'b']
values = [1, 2]
dict = dict(zip(keys, values))
print(dict)
