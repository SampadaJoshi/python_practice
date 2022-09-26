import math as m   # import math library to call tan function and get pi constant
def polysum(n,s):  
    area = 0.25*n*s**2/m.tan(m.pi/n) # conmute area and store the value 
    perimeter = n*s                  # compute perimeter and store the value
    result = area + perimeter**2     # sum the area and square of the perimeter ,and store the value into 'result'
    return float('%.4f'%result)      # round the result to 4 decimal places, and return the result
