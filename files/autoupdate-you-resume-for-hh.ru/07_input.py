Напишите программу, принимающую на вход целое число, которая выводит True, 
если переданное значение попадает в интервал (−15,12]∪(14,17)∪[19,+∞) и 
False в противном случае (регистр символов имеет значение).

Обратите внимание на разные скобки, используемые для обозначения интервалов. 
В задании используются полуоткрытые и открытые интервалы.

# put your python code here
X = int(input())
if X<=12 and X>-15:
    print('True')
elif X>14 and X<17:
    print('True')
elif X>=19:
    print('True')
else:
    print('False')
