# # Задача 1-1
# # Ввести два числа x и y. Напечатать сумму и произведение этих чисел (оператор + и *)
# # num1 = int(input('Введите число №1: '))
# # num2 = int(input('Введите число №2: '))
# # print("Сумма чисел №1 и №2 = ", num1+num2)
# # print("Произведение чисел №1 и №2 = ", num1*num
#
# # Задача 1-2
# # Ввести два числа x и y. Напечатать наибольшее из чисел x+y, x-y, x*y, x/y, x//y,
# # num1=int(input('Введите число №1: '))
# # num2=int(input('Введите число №2: '))
# # sum=num1+num2
# # sub=num1-num2
# # mul=num1*num2
# # div=num1/num2
# # div_int=num1//num2
# # if sum>sub and sum>mul and sum>div and sum>div_int:
# #     print('Наибольшее выражение 2 чисел - сумма = ', sum)
# # elif sub > sum and sub > mul and sub > div and sub > div_int:
# #         print('Наибольшее выражение 2 чисел - разность =', sub)
# # elif mul > sum and mul > sub and mul > div and mul > div_int:
# #         print('Наибольшее выражение 2 чисел - произведение =', mul)
# # elif div > sum and div > sub and div > mul and div > div_int:
# #         print('Наибольшее выражение 2 чисел - деление =', div)
# # else:
# #     print('Наибольшее выражение 2 чисел - целочисленное деление =', div_int)
#
#
# # Задача 1-3
# # Ввести два числа x и y. Напечатать второе по величине из чисел x+y, x-y, x*y, x/y, x//y,
# num1 = int(input('Введите число №1: ' ))
# num2 = int(input('Введите число №2: ' ))
# summ = num1 + num2
# sub = num1 - num2
# mul = num1 * num2
# div = num1 / num2
# div_int = num1 // num2
# if summ > sub and summ > mul and summ > div and summ > div_int:
#     x=summ
#     print('Наибольшее выражение 2 чисел - сумма = ', summ)
# elif sub > summ and sub > mul and sub > div and sub > div_int:
#     x=sub
#     print('Наибольшее выражение 2 чисел - разность =', sub)
# elif mul > summ and mul > sub and mul > div and mul > div_int:
#     x=mul
#     print('Наибольшее выражение 2 чисел - произведение =', mul)
# elif div > summ and div > sub and div > mul and div > div_int:
#     x=div
#     print('Наибольшее выражение 2 чисел - деление =', div)
# else:
#     x=div_int
#     print('Наибольшее выражение 2 чисел - целочисленное деление =', div_int)
# print('x =', x)
#
# if x==summ:
#     if sub > summ and sub > mul and sub > div and sub > div_int:
#         y = sub
#         print('Наибольшее второе выражение 2 чисел - разность =', sub)
#     elif mul > summ and mul > sub and mul > div and mul > div_int:
#         y = mul
#         print('Наибольшее второе выражение 2 чисел - произведение =', mul)
#     elif div > summ and div > sub and div > mul and div > div_int:
#         y = div
#         print('Наибольшее второе выражение 2 чисел - деление =', div)
#     else:
#         y = div_int
#         print('Наибольшее второе выражение 2 чисел - целочисленное деление =', div_int)
#     print('y =', y)
# elif x==sub:
#     if summ > mul and summ > div and summ > div_int:
#         y = sub
#         print('Наибольшее второе выражение 2 чисел - разность =', sub)
#     elif mul > summ and mul > div and mul > div_int:
#         y = mul
#         print('Наибольшее второе выражение 2 чисел - произведение =', mul)
#     elif div > summ and div > mul and div > div_int:
#         y = div
#         print('Наибольшее второе выражение 2 чисел - деление =', div)
#     else:
#         y = div_int
#         print('Наибольшее второе выражение 2 чисел - целочисленное деление =', div_int)
#     print('y =', y)
# if x==mul:
#     if summ > sub and summ > div and summ > div_int:
#         y = summ
#         print('Наибольшее второе выражение 2 чисел - сумма = ', summ)
#     elif sub > summ and sub > div and sub > div_int:
#         y = sub
#         print('Наибольшее второе выражение 2 чисел - разность =', sub)
#     elif div > summ and div > sub and div > div_int:
#         y = div
#         print('Наибольшее второе выражение 2 чисел - деление =', div)
#     else:
#         y = div_int
#         print('Наибольшее второе выражение 2 чисел - целочисленное деление =', div_int)
#     print('y =', y)
#
# if x == div:
#     if summ > sub and summ > mul and summ > div_int:
#         y = summ
#         print('Наибольшее второе выражение 2 чисел - сумма = ', summ)
#     elif sub > summ and sub > mul and sub > div_int:
#         y = sub
#         print('Наибольшее второе выражение 2 чисел - разность =', sub)
#     elif mul > summ and mul > sub and mul > div_int:
#         y = mul
#         print('Наибольшее второе выражение 2 чисел - произведение =', mul)
#     else:
#         y = div_int
#         print('Наибольшее второе выражение 2 чисел - целочисленное деление =', div_int)
#     print('y =', y)

