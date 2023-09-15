#imc é índice de massa corporal, medida internacional usada para calcular se uma pessoa está no peso ideal
# IMC = Peso/(altura)2
#input de informação de peso e altura


#terminal de dados do paciente
peso = float(input("Seu peso: "))
altura = float(input("Sua altura: "))

#calculo do IMC
imc = peso/(altura * altura) #elevado à 2

print("Seu IMC: {0}".format(imc)) #.format() especifica o valor e encaixa no texto.

#medidas de saude e imc
if imc < 16:
    print("Você tem magreza grave")
elif imc >= 16 and imc <17:
    print("Você tem magreza moderada")
elif imc >= 17 and imc < 18.5:
    print("Você tem magreza leve")
elif imc >= 18.5 and imc <25:
    print("você está saudável")
elif imc >= 25 and imc <30:
    print("você está com sobrepeso")
elif imc >= 30 and imc < 35:
    print("você está com obesidade")
elif imc >= 35 and imc < 40:
    print("você está com obesidade severa")
elif imc >= 40:
    print("você está com obesidade mórbida")