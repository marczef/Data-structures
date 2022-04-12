from typing import Tuple, List

class Node:

    def __init__(self, data):
        self.data=data
        self.next = None


class LinkedList:


    def __init__(self,whole=None): #dodałam funkcjonalność że oprócz inicjowania pustej listy można od razu zainicjować listę z elementami

        self.datas=[]

        if whole is not None:
            self.datas = []
            node = Node(whole[0])
            self.head = node
            for elem in whole[1:]:
                node.next = Node(elem)
                node = node.next
                self.datas.append(node)
        else:
            self.head = None



    def __str__(self):

        string="["
        printval = self.head
        while printval is not None:
            string+=str(printval.data)+"\n"
            printval=printval.next
        string+="]"

        return string


    def destroy(self):
        self.head=None

    def add(self, elem):
        elem=Node(elem)
        elem.next = self.head
        self.head = elem

    def remove(self):
        self.head= self.head.next

    def is_empty(self) -> bool:

        if self.head is None:
            return True
        else:
            return False

    def __len__(self): #odpowiednik lenght, żeby łatwiej można było wywoływać funkcję

        val=self.head
        pom=1
        while val.next is not None:
            pom+=1
            val=val.next

        return pom

    def get(self):

        return self.head.data

    def update(self, val):

        pom=self.head

        if pom !=None:

            while pom.next is not None:
                pom=pom.next
            pom.next=Node(val)

        else:
            self.head = Node(val)

    def pop(self):

        pom=self.head
        while pom.next.next is not None:
            pom=pom.next
        pom.next=None

    def take(self,n):

        if n<=len(self):
            counter=0
            val=self.head
            list=LinkedList()
            while counter != n:
                list.update(val.data)
                val=val.next
                counter+=1

        else:
            return self

        return list


    def drop(self, n):

        if n<=len(self):

            counter=0
            val=self.head
            list=LinkedList()

            while counter != n:
                #list.update(val.data)
                val=val.next
                counter+=1

            while val.next is not None:
                list.update(val.data)
                val=val.next
                counter+=1

            list.update(val.data)

        else:
            return self

        return list



def main():


    list = LinkedList([('AGH', 'Kraków', 1919),
('UJ', 'Kraków', 1364),
('PW', 'Warszawa', 1915),
('UW', 'Warszawa', 1915),
('UP', 'Poznań', 1919),
('PG', 'Gdańsk', 1945)])
    print(list)

    list.add("cos")
    print(list)

    list.remove()
    print(list)

    list.update('cos')
    print(list)

    list.pop()
    print(list)

    print(list.is_empty())
    print(len(list))
    print(list.get())

    list2=list.take(4)
    print(list2)

    list3=list.drop(4)
    print(list3)

    list3.destroy()
    print(list3)


if __name__ == "__main__":
    main()