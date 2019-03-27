FibArray = [0,1]

def fibonacci(n):
  if n < 0:
    print ("Incorrect Input")
  elif n + 1 <= len(FibArray):
    return FibArray[n]
  else:
    temp_fib = fibonacci(n-1) + fibonacci(n-2)
    FibArray.append(temp_fib)
    return temp_fib

print (fibonacci(50))