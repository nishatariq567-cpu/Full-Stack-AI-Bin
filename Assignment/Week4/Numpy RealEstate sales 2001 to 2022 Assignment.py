import numpy as np
Sale_Amount,Sales_Ratio=np.genfromtxt("Week4/Real_Estate_Sales_2001-2022_GL-Short.csv",delimiter=',',usecols=(6,7),dtype=None,unpack=True,skip_header=1,invalid_raise=False)
print(Sale_Amount)
print(Sales_Ratio)

#statistics operations

print("Average Sale_Amount =",np.average(Sale_Amount))
print("Minimum Sale_Amount =",np.min(Sale_Amount))
print("Maximum Sale_Amount =",np.max(Sale_Amount))
print("Median of Sale_Amount =",np.median(Sale_Amount))
print("Mean of the Sale_Amount =",np.mean(Sale_Amount))
print("25 percentile of Sale_Amount =",np.percentile(Sale_Amount,25))
print("75 percentile of Sale_Amount =",np.percentile(Sale_Amount,75))
print("3 percentile of Sale_Amount =",np.percentile(Sale_Amount,3))

print("Average of the Sales_Ratio =",np.average(Sales_Ratio))
print("Minimum Sales_Ratio are =",np.min(Sales_Ratio))
print("Maximum Sales_Ratio are =",np.max(Sales_Ratio))
print("Median of Sales_Ratio =",np.median(Sales_Ratio))
print("Mean of Sales_Ratio =",np.mean(Sales_Ratio))
print("25 percentile of Sales_Ratio =",np.percentile(Sales_Ratio,25))
print("75 percentile of Sales_Ratio =",np.percentile(Sales_Ratio,75))
print("3 percentile of Sales_Ratio =",np.percentile(Sales_Ratio,3))

#Maths operations

print("Square of number of Sales_Ratio =",np.square(Sales_Ratio))
print("square root of number of Sales_Ratio =",np.sqrt(Sales_Ratio))
print("Power of number of Sales_Ratio =",np.power(Sales_Ratio,Sales_Ratio))
print("Absolute of number of Sales_Ratio =",np.abs(Sales_Ratio))

# Perform basic arithmetic operations

Addition=Sales_Ratio+Sale_Amount
Substraction=Sales_Ratio-Sale_Amount
Multiplication=Sales_Ratio*Sale_Amount
Dividing=Sales_Ratio/Sale_Amount

print("Addition of funding round and number of investor =",Addition)
print("Subtraction of funding round and number of investor =",Substraction)
print("Multiplication of funding round and number of investor =",Multiplication)
print("Division of funding round and number of investor =",Dividing)

#Trigonometric Functions
InvestmentPie = (Sale_Amount/np.pi) +1
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
 
D2FundingandInvestor=np.array([Sale_Amount,Sales_Ratio])
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
D2newarray=np.reshape(D2FundingandInvestor,(2, 139))
print("after reshaping =",D2newarray)
print("Size of the reshaping array =",np.size(D2newarray))
print("Number of Dimension of array =",np.ndim(D2newarray))
print("Shape of the array =",np.shape(D2newarray))

