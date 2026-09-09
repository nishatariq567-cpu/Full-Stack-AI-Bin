#Write a program to create a new string made of an input string’s first,
#middle, and last character

String=input("Enter Your Data: ")
print("First Character",String[0])
print("Middle Character",String[len(String)//2])
print("Last Character",String[-1])

#Write a program to count occurrences of all characters within a string
#Given.

String_Data=input("Enter English Word: ")
for ch in String_Data:
    print(ch,":",String_Data.count(ch))

#Reverse a given string

User_input=input("Enter Your Name: ")
print(User_input[::-1])

#Split a string on hyphens

Data_var=input("Enter 3 names by using - :")
Parts=Data_var.split("-")
for i in Parts:
    print(i)

#Remove special symbols / punctuation from a string

Mix_data=input("Enter Mix Data :")
new=""
for ch in Mix_data:
    if ch.isalnum():
        new=new+ch

print(new)


        