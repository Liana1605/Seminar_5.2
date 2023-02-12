#Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
#максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
#максимальные – на минимальные.
#Input: 5 -> 1 3 3 3 4
#Output: 1 3 3 3 1

from random import randint
grades = []

count = int(input('Введите число: '))

for _ in range(count):
    grades.append(randint(1, 5))
print(grades)

for i in range(len(grades)):
    if grades[i] == max(grades):
        grades[i] = min(grades)

print(grades)


