import numpy as np
Total_Funding_USD_Millions,Valuation_USD_Millions=np.genfromtxt("Week4/global_tech_startups_2026.csv",delimiter=',',usecols=(7,8),dtype=None,unpack=True,skip_header=1,invalid_raise=False)
print(Total_Funding_USD_Millions)
print(Valuation_USD_Millions)

#statistics operations

print("Average Total_Funding_USD_Millions =",np.average(Total_Funding_USD_Millions))
print("Minimum Total_Funding_USD_Millions =",np.min(Total_Funding_USD_Millions))
print("Maximum Total_Funding_USD_Millions =",np.max(Total_Funding_USD_Millions))
print("Median of Total_Funding_USD_Millions =",np.median(Total_Funding_USD_Millions))
print("Mean of the Total_Funding_USD_Millions =",np.mean(Total_Funding_USD_Millions))
print("25 percentile of Total_Funding_USD_Millions =",np.percentile(Total_Funding_USD_Millions,25))
print("75 percentile of Total_Funding_USD_Millions =",np.percentile(Total_Funding_USD_Millions,75))
print("3 percentile of Total_Funding_USD_Millions =",np.percentile(Total_Funding_USD_Millions,3))

print("Average of the Valuation_USD_Millions =",np.average(Valuation_USD_Millions))
print("Minimum Valuation_USD_Millions are =",np.min(Valuation_USD_Millions))
print("Maximum Valuation_USD_Millions are =",np.max(Valuation_USD_Millions))
print("Median of Valuation_USD_Millions =",np.median(Valuation_USD_Millions))
print("Mean of Valuation_USD_Millions =",np.mean(Valuation_USD_Millions))
print("25 percentile of Valuation_USD_Millions =",np.percentile(Valuation_USD_Millions,25))
print("75 percentile of Valuation_USD_Millions =",np.percentile(Valuation_USD_Millions,75))
print("3 percentile of Valuation_USD_Millions =",np.percentile(Valuation_USD_Millions,3))

#Maths operations

print("Square of Valuation_USD_Millions =",np.square(Valuation_USD_Millions))
print("square root of Valuation_USD_Millions =",np.sqrt(Valuation_USD_Millions))
print("Power of Valuation_USD_Millions =",np.power(Valuation_USD_Millions,Valuation_USD_Millions))
print("Absolute of Valuation_USD_Millions =",np.abs(Valuation_USD_Millions))

# Perform basic arithmetic operations

Addition=Valuation_USD_Millions+Total_Funding_USD_Millions
Substraction=Valuation_USD_Millions-Total_Funding_USD_Millions
Multiplication=Valuation_USD_Millions*Total_Funding_USD_Millions
Dividing=Valuation_USD_Millions/Total_Funding_USD_Millions

print("Addition of funding round and number of investor =",Addition)
print("Subtraction of funding round and number of investor =",Substraction)
print("Multiplication of funding round and number of investor =",Multiplication)
print("Division of funding round and number of investor =",Dividing)

#Trigonometric Functions
InvestmentPie = (Valuation_USD_Millions/np.pi) +1
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
 
D2FundingandInvestor=np.array([Valuation_USD_Millions,Total_Funding_USD_Millions])
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
D2newarray=np.reshape(D2FundingandInvestor,(2, 25000))
print("after reshaping =",D2newarray)
print("Size of the reshaping array =",np.size(D2newarray))
print("Number of Dimension of array =",np.ndim(D2newarray))
print("Shape of the array =",np.shape(D2newarray))

