contador = 0
menor = maior = 0
while contador <= 5:
    numero = int(input(f'digite o {contador} numero: '))
    contador += 1
    if contador == 1:
        maior = numero 
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print (f'O maior valor é o {maior}.')   
print (f'O menor numero é o {menor}.')    


# atualMaiorNumero = int(input('Digite um numero: '))
# for contNumero in range(1, 5, 1):
#     novoNumero = int(input("Digite um numero inteiro: "))
#     if novoNumero > atualMaiorNumero:
#         atualMaiorNumero = novoNumero
       
# print("Maior numero digitado = ", atualMaiorNumero)


ana = 150
felisberto = 110
contador = 0
print('\nDesafio Felisberto/Ana')
while felisberto < ana:
    contador += 1
    felisberto += 3
    ana += 2
print (f'\nSerão necessários {contador} anos!')


#exercicio 2

somapeso = contador = media = 0
contadorpeso = 0
print('='*20)
print ('\033[1;31mFlag de parada [ 0 ]\033[m')
while True:
    contador += 1
    numero = float (input(f'\nDigite {contador} peso: '))
    somapeso += numero 
    if numero == 0:
        break
    if numero > 800:
        contadorpeso +=1
media = somapeso/(contador-1)
print ('=-'*20)
print(f'{contador-1} pratos foram pesados, com uma media igual a {media:.2f}')
print (f'Com {contadorpeso} pratos acima de 800 gramas')
      









