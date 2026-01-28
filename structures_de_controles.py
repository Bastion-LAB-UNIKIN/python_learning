
def signe(x):
    if x > 0:
        print(x , 'positif')
    elif x == 0:
        print(x,'nul')
    else:
        print(x,'négatif')
signe(-5)
for i in range(10,-10,-3):
    signe(i)

def fibonacci(n):
    x=0
    y=1
    fib=[x]
    while y < n:
        print(x)
        x,y =y,x+y
        fib.append(x)
    return fib
print(fibonacci(1000))

