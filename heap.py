#skonczone
class Element:

    def __init__(self, prior, val):
        self.prior = prior
        self.val = val

    def __gt__(self, other):
        if self.prior > other.prior:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.prior < other.prior:
            return True
        else:
            return False

    def __str__(self):

        string = str(self.prior)+": "+str(self.val)
        return string

    def __repr__(self):
        return str(self.prior)+ ": "+str(self.val)

class Heap:

    def __init__(self):
        self.tab = []
        self.size=0


    def is_empty(self):
        if self.tab == []:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty() is True:
            print('nie ma heada')
            return
        else:
            return self.tab[0]

    def right(self, i):
        if (i * 2 + 2) < self.size:
            return i * 2 + 2
        else:
            return None

    def left(self, i):
        if (i*2+1) < self.size:
            return i*2+1
        else:
            return None

    def parent(self, i):
        if ((i - 1)//2) >= 0:
            return ((i - 1)//2)
        else:
            return None

    def enqueue(self, prior, val):
        if self.size == 0:
            el = Element(prior, val)
            self.tab.append(el)
            self.size += 1
        else:
            el = Element(prior, val)
            self.tab.append(el)
            self.size+=1
            i = self.size-1

            while self.parent(i) is not None and self.tab[self.parent(i)] < self.tab[i]:
                self.tab[self.parent(i)], self.tab[i] = self.tab[i], self.tab[self.parent(i)]
                i = self.parent(i)

    def dequeue(self):

        if self.is_empty() is True:
            return None
        else:
            self.tab[0], self.tab[-1] = self.tab[-1], self.tab[0]
            self.size-=1
            pom=self.tab[-1]
            del self.tab[-1]


            curr_node=0

            while 1:
                if self.left(curr_node) is not None and self.right(curr_node) is not None:
                    if self.tab[curr_node] < self.tab[self.left(curr_node)] or self.tab[curr_node] == self.tab[self.left(curr_node)] and self.tab[curr_node] < self.tab[self.right(curr_node)] or self.tab[curr_node] == self.tab[self.left(curr_node)]:
                        if self.tab[self.left(curr_node)] > self.tab[self.right(curr_node)]:
                            self.tab[self.left(curr_node)], self.tab[curr_node] = self.tab[curr_node], self.tab[self.left(curr_node)]
                            curr_node = self.left(curr_node)
                        else:
                            self.tab[self.right(curr_node)], self.tab[curr_node] = self.tab[curr_node], self.tab[self.right(curr_node)]
                            curr_node = self.right(curr_node)
                    else:
                        return pom

                if self.left(curr_node) is None and self.right(curr_node) is not None:
                    if self.tab[self.right(curr_node)] > self.tab[curr_node]:
                        self.tab[self.right(curr_node)], self.tab[curr_node] = self.tab[curr_node], self.tab[self.right(curr_node)]
                        curr_node = self.right(curr_node)
                    else:
                        return pom

                if self.right(curr_node) is None and self.left(curr_node) is not None:
                    if self.tab[self.left(curr_node)] > self.tab[curr_node]:
                        self.tab[self.left(curr_node)], self.tab[curr_node] = self.tab[curr_node], self.tab[self.left(curr_node)]
                        curr_node = self.left(curr_node)
                    else:
                        return pom

                if self.right(curr_node) is None and self.left(curr_node) is None:
                    return pom


    def print_tree(self, idx, lvl):
        if idx is not None and idx<self.size:
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl+1)

    def print_tab(self):
        if self.is_empty():
            print('{}')
            return
        print ('{', end=' ')
        for i in range(self.size-1):
            print(self.tab[i], end = ', ')
        if self.tab[self.size-1]: print(self.tab[self.size-1] , end = ' ')
        print( '}')


def main():
    heap = Heap()

    tab=['A','L','G','O','R','Y','T','M']
    key=[4, 7, 6, 7, 5, 2, 2, 1]
    for i in range(len(key)):
        heap.enqueue(key[i], tab[i])
    heap.print_tree(0, 0);
    heap.print_tab()



    print(heap.dequeue())
    print(heap.peek())
    heap.print_tab()

    while heap.is_empty() is False:
        print(heap.dequeue())

    heap.print_tab()



if __name__ == "__main__":
    main()