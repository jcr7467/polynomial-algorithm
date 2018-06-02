# Implementation of Horner Method 
# for Polynomial Evaluation
 

def horner(poly, n, x):
 
    # Initialize result
    result = poly[0]  
  
    # Evaluate value of polynomial
    # using Horner's method
    for i in range(1, n):
 
        result = result*x + poly[i]
  
    return result
  

 
# Let us evaluate value of
# 2x^3 - 6x^2 + 2x - 1 for a certain x 
poly = [2, -6, 2, -1]
x = 5
n = len(poly)
 
print("The value of this polynomial when x =",x,'is', horner(poly, n, x))
