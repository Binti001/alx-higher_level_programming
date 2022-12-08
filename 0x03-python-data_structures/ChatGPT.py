#!/bin/usr/python3
import datetime



#ask user to input their birthday

birthday = input('Please enter your birthday in the format mm/dd/yyyy: ')



#convert the birthday to a date object

birthdate = datetime.datetime.strptime(birthday, '%m/%d/%Y')



#find the difference between today and the birthday

today = datetime.datetime.now()

difference = today - birthdate



#print the result

print('You have been alive for', difference.days, 'days!')
