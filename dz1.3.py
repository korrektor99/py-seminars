#Напишите программу, которая принимает на вход координаты 
#точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
print("Введите X И Y по по очереди, с учетом того что они не должны быть равны 0")
x=float(input())
y=float(input())
if x>0 and y>0:
    print('точка находится в 1 четверти')
elif x<0 and y>0:
    print('2четверть')
elif  x>0 and y<0:
    print('4четверть')
elif  x<0 and y<0:
    print('3четверть')   