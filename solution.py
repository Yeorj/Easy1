#!/usr/bin/python

import sys

storedUsers= open('names', 'a')

name = raw_input('Hi, please enter your name: ')
age = raw_input('How old are you?: ')
username = raw_input('Please enter your username: ')

sys.stdout.write('your name is ' + name + ', you are ' + str(age) + ' years old, and your username is ' + str(username) + '\n')

storedUsers.write(name + '\t' + age + '\t'+username+'\n')

storedUsers.close()
