def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somado os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)






'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''



'''def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')
 for valor in num:
        print(f'{valor} ', end='')
    print('Fim')'''


'''contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'S soma de A + B = {s}')'''


#programa principal
'''soma(b=4, a=5)
soma(7, 2)'''

'''soma(8, 9)
soma(2, 1)
soma(4, 1)'''



'''a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)'''