def estacoes_do_ano(dia, mes):
    if dia >= 1 and dia <= 31 and mes == 2:
        return ('Voce nasceu no Verão !')
    elif dia >= 1 and dia <= 19 and mes == 3:
        return ('Voce nasceu no Verão !')
    elif dia >= 20 and dia <= 31 and mes == 3 or dia >= 1 and dia <= 30 and mes == 4:
        return ('Você nasceu no outono !')
    elif dia >= 1 and dia <= 31 and mes == 5:
        return ('Você nasceu no outono !')
    elif dia >= 1 and dia <= 20 and mes == 6:
        return ('Você nasceu no outono !')
    elif dia >= 21 and dia <= 30 and mes == 6 or dia >= 1 and dia <= 31 and mes == 7:
        return ("Você nasceu no inverno !")
    elif dia >= 1 and dia <= 31 and mes == 8:
        return ("Você nasceu no inverno !")
    elif dia >= 1 and dia <= 22 and mes == 9:
        return ("Você nasceu no inverno !")
    elif dia >= 23 and dia <= 30 and mes == 9 or dia >= 1 and dia <= 31 and mes == 10:
        return ("Você nasceu na primavera !")
    elif dia >= 1 and dia <= 30 and mes == 11:
        return ("Você nasceu na primavera !")
    elif dia >= 1 and dia <= 21 and mes == 12:
        return ("Você nasceu na primavera !")
    elif dia >= 22 and dia <= 31 and mes == 12 or dia >= 1 and dia <= 31 and mes == 1:
        return ('Voce nasceu no Verão !')
    else:
        print('Invalido')
