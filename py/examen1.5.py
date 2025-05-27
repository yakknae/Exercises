def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * (factorial(n-1))
    
num = factorial(5)
print(f"El factorial de 5 es: {num}")