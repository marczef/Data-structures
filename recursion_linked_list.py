#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Node:

    def __init__(self, data, next=None):
        self.data=data
        self.next = next

def nil():
    return Node(None)

def create():
    return nil()

def cons(list, el):
    return Node(el,list)

def first(list):
    return list.data

def rest(list):
    return list.next

def length(list, counter=0):

    if list.next is None:
        return counter
    else:
        counter+=1
        return length(remove(list), counter)

def show(list, string='['):


    if list.next is None:
        string + ']'
        print(string)
    else:
        string += str(first(list)) + '\n'
        return show(rest(list), string)

def destroy(list):
    list.data = None
    list.next = None


def is_empty(list):
    if list.data==None and list.next==None:
        return True
    else:
        return False

def add_end(el, list):
    if is_empty(list):
        return cons(list, el)
    else:
        first_el = first(list)
        rest_lst = rest(list)
        recreated_lst = add_end(el, rest_lst)
        return cons(recreated_lst, first_el)

def remove(list):
    return rest(list)

def pop(list):
    if is_empty(list.next):
        return create()
    else:
        first_el = first(list)
        rest_lst = rest(list)
        recreated_lst = pop(rest_lst)
        return cons(recreated_lst, first_el)

def take(list, nr):
    if length(list)<=nr:
        return list
    else:
        return take(pop(list), nr)

def drop(list, nr):
    if length(list)==nr:
        return list
    else:
        return drop(remove(list), nr+1)




def main():

    list=create()
    list=cons(list, ('AGH', 'Kraków', 1919))
    list = cons(list, ('UJ', 'Kraków', 1364))
    list = cons(list, ('PW', 'Warszawa', 1915))
    list = cons(list, ('UW', 'Warszawa', 1915))
    list = cons(list, ('UP', 'Poznań', 1919))
    list = cons(list, ('PG', 'Gdańsk', 1945))
    show(list)

    list=cons(list, 'cos')
    show(list)

    list=remove(list)
    show(list)

    list=add_end('cos',list)
    show(list)

    list=pop(list)
    show(list)

    print(is_empty(list))
    print(length(list))
    print(first(list))

    list2=take(list,4)
    show(list2)

    list3=drop(list, 2)
    show(list3)


if __name__ == "__main__":
    main()

