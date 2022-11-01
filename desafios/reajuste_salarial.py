# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
salario = int(input()) 
percentual_de_reajuste = 0
reajuste_ganho = 0
novo_salario = 0

if (salario>=0 and salario<=600):
  percentual_de_reajuste = 0.17

elif (salario > 600 and salario<=900):
  percentual_de_reajuste = 0.13

elif (salario > 900 and salario<=1500):
  percentual_de_reajuste = 0.12

elif (salario > 1500 and salario<=2000):
  percentual_de_reajuste = 0.10

else: 
  percentual_de_reajuste = 0.05
  
  
reajuste_ganho = percentual_de_reajuste * salario

novo_salario = f'{(salario + reajuste_ganho):.2f}'
novo_salario = novo_salario.replace('.',',')

reajuste_ganho = f'{(percentual_de_reajuste * salario):.2f}'
reajuste_ganho = reajuste_ganho.replace('.',',')

percentual_de_reajuste = int(percentual_de_reajuste * 100)

print(f"Novo salario: {novo_salario} Reajuste ganho: {reajuste_ganho} Em percentual: {percentual_de_reajuste} %")
