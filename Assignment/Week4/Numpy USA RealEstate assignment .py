import numpy as np

Brokered_by,Price,Bed,Bath=np.genfromtxt("Week4/RealEstate-USA.csv",delimiter=",",usecols=(0,2,3,4),dtype=None,unpack=True,skip_header=1)
print(Brokered_by)
print(Price)
print(Bed)
print(Bath)


print("Average of the price is here =",np.average(Price))
print("Standard Deviation of the Price =",np.std(Price))
print("Median of the Property price",np.median(Price))
print("Minimum price of property =",np.min(Price))
print("Maximum price of property =",np.max(Price))
print("Percentile 25- =",np.percentile(Price,25))
print("Percentile 75- =",np.percentile(Price,75))
print("Percentile 3- =",np.percentile(Price,3))

print("Square of the price =",np.square(Price))
print("Squareroot of the price =",np.sqrt(Price))
print("Power of the price =",np.power(Price,Price))
print("Convert negative to positive values =",np.abs(Bed))

pieprice=(Price/np.pi)+1
print("SIne value of PiPrice =",np.sin(pieprice))
print("Cosine value of Piprice =",np.cos(pieprice))
print("Tangent value of Piprice =",np.tan(pieprice))
print("Exponential Value of Piprice =",np.exp(pieprice))
print("Logarithm value of Piprice =", np.log(pieprice))
print("10 Logarithm value of Piprice =",np.log10(pieprice))

print("Hyperbolic SIne of Piprice =",np.sinh(pieprice))
print("Hyperbolic Cosine of Piprice =",np.cosh(pieprice))
print("Hyperbolic Tangent of Piprice =",np.tanh(pieprice))
print("Inverse Hyperbolic Sine of Piprice =",np.arcsinh)
print("Inverse Hyperbolic Cosine of Piprice =",np.arccosh(pieprice))

long = np.array([74.3587, 73.0479, 72.8777, 67.0011, 71.5249])
lat = np.array([31.5204, 33.6844, 19.0760, 24.8607, 34.0151])

D2longLat=np.array([long,lat])
print("Long + Lat 2 Dimensional array =",D2longLat)
print("Find the Dimensions of array =",D2longLat.ndim)
print("Check Total number of elements in array =",D2longLat.size)
print('gives size of array in each dimension =',D2longLat.shape)
print("Data type of array =",D2longLat.dtype)

# Splicing array
d2longlatslice=D2longLat[0:1:1,1:5:1]
print("splicing of 2 Dimensional array =",d2longlatslice)
d2longlatslice2=D2longLat[:1,3:4:1]
print("Second splicing of 2 Dimensional array =",d2longlatslice2)

# Indexing array
d2longlatonlyitem=d2longlatslice[0,1]
print("Only Single value print by give index =",d2longlatonlyitem)
d2longlatonlyitem2=d2longlatslice[0,2]
print("Second Only Single value print by give index =",d2longlatonlyitem2)

Newdata=[1,2,3,4,5,6,7,8,9,10]
mydata=np.reshape(Newdata,(2,5))
print(mydata)
print("Size of the array =",mydata.size)
print("Number of dimesnions in array =",mydata.ndim)
print("Shape of the array =",mydata.shape)
print("Data type of the array =",mydata.dtype)


