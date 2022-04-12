#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]

class Cyclic_list:

    def __init__(self, tab=[None for i in range(5)]):
        self.tab = tab
        self.size = len(tab)
        self.index_zap = 0
        self.index_od = 0

    # kolejka
    def print_queue(self):
        string = '['

        index_od_pom = self.index_od

        while index_od_pom != self.index_zap:
            string += str(self.tab[index_od_pom]) + " "
            if index_od_pom < self.size-1:
                index_od_pom += 1
            else:
                index_od_pom = 0

        return string + ']'

    def print_tab(self):
        string = '['
        for el in self.tab:
            string += str(el) + ' '
        return string + ']'

    def is_empty(self):
        if self.index_od == self.index_zap:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty() == True:
            return None
        else:
            return self.tab[self.index_od]

    def enqueue(self, val):

        if self.index_zap==self.size:
            self.index_zap=0

        if not self.is_empty():
            if self.index_zap+1==self.index_od:
                for i in range(self.size):
                    self.tab.insert(i+self.index_zap, None)
                self.index_od+=self.size
                self.size=self.size*2

        self.tab[self.index_zap]=val
        self.index_zap+=1

    def dequeue(self):

        if self.is_empty():
            return None
        else:
            pom = self.tab[self.index_od]
            self.index_od += 1

            if self.index_od == self.size:
                self.index_od=0


            return pom


def main():

    list=Cyclic_list()

    for i in range(1,5):
        list.enqueue(i)
    print(list.print_queue())
    print(list.print_tab())

    print(list.dequeue())
    print(list.peek())

    for i in range(5,9):
        list.enqueue(i)
    print(list.print_queue())
    print(list.print_tab())

    for i in range(list.size):
        list.dequeue()

    print(list.is_empty())





if __name__ == "__main__":
    main()
