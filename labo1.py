def factorial(n):
    r=1
    for i in range(1,n+1):
        r *= i
    return r

n = int(input("Ingrese el numero del factorial: ")) 
print(f"El factorial es {factorial(n)}")