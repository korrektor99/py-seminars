#Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
print('введите х1')
x1=float(input())
print('введите y1')
y1=float(input())
print('введите х2')
x2=float(input())
print('введите y2')
y2=float(input())
import math
distanse=math.sqrt((x1-x2)**2+(y1-y2)**2)
print(distanse)