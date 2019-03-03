#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    t1 = 0
    t2 = 0
    t3 = 0

    for i in range(0, len(input_string)):
    	if input_string[i] == '{':
    		t1+=1
    	if input_string[i] == '}':
    		t1-=1
    	if input_string[i] == '(':
    		t2+=1
    	if input_string[i] == ')':
    		t2-=1
    	if input_string[i] == '[':
    		t3+=1
    	if input_string[i] == ']':
    		t3-=1

    if t1 == 0 and t2 == 0 and t3 == 0:
    	return True
    else:
    	return False

    raise NotImplementedError
