#Verfifica estação do ano

print('\n\t\t --- Estação do Ano --- \n\t\t')

#Entradas
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))

#Processamento

if dia >= 1 and dia <= 31 and mes == 2:
    print('Voce nasceu no Verão !')
elif dia >= 1 and dia <= 19 and mes == 3:
    print('Voce nasceu no Verão !')
elif dia >= 20 and dia <= 31 and mes == 3 or dia >= 1 and dia <= 30 and  mes == 4:
    print('Você nasceu no outono')
elif dia >= 1 and dia <= 31 and mes == 5:
    print('Você nasceu no outono')
elif dia >= 1 and dia <= 20 and mes == 6:
    print('Você nasceu no outono')
elif dia >= 21 and dia <= 30 and mes == 6 or dia >= 1 and dia <= 31 and mes == 7:
    print("Você nasceu no inverno")
elif dia >= 1 and dia <= 31 and mes == 8:
    print("Você nasceu no inverno")
elif dia >= 1 and dia <= 22 and mes == 9:
    print("Você nasceu no inverno")
elif dia >= 23 and dia <= 30 and mes == 9 or dia >= 1 and dia <= 31 and mes == 10:
    print("Você nasceu na primavera")
elif dia >= 1 and dia <= 30 and mes == 11:
    print("Você nasceu na primavera")
elif dia >= 1 and dia <= 21 and mes == 12:
    print("Você nasceu na primavera")
elif dia >= 22 and dia <= 31 and mes == 12 or dia >= 1 and dia <= 31 and mes == 1:
        print('Voce nasceu no Verão !')
else:
    print('Invalido')

