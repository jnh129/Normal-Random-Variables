"""
Random Number Generators
"""

import random
import math
from matplotlib import pyplot as plt

'''Method-1: Sum of Uniform Random Variables'''

def Method_1():
    data = [random.uniform(0,1) for i in range(12)]
    result = 0
    for element in data:
        result += element - 6
    return result

'''Method-2: Box-Muller Method'''

def Method_2():
    result = ""
    U1 = random.uniform(0,1)
    U2 = random.uniform(0,1)
    Z1 = math.sqrt(-2*math.log(U1))*math.cos(2*math.pi*U2)
    Z2 = math.sqrt(-2*math.log(U1))*math.sin(2*math.pi*U2)
    result += "Z1 = "+str(Z1)+", Z2 = "+str(Z2)
    return result

'''Method-3: Polar Method'''

def Method_3():
    result = ""
    S = 2
    while S > 1:
        U1 = random.uniform(0,1)
        U2 = random.uniform(0,1)
        V1 = 2*U1 - 1
        V2 = 2*U2 - 1
        S = V1**2 + V2**2
    Z1 = math.sqrt(-2*math.log(S)/S)*V1
    Z2 = math.sqrt(-2*math.log(S)/S)*V2
    result += "Z1 = "+str(Z1)+", Z2 = "+str(Z2)
    return result

'''Method-4: Inversion Method'''

def phiInverse(U):
    '''This is separated for organizational purposes'''
    w = math.sqrt(-2*math.log(U))
    a0 = 2.515517
    a1 = 0.802853
    a2 = 0.010328
    b0 = 1
    b1 = 1.432788
    b2 = 0.189269
    b3 = 0.001308

    numerator = a0 + a1*w + a2*(w**2)
    denomenator = b0 + b1*w + b2*(w**2) + b3*(w**3)

    result = -w + numerator/denomenator
    return result
    
    
def Method_4():
    result = 0
    U = random.uniform(0,1)
    if U <= .5:
        result = phiInverse(U)
    else:
        result = phiInverse(1-U)
    return result

'''Method-5: Acceptance-Rejection Method'''

def Method_5():
    Z = 0
    Y1 = 0
    Y2 = 0
    while Y2 < .5*(Y1-1)**2:
        U1 = random.uniform(0,1)
        U2 = random.uniform(0,1)
        Y1 = -math.log(U1)
        Y2 = -math.log(U2)
    Z = Y1
    U3 = random.uniform(0,1)
    if U3 <= .5:
        Z = abs(Z)
    else:
        Z = -abs(Z)
    return Z

'''Method-6: Using Generalized Exponential Distribution'''

def Method_6():
    U = random.uniform(0,1)
    X = -math.log(1-U**(0.0775))
    Z = (math.log(X)-1.0821)/0.3807
    return Z

'''Method-7: Bol'shev Formula'''

def Method_7():
    data = [random.uniform(0,1) for i in range(5)]
    data = [math.sqrt(3)*(2*elm - 1) for elm in data]
    X = sum(data)
    X = X/math.sqrt(5)
    Z = X-.01*(3*X-X**3)
    return Z

'''Method-8: Inversion Method'''

def Method_8():
    U = random.uniform(0,1)
    Z = (1/1.702)*(-math.log(1/U-1))
    return Z

'''Method-9: Proposed Method'''

def Method_9():
    U = random.uniform(0,1)
    X1 = math.tanh(-31.35694 + 28.77154*U)
    X2 = math.tanh(-2.57136 - 31.16364*U)
    X3 = math.tanh(3.94963 - 1.66888*U)
    X4 = math.tanh(2.31229 + 1.84289*U)
    Z = .46615 + 90.72192*X1 - 89.36967*X2 - 96.55499*X3 + 97.36346*X4
    return Z


def main():
    example = [Method_1() for i in range(1000)]
    plt.hist(example)
    
if __name__ == "__main__":
    main()
