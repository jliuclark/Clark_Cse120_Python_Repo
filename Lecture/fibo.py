def fib_print(n): # Define function - write Fibonacci series up to n
    """Print a Fibonacci series up to n."""# Documentation string
    a = 0; b = 1; # set up base
    while b < n:  # condition  
        print(b, end=' '); c = a + b; a = b; b = c   
        
def fib_return(n): # Define function - write Fibonacci series up to n
    """Retunr a list containing a Fibonacci series up to n."""# Documentation string
    series = []#create an emply list for holding the series
    a = 0; b = 1; # set up base
    while b < n:  # condition  
        series.append(b); c = a + b; a = b; b = c
    return series       