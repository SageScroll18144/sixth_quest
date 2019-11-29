import random as rd
import math as m

#Valor arbitrário para a questão
R = 1

#Valor arbitrário para o algoritmo(obs.: quanto maior melhor o resultado)
PONTOS_LENGTH = 100000 

def f(x, y):
    if ((x <= R) and (y <= (x*x/R))):
        return 1
    else:
        return 0

def main():
    somatoria = 0

    for i in range(PONTOS_LENGTH):      
        #Escolhe valores entre 0 e 1
        x = rd.random()
        y = rd.random()
        
        somatoria += f(x, y)

    theta = 90 * somatoria/PONTOS_LENGTH
    
    #print(m.ceil(m.cos(theta))/m.ceil(m.sin(theta)))
    print(theta)
if __name__ == "__main__":
    main()
