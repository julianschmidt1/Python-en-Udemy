class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1=operando1
        self.operando2=operando2
    #Atributo suma     
    def sumar(self):
        return self.operando1+self.operando2
    #Atributo resta
    def restar(self):
        return self.operando1-self.operando2
    #Atributo multiplicacion
    def multiplicar(self):
        return self.operando1*self.operando2
    #Atributo division
    def dividir(self):
        return self.operando1%self.operando2
    
#Objeto Suma
aritmetica=Aritmetica(2, 4)
print("Resultado de la suma: ",aritmetica.sumar())

#Objeto Resta
aritmetica=Aritmetica(10, 7)
print("Resultado de la resta: ",aritmetica.restar())

#Objeto Multiplicar
aritmetica=Aritmetica(5, 2)
print("Resultado de la multiplicacion: ",aritmetica.multiplicar())

#Objeto Dividir
aritmetica=Aritmetica(10, 2)
print("Resultado de la division: ",aritmetica.dividir())