from numeros_identicos_exception import NumerosIdenticosException

resultado=None

try:
    a=int(input("Ingrese el primer valor: "))
    b=int(input("Ingrese el segundo valor : "))
    if a==b:
        raise NumerosIdenticosException("numeros iguales")
    resultado=a/b
#except ValueError as e:
#    print("Error ValueError")
#    print(type(e))
except ZeroDivisionError as e:
    print("Error ZeroDivision")
    print(type(e))
except TypeError as e:
    print("Error TypeError")
    print(type(e))
except Exception as e:
    print("Error exception generica")
    print(type(e))
else:
    print("Tamo libre de exsepshooons")
finally:
    print("No más excepciones")
    
print("Resultado: ",resultado)
print("Se sigue")