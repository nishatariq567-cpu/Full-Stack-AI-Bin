import numpy as np

Funding_rounds,Investment_Amount,Num_of_investors=np.genfromtxt("Week4/startup_growth_investment_data.csv",delimiter=",",usecols=(2,3,5),dtype=None,unpack=True,skip_header=1)
print(Funding_rounds)
print(Investment_Amount)
print(Num_of_investors)

#statistics operations

print("Average investment startup =",np.average(Investment_Amount))
print("Minimum investment are =",np.min(Investment_Amount))
print("Maximum investment are =",np.max(Investment_Amount))
print("Median of Investment Amount =",np.median(Investment_Amount))
print("Mean of the investment amount =",np.mean(Investment_Amount))
print("25 percentile of investment =",np.percentile(Investment_Amount,25))
print("75 percentile of investment =",np.percentile(Investment_Amount,75))
print("3 percentile of investment =",np.percentile(Investment_Amount,3))

print("Average of the funding rounds =",np.average(Funding_rounds))
print("Minimum funding rounds are =",np.min(Funding_rounds))
print("Maximum Funding rounds are =",np.max(Funding_rounds))
print("Median of funding rounds =",np.median(Funding_rounds))
print("Mean of Funding Rounds =",np.mean(Funding_rounds))
print("25 percentile of funding rounds =",np.percentile(Funding_rounds,25))
print("75 percentile of funding rounds =",np.percentile(Funding_rounds,75))
print("3 percentile of funding rounds =",np.percentile(Funding_rounds,3))

#Maths operations

print("Square of number of investor =",np.square(Num_of_investors))
print("square root of number of investor =",np.sqrt(Num_of_investors))
print("Power of number of investor =",np.power(Num_of_investors,Num_of_investors))
print("Absolute of number of investor =",np.abs(Num_of_investors))

# Perform basic arithmetic operations

Addition=Funding_rounds+Num_of_investors
Substraction=Funding_rounds-Num_of_investors
Multiplication=Funding_rounds*Num_of_investors
Dividing=Funding_rounds/Num_of_investors

print("Addition of funding round and number of investor =",Addition)
print("Subtraction of funding round and number of investor =",Substraction)
print("Multiplication of funding round and number of investor =",Multiplication)
print("Division of funding round and number of investor =",Dividing)

#Trigonometric Functions
InvestmentPie = (Investment_Amount/np.pi) +1
print("Sine of the InvestmentPie =",np.sin(InvestmentPie))
print("Cosine of the InvestmentPie =",np.cos(InvestmentPie))
print("Tangent of the InvestmentPie =",np.tan(InvestmentPie))

# Calculate the hyperbolic sine Cosine and tangent
print("Hyperbolic sine of InvestmentPie =",np.sinh(InvestmentPie))
print("Hyperbolic cosine of InvestmentPie =",np.cosh(InvestmentPie))
print("Hyperbolic Tangent of InvestmentPie =",np.tanh(InvestmentPie))

## Calculate the inverse hyperbolic sine and Cosine
print("Inverse Hyperbolic Sine of InvestmentPie =",np.arcsin(InvestmentPie))
print("Inverse Hyperbolic Cosine of InvestmentPie =",np.arccos(InvestmentPie))

# Calculate the natural logarithm and base-10 logarithm

print("Natural Logarithm of InvestmentPie =",np.log(InvestmentPie))
print("Base 10 Algarithm of InvestmentPie =",np.log10(InvestmentPie))

#Create Two Dimensional arrary and find number of dimensions ,Number of array ,Data type of array,size of array in each dimension
 
D2FundingandInvestor=np.array([Funding_rounds,Num_of_investors])
print("Two Dimensional array are =",D2FundingandInvestor)
print("Number of that array is =",np.size(D2FundingandInvestor))
print("Dimension of array =",np.ndim(D2FundingandInvestor))
print("Find number of element in each array =",np.shape(D2FundingandInvestor))

# Splicing array
print("Slicing of array by given start:ending:step = ",D2FundingandInvestor[0:1:1,4:9:1])
print("Second Slicing of array =",D2FundingandInvestor[0:1:1,9:18:1])

# Indexing array
print("2d array fetch value by index =",D2FundingandInvestor[0,18])
print("second 2d array fetch value by index =",D2FundingandInvestor[1,45])

#reshape of array
D2newarray=np.reshape(D2FundingandInvestor,(100,100))
print("after reshaping =",D2newarray)
print("Size of the reshaping array =",np.size(D2newarray))
print("Number of Dimension of array =",np.ndim(D2newarray))
print("Shape of the array =",np.shape(D2newarray))
