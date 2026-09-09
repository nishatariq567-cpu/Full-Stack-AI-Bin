#Beginner Level (Strings Fundamentals)

#Write a program that reads a string and prints its length.

Data_length=input("Enter your Words: ")
print("Total Length",len(Data_length))

#Convert the input string to uppercase and lowercase.

Str_Data=input("Enter Your Data :")
print("Data in Uppercase",Str_Data.upper())
print("Data in Lowecase",Str_Data.lower())

#Count how many times a given character appears in a string (case-sensitive).

Count_Data=input("Enter the Name :")
for ch in Count_Data:
    print(ch,":",Count_Data.count(ch))

#Print the first and last character of a string; handle empty input.

String_Data=input("Enter any Fruit Name ")
print("First Character is :",String_Data[0])
print("Last Character Is ",String_Data[-1])

#Check if a substring exists in a string.

s=input("Enter the Main String :")
sub=input("Enter the Substring :")
print(sub in s)

#Print a substring from index start to end (exclusive).

user_data=input("Enter Your String Data :")
start=int(input("Enter starting Index :"))
end=int(input("Enter end Index :"))
print(user_data[start:end])

#Reverse a String

rev_var=input("Enter your father name :")
print("Reverse Data :",rev_var[::-1])

#Replace all occurrences of a word with another (case-sensitive).

s_data=input("Enter Sentance :")
old=input("Enter old Word for changing :")
new=input("Enter New Word for Changing :")
result=s_data.replace(old,new)
print(result)

#Split a sentence on spaces and join with -.

Data_Var=input("Enter Data is here :")
words=Data_Var.split()
result="-".join(words)
print(result)

#Strip Whitespace  Remove leading and trailing spaces.

strip_var=input("Enter Data with extra spaces :")
print(strip_var.strip())

#Intermediate Level (More Involved String Tasks)

#Count vowels and consonants (letters only; ignore digits/punctuation).

Text=input("Enter a String :")
Vowels=0
Consonants=0

for ch in Text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            Vowels+=1
        else:
            Consonants+=1
print("Vowels :",Vowels)
print("Consonants :",Consonants)

#Palindrome Check (Ignore Case & Non-alphanumerics)

Alp_Data=input("Enter Alphabates Data")
clean=""
for ch in Alp_Data:
    if ch.isalnum():
        clean=clean+ch.lower()

if clean==clean[::-1]:
    print("True")
else:
    print("False")

#Convert a sentence to title case without using .title().

Data_Text=input("Enter Sentance here :")
words=Data_Text.split()
result=""
for Word in words:
    result=result+Word[0].upper()+Word[1:].lower()+""
print(result.strip())

#Return a list of starting indices where a substring occurs.
#Input: s="aaaa", sub="aa" → Output: [0, 1, 2]

s = "aaaa"
sub = "aa"
ans = []
for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        ans.append(i)
print(ans)

#Build a frequency dictionary for characters (case-insensitive, skip spaces).

Text_data=input("Enter Sentance here :")
count={}
for character in Text_data.lower():
    if character!=" ":
        if character in count:
            count[character]=count[character]+1
        else:
            count[character]=1

#Check if two strings are anagrams (ignore spaces, punctuation, and case).
# Input: "Listen", "Silent" → Output: True          

Str1=input("Enter First Word :")
Str2=input("Enter Second Word :")
clean_Str1=[]
for ch in Str1.lower():
    if ch.isalpha():
        clean_Str1.append(ch)

clean_Str2=[]
for cch in Str2.lower():
    if cch.isalpha():
        clean_Str2.append(cch)

if sorted(clean_Str1)==sorted(clean_Str2):
 print("True")
else:
    print("False")

#Compress Repeated Characters (RLE-lite)
#Compress runs of the same character as <char><count>.

text = "aaabbcaaaa"
if not text:
    print("")
else:
    compressed_result = "" 
    current_char = text[0] 
    count = 1  
    for i in range(1, len(text)):
        if text[i] == current_char:
            count = count + 1 
        else:
            compressed_result = compressed_result + current_char + str(count)
            current_char = text[i]
            count = 1
    compressed_result = compressed_result + current_char + str(count)
    print(compressed_result)

#Find the longest word; if multiple, return the first. Consider words as alphabetic
#sequences.

sentence = "Find the longest_word here!"
clean_sentence = sentence.replace("_", " ").replace("!", " ")
words = clean_sentence.split()
longest = max(words, key=len)
print(longest)

#Remove Duplicate Characters but Keep Order
#Remove duplicates while preserving the first occurrence order.
#Input: "banana" → Output: "ban"
#Hint: Maintain a seen set; build result by adding chars not in seen.

Text_data="Banana"
Seen=set()
result=[]
for ch in Text_data:
    if ch not in Seen:
        Seen.add(ch)
        result.append(ch)
print("".join(result))        

#Mask Email Username
#Mask all but the first and last character 
#of the username with *; keep domain intact.

email = "john.doe@example.com"
parts = email.split("@")
username = parts[0]  
domain = parts[1]  
stars = "*" * (len(username) - 2)
output = username[0] + stars + username[-1] + "@" + domain
print(output)