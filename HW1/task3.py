from os import system
from math import factorial
system("cls")
'''
Условие:
В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. 
Какова вероятность того, что все извлеченные детали окрашены?
'''


def f_combination(n, k):
    return (factorial(n) / (factorial(k) * factorial(n-k)))


'''
    P(A)=m/n - общее количество исходов определяется кол-ом сочетаний из 15 возможных 3,
    а количество благоприятных исходов, что все детали окрашены из 9 возможных 3
'''
m = f_combination(9, 3)  # m = из "9" "3"
n = f_combination(15, 3)  # n = из "15" "3"
P = m / n
print(
    f'\n<<< Вероятность того, что все 3 детали окрашены = {round(P*100,3)}% >>>')