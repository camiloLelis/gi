import datetime
import os
import re  # modulo de regex
os.system('clear')
nasc= input("suA data de nascimento ?(exemplo : 1985/3/26)") # digita a data conforme exemplo, primeiro o ano ,porem tenho que fazer validação, e tratamento de erros
result= re.split(r'/',nasc) #aqui o método split do modulo re , tem o 1º parametro '/' que diz que a cada sinal deste parametro ele irá dividir o segundo parametro , que é variavel nasc, 
nasceu= datetime.datetime(int(result[0]), int(result[1]), int(result[2])) # aqui joga o que foi dividido no metodo split
print (result)
print (nasceu)
data= datetime.datetime.now()# aqui joga o return do metodo datetime.datetime.now() que é o dia mes e ano e horas atual para variavel data
idade= data-nasceu #aqui divide a data atual que1 tá na variavel data pelo variavel que mostra o dia que nasceu, e joga na variavel idade
idcerta=int(re.sub(r'days,...............','', str(idade))) #usei o metodo re.sub() que substitui o 1º texto do 1ºparametro pelo 2ºsegundo , no que estiver no 3ºparametro
print(str(idcerta) + " dias que você viveu até hoje ")
anos= int(int(idcerta) / 365.25) # transforma a variavel idcerta de string em inteiro e divide pelo numeros de dias de um ano,coloquei um int a mais para delimitar o numero de casas decimais, ou seja não dar numeros quebrados,365,25 devido a ano bisexto, mais não pensei direito 
print ("você tem " + str(anos) + " anos de vida")
#print(idade)
