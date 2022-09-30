soma: int
x: int

x = int(input('Digite um número: '))
soma = 0

while x !=0:
    soma = soma + x
    x = int(input('Digite um número: '))

print( 'Soma vale: ', soma)