print("########################################")
print("          Calculadora Python            ")
print("########################################")


print(" tecla a opção desejada e aperte ENTER: ")
print("1 - SOMA")
print("2 - Subtração")
print("3 - Multiplicar")
print("4 - Dividir")
print("5 - Potenciação")
print("6 - Radiciação")
print("7 - Sair")

op = input("opção desejada: ")
op = int(op)

if(op == 5):
	print(" SAINDOOOOOOO... ")
else:
	a = input("Entre com o valor de a: ")
	a = int(a)
	b = input("Entre com o valor de b:" )
	b = int(b)
	if ( op == 1 ):
		print("A soma é: ", a + b)
	elif ( op ==2 ):
		print("A subtração é: ", a - b)
	elif ( op ==3 ):
		print("A Multiplicar é: ", a * b)
	elif ( op ==4 ):
		print("A Dividir é: ", a / b)
	elif ( op ==5 ):
		print("Potenciação é: ", a ** b)
	elif ( op ==6 ):
		print("Radiciação: ", a ** (1/b))
    elif ( op ==7 ):
        print(" SAINDOOOOOOO... ")
  

input()