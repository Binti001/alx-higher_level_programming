#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number < 0:
    number1 = number * -1
if number > 0:
    number1 = number
num = number1 % 10
num = int(num)
if num > 5:
    print("Last digit of {} is {} and is greater than 5". format(number, num))
if num == 0:
    print("Last digit of {} is {} and is 0". format(number, num))
if num < 6 and num != 0:
    print("Last digit of {} is {} and is less than \
 6 and not 0". format(number, num))
