print ('-----'*10)
print ('RODÍZIO E CARROS EM SÃO PAULO')
print ('-----'*10)
print ('SAIBA QUE DIA O SEU VEÍCULO PODE RODAR')
print ('-----'*10)


n_placa = int(input('Digite o ultimo numero da placa do seu veículo --> '))
print ('---=-=-'*10)
if n_placa == 1  or  n_placa == 2:
  print('Segunda-Feira é o seu dia de Rodízio, obrigado, volte sempre!')
  print ('-=-=-=-='*10)
elif n_placa == 3 or n_placa ==  4:
  print('Terça-Feira é o seu dia de Rodízio, obrigado, volte sempre!')
elif n_placa == 5 or n_placa == 6:
  print('Quarta-Feira é o seu dia de Rodízio, obrigado, volte sempre!')
elif n_placa == 7 or n_placa ==8:
  print('Quinta-Feira é o seu dia de Rodízio, obrigado, volte sempre!')
elif n_placa == 9 or n_placa ==0:
  print('Sexta-Feira é o seu dia de Rodízio, obrigado, volte sempre!')
else:
  print('Ultimo número de placa NÃO correspondente, Desculpe !')
print ('-=-=-=-='*10)
