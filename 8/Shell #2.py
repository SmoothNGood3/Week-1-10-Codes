import math
def newton(x, estimate):
    if abs (x-estimate ** 2) <= 0.000001:
            return estimate
    else:
        estimate = newton(x, (estimate + x/estimate)/2)
    return estimate  

def main():
    while True:
        x = (input("Enter a positive number or press the 'enter' key to quit: "))
        if x == "":    
                break
        x = float(x)
        print("Newtons estimate of the sqaure root of the number is: ", newton(x, x/2))
        print("The True value of the square root is: ", math.sqrt(x))
main()
