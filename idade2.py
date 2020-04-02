import datetime
import os
import re  # modulo de regex
os.system('clear')
nasc= input("suA data de nascimento ?(exemplo : 1985/3/26)") # digita a data conforme exemplo, primeiro o ano ,porem tenho que fazer validação, e tratamento de erros
result= re.split(r'/',nasc) # aqui o método split do modulo re , tem o 1º parametro '/' que diz que a cada sinal deste parametro ele irá dividir o segundo parametro , que é variavel nasc, 
nasceu= datetime.datetime(int(result[0]), int(result[1]), int(result[2])) # aqui joga o que foi dividido no metodo split
print (result)
print (nasceu)
data= datetime.datetime.now()# aqui joga o return do metodo datetime.datetime.now() que é o dia mes e ano e horas atual para variavel data
idade= data-nasceu #aqui divide a data atual que tá na variavel data pelo variavel que mostra o dia que nasceu, e joga na variavel idade
print(idade)
