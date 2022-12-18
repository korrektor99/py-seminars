#Напишите программу, которая найдёт произведение 
#пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
numbers=[2,3,4,5,6]
result=[0,0,0]
k=0
for i in numbers:
    k+=1
#print (k)

for i in numbers:
    while (i<=k):
        for i in result:
            i=numbers[i]*numbers[k-1]
        print (i)
        k-=1
if (k%2>0):
    result.append(numbers[k-1]*numbers[k-1])
print (result[k])
