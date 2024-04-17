
def sumatoria1(value):  #no recursiva
    resultado = 0
    while value > 0:
        resultado = resultado + value 
        value -= 1
    return resultado
resultado = sumatoria1(7)
print("sumatoria no recursiva ",resultado)

def sumatoria2(value):  # recursiva
    if value == 1:
        return 1
    return value + sumatoria2(value - 1)
resultado = sumatoria2(6)
print("sumatoria recursiva ",resultado)





def factorial(value):    #no recursiva
    resultado = 1
    for i in range(1,value+1):
        resultado *= i
    return resultado

resultado = factorial(4)
print("factorial no recursivo ",resultado)


def factorial2(value):    # recursiva
    if value in (0,1):
        return 1
    return value * factorial(value-1)

resultado = factorial2(3)
print("factorial no recursivo ",resultado)





def fibonacci(value):    # no recursiva
    if value < 2 : 
        return value
    values = [0,1]

    for _ in range(value - 1):
        values.append(values[-1] + values[-2])

    return values[value]

resultado = fibonacci(13)
print("fibonacci no recursivo ",resultado)

def fibonacci2(value):     # recursiva
    resultado = 0
    for i in range(value):
        if i < 2:   
            resultado = 1   
        else:
            resultado = resultado + fibonacci(i-1)  
    return resultado
    

resultado = fibonacci2(4)
print("fibonacci recursivo ",resultado)


def fibonacci3(value):     # de Magui
    anterior, resultado = 0,1
    for _ in range(value-1):
        anterior, resultado = resultado, anterior + resultado
    return resultado

resultado = fibonacci3(13)
print("fibonacci de magui ",resultado)