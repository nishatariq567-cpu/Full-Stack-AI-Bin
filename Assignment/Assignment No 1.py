#Write a program that converts a temperature from Celsius to Fahrenheit.
#  (Formula: Fahrenheit =(Celsius * 9/5) + 32)

Celsius=int(input("Enter Temperature in celsius :"))
Fahrenheit=(Celsius*9/5)+32
print("Temperature in Fahrenheit=",Fahrenheit)

#Calculate Area of a Rectangle

Length=int(input("Enter Length ="))
Width=int(input("Enter Width ="))
Area=Length*Width
print("Area of Rectangle=",Area)

#Calculate Compound Interest Use the formula: CI = P * (1 + R/100)**T-P
# Where P = principal, R = rate, T = time

P=int(input("Enter Principle Value="))
R=int(input("Enter Rate="))
T=int(input("Enter time="))
CI=P*(1+R/100)**T-P
print("Compound Interest =",CI)

#Perimeter of a Rectangle - 
# Take length and width as input and calculate the perimeter

Length=int(input("Enter Length="))
Width=int(input("Enter Width="))
Perimeter=2*(Length+Width)
print("Perimeter of Rectangle =",Perimeter)

#Average of Three Numbers - 
#Input three numbers and print their average

Num1=int(input("Enter First Number="))
Num2=int(input("Enter Second Number="))
Num3=int(input("Enter Third Number"))
Average=(Num1+Num2+Num3)/3
print("Average of Three Numbers=",Average)

#Square and Cube of a Number -
#Ask the user for a number and display its square and cube.

Number=int(input("Enter Number:"))
Square=(Number)*2
Cube=(Number)*3
print("Square of Number :",Square)
print("Cube of Number :",Cube)

#Distribute Items Equally - You have n candies and k students.
#Write a program to find:
#how many candies each student gets
#how many are left

Candies=int(input("Enter Number of Candies: "))
Students=int(input("Enter Number of Students: "))
Each_Student=Candies//Students
Left_Candies=Candies%Students
print("Each Student Get:",Each_Student)
print("Candies Left: ",Left_Candies)

#Calculate Profit or Loss Input cost price and selling price.
# Display either: Profit and amount, or Loss and amount, or 
#No Profit No Loss

Cost_Price=int(input("Enter Cost Price: "))
Selling_Price=int(input("Enter Selling Price: "))
if Selling_Price>Cost_Price:
    profit=Selling_Price-Cost_Price
    print("proft: ",profit)
elif Cost_Price>Selling_Price:
    Lose=Cost_Price-Selling_Price
    print("Lose: ",Lose)
else:
    print("No Proft , No Lose")
    
#Total Marks and Percentage
#Input marks of 5 subjects. Print:  Total marks  Percentage
#  Average    

sub1=int(input("Enter English number :"))
sub2=int(input("Enter Urdu Number: "))
sub3=int(input("Enter Biology Number: "))
sub4=int(input("Enter Physics Number: "))
sub5=int(input("Enter Math Number: "))
Sum=(sub1+sub2+sub3+sub4+sub5)
print("Total Numbers :",Sum)
persantage=(Sum/500)*100
print("Persantage of Numbers",persantage)
Average=Sum/5
print("Average of total number: ",Average)

#Salary Calculator Input basic salary. Calculate:  HRA = 20% of basic
#  DA = 15% of basic  Total Salary = Basic + HRA + DA

Salary=int(input("Enter Your Basic Salary: "))
HRA=Salary*20/100
DA=Salary*15/100
Total_Salary=HRA+DA+Salary
print("Total Salary include HRA+DA :",Total_Salary)

#Age in Months and Days Input your age in years. Calculate and print age in:
# Months  Days (approximate)

Age=int(input("Enter Your Age in years :"))
In_Month=Age*12
In_day=Age*365
print("Age in Months :",In_Month)
print("Age in Days :",In_day)

#Currency Converter (USD to PKR) Input amount in USD. 
# Convert using a fixed exchange rate.

Amount=int(input("Enter Amount in dollar :$"))
Rupees=Amount*280
print("Amount in rupees :",Rupees)

#Sum of First N Natural Numbers Input a number n,
#calculate sum of first n natural numbers. 
#Formula: sum = n * (n + 1) / 2

n=int(input("Enter a Number : "))
sum=n*(n+1)/2
print("First N number :",n,"Natural number is",sum)

#Percentage of Correct Answers Input total questions and correct answers
#, and calculate the percentage score.

Total_Questions=int(input("Enter Total questions: "))
Correct_Answer=int(input("Enter Correct Answers"))
Persant=(Correct_Answer/Total_Questions)*100
print("Persantage Score :",Persant,"%")

#Speed, Distance, and Time Input distance and time,
#and calculate speed.

Distance=int(input("Enter Distance :")),("Km")
Time=int(input("Enter Time :")),("hr")
Speed=Distance/Time
print("Speed is :",Speed)

#Calculate Body Mass Index (BMI) Input weight (kg) and height (m),
#then calculate: BMI = weight / (height ** 2)

weight = int(input("Enter your weight in kg: "))
height = int(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print("Your BMI is:", bmi)

#Convert Minutes to Hours and Minutes Input number of minutes
#and convert to hours and remaining minutes.
#Example: 130 minutes → 2 hours 10 minutes

minutes = int(input("Enter total minutes: "))
hours=minutes//60
remaining_minutes=minutes%60
print("Hours:",hours)
print("Remaining Minutes:",remaining_minutes)