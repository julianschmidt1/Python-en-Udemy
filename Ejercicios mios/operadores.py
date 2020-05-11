class Operadores:
    def __init__(self):
        self.num1=int(input("Ingrese el primer numero: "))
        self.num2=int(input("Ingrese el segundo numero: "))
        
    def suma(self):
        suma= self.num1+self.num2
        print("La suma es: ",suma)

    def resta(self):
        resta= self.num1-self.num2
        print("La resta es: ",resta)
        
    def multi(self):
        mult= self.num1*self.num2
        print("La  es: ",mult)

    def div(self):
        div= self.num1/self.num2
        print("La  es: ",div)

op=Operadores()
op.suma()
op.resta()
op.multi()
op.div()