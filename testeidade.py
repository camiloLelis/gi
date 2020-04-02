# !/usr/bin/python
# Encoding: UTF-8
# Calcula quantos dias de vida uma pessoa teve dado o dia, mes e ano de seu nascimento.
# Autor: David Wilian Oliveira de Sousa - adaptado de Ewerton Tiago de Azevedo
# Data: 26-10-2011

#configurações iniciais
import datetime

hoje=datetime.date.today()

anoAtual= hoje.strftime("%Y")

meses = { 'janeiro' : 1 , 'fevereiro' : 2 , 'marco' : 3 , 'abril' : 4 , 'maio' : 5 , 'junho' : 6 , 'julho' : 7 , 'agosto' : 8 , 'setembro' : 9 , 'outubro' : 10 , 'novembro' : 11 , 'dezembro' : 12 }
meses1 = {  1 : 'janeiro' , 2 : 'fevereiro' , 3 : 'marco', 4 : 'abril' , 5 : 'maio' , 6 : 'junho', 7 : 'julho', 8 : 'agosto' , 9 : 'setembro' , 10 : 'outubro' , 11 : 'novembro' , 12 : 'dezembro' }

bissexto = False

#dados forncecidos

coletandodados = True
nome= input ("qual filho do camilo vocẽ é ?")
while coletandodados == True:
    dia= input("Digite o dia do seu nascimento \nExemplo: 31 \n" )

    mes= input("\n Digite o mes do seu nascimento (numero ou por extenso entre aspas)\nExemplos: 12 , 'agosto', 'marco'")
    print (mes)
# #Testa se o mês existe
    if type(mes) is str:
        if meses.has_key(mes) == True:
            print mes in meses
            mes= meses[mes]
            print mes
        elif mes in meses == False:
            print "nome de mes invalido. Tente novamente."
            continue
# #Testa se o dia é compatível com o mês
    if type(mes) is int:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes ==12:
            if dia > 31:
                print "Esse mes possui somente 31 dias."
                continue
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia > 30:
                print "Esse mes possui somente 30 dias."
                continue
        if mes == 2:
            if dia == 29:
                bissexto = True
                print "Sera verificado se o ano e bissexto"
            elif dia > 29:
                print "Fevereiro tem no maximo 29 dias!"
                continue

    ano=input("\n Digite o ano do seu nascimento (a partir de 1583) \n Exemplo: 1990 \n ")
    if ano < 1583:
        print "Nao e possivel calcular para antes de 1583, o calendario que usamos hoje nao existia."
        continue

# #Verifica se o ano é bissexto
    if bissexto == True:
        if ano % 100 == 0:
            if ano % 400 != 0:
                print "Esse ano nao e bissexto, portanto nao possui 29 de fevereiro."
                continue
        elif ano % 100 != 0:
            if ano % 4 != 0:
                print "Esse ano nao e bissexto, portanto nao possui 29 de fevereiro."
                continue

        print "Esse ano e bissexto."

#Verifica se a pessoa "nasceu no futuro":
    if ano > anoAtual:
        print "Voce nasceu no futuro?"
        continue

    print nome" Sua data de nascimento e: ", dia, "de", meses1[mes], "de", ano,  "\n"
    confirma = raw_input("Confirma sua data de nascimento (s/n)? ")
    if confirma == 's':
        coletandodados = False

# Cálculos
# fica bem facil usando o modulo datetime

niver = datetime.date(ano, mes, dia)

idadeemdias = hoje - niver

print "Sua idade em dias e ", idadeemdias.days, "dias."