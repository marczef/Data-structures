#skonczone
class Element:
    def __init__(self, key, value):
        self.key=key
        self.value=value


class Dictionary:

    def __init__(self, size, c1, c2):

        self.tab = [None for i in range(size)]
        self.size = size
        self.c1=c1
        self.c2=c2

    def __str__(self):

        string='{'
        for i in self.tab:
            if i is not None:
                string+='['+str(i.key)+': '+str(i.value)+'], '
            else:
                string+="None "

        string+='}'
        return string

    def to_int(self, data):
        pom = 0
        for i in data:
            pom += + ord(i)

        return pom


    def hash_function(self, data, i):
        if isinstance(data, str):
            index = int(self.to_int(data) + self.c1 * i + self.c2 * i ** 2) % self.size
            if index == i:
                for j in range(self.size):
                    if self.tab[index] is not None:
                        index = (index + 1) % self.size
                    else:
                        break
                return index
            else:
                return index
        else:
            index = int(int(data) + self.c1 * i + self.c2 * i ** 2) % self.size
            if index == i:
                for j in range(self.size):
                    if self.tab[index] is not None:
                        index = (index + 1) % self.size
                    else:
                        break
                return index
            else:
                return index

    def insert(self, key, value):
        for i in range(self.size):
            if self.tab[self.hash_function(key, i)] is None or self.tab[self.hash_function(key, i)].key == key:
                node=Element(key,value)
                self.tab[self.hash_function(key, i)]=node
                return
        print('nie ma miejsca')

    def search(self, key):

        for i in self.tab:
            if i is not None:
                if i.key==key:
                    return i.value

        return None

    def remove(self, key):

        exist=False
        for i in range(self.size):
            if self.tab[i] is not None:
                if self.tab[i].key==key:
                    self.tab[i]=None
                    exist=True

        if exist is False:
            print("Brak danej")


def function1(dict: Dictionary):


    for i in range(1, 16):

        if i==6:
            dict.insert(18, chr(ord('A') + i-1))
        elif i ==7:
            dict.insert(31, chr(ord('A') + i-1))
        else:
            dict.insert(i, chr(ord('A') + i-1))

    print(dict)
    print(dict.search(5))
    print(dict.search(14))
    dict.insert(5, 'Z')
    print(dict)
    print(dict.search(5))
    print(dict)
    dict.remove(5)
    print(dict)
    print(dict.search(31))
    dict.insert('test', 'W')
    print(dict)

def function2(dict: Dictionary):

    for i in range(1, 16):
        dict.insert(i*13, chr(ord('A') + i - 1))

    print(dict)



def main():

    dict = Dictionary(13, 1, 0)
    function1(dict)

    dict=Dictionary(13, 1, 0)
    function2(dict)

    dict = Dictionary(13, 0, 1)
    function1(dict)

    dict=Dictionary(13, 0, 1)
    function2(dict)


if __name__ == "__main__":
    main()
