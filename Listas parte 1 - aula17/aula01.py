num = [2, 4, 3, 2, 3, 10]
num[0] = 4 #4 vai pra posição 0
num.append(10) #adiciona o 10
num.insert(3, 20) #coloca o número 20 na posição 3
print(num)

num.pop(1) #tira o elemento 1, que no caso é o num 4
print(num)

num.sort() #ordem normal
print(num)
num.sort(reverse= True)#ordem do maior pro menor
print(num)
print(f'Essa lista tem {len(num)} elementos')


