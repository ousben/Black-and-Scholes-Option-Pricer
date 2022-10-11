import numpy as np
from scipy.stats import norm

def blackAndScholes():
    r = float(input("What is the interest rate ? "))
    S = int(input("What is the value of the underlying asset ? "))
    K = int(input("What is the Strike Price ? "))
    T = float(input("What is the duration of the option ? (percentage of a year) "))
    sigma = float(input("What is the Volatility ? (between 0 and 1) "))
    type = input("Is it a Call or a Put ?(only 'Call' and 'Put' accepted) ")

    d1 = (np.log(S/K) + (r + sigma**2/2)* T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "Call":
            price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "Put":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Some parameters haven't been confirmed. Please resolve")

print("According to the program, the Option price is: ", blackAndScholes())