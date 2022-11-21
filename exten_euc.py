# Recursion Based
def gcd(a, b):
    global x, y
    if (b == 0):
        x=1
        y=0
        return a 
    greatest_common_divisor = gcd(b, a % b)
    x1 = x 
    y1 = y 
    
    x = y1
    y = x1 - (a // b) * y1
    return greatest_common_divisor
    
print(gcd(5, 11))
