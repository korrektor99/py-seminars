#Напишите программу, которая принимает на вход 
#вещественное число и показывает сумму его цифр.
n = int(input("Введите число:"))
def  Sum(num):
    a = 0
    while(num > 0):
        c = num % 10
        a = a + c
        num = num//10
    return a
print(Sum(n))