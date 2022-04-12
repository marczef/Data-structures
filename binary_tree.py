class Root:

    def __init__(self):
        self.head = None

    def insert(self, key, val):

        if self.head is None:
            child = Child(key, val)
            self.head = child

        else:
            curr_node = self.head
            child = Child(key, val)

            while 1:
                if curr_node.key > key:
                    if curr_node.left is None:
                        curr_node.left = child
                        return
                    else:
                        curr_node = curr_node.left

                if curr_node.key < key:
                    if curr_node.right is None:
                        curr_node.right = child
                        return
                    else:
                        curr_node = curr_node.right

                if curr_node.key == key:
                    curr_node.val = val
                    return

    def search(self, key, curr_node):

        if curr_node is None:
            return None
        else:
            if curr_node.key < key:
                return self.search(key, curr_node.right)
            elif curr_node.key > key:
                return self.search(key, curr_node.left)
            else:
                return curr_node.val


    def print_tree(self):
        print("==============")
        self._print_tree(self.head, 0)
        print("==============")


    def _print_tree(self, node, lvl):
        if node != None:
            self._print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.val)

            self._print_tree(node.left, lvl + 5)

    def list_2d(self, node=None, pom=0):
        if self.head is None:
            return None
        if node is None and pom == 0:
            node = self.head
        list=[]
        if node is not None:
            list = self.list_2d(node.left, pom+1)
            list[node.key] = node.val
            list.update(self.list_2d(node.right, pom+1))
        return list

    def print_list(self):
        print(self.tree_list())

    def delete(self, key):

        if self.search(key, self.head) is None:
            print("nie ma zmiennej o takim kluczu")
            return 0

        else:
            curr_node = self.head
            prev_node = self.head
            pom=0

            while 1:
                if curr_node.key > key:
                    if curr_node.left.key == key:
                        prev_node = curr_node
                        curr_node = curr_node.left
                        pom=1
                        break
                    else:
                        curr_node = curr_node.left

                if curr_node.key < key:
                    if curr_node.right.key == key:
                        prev_node = curr_node
                        curr_node = curr_node.right
                        pom=2
                        break
                    else:
                        curr_node = curr_node.right


                if curr_node.key == key:
                    break

            if curr_node.left is None and curr_node.right is None:
                if prev_node.left is not None:
                    if prev_node.left.key == key:
                        prev_node.left = None

                if prev_node.right is not None:
                    if prev_node.right.key == key:
                        prev_node.right = None
                return

            if curr_node.left is None and curr_node.right is not None:
                if pom == 2: #jesli ansz usuwany jest z prawej
                    prev_node.right = curr_node.right
                elif pom == 1:
                    prev_node.left = curr_node.right
                return


            if curr_node.left is not None and curr_node.right is None:

                if pom == 2:
                    prev_node.right = curr_node.left
                elif pom == 1:
                    prev_node.left = curr_node.left

            if curr_node.left is not None and curr_node.right is not None:

                if curr_node.right.left is None:
                    curr_node.key = curr_node.right.key
                    curr_node.val = curr_node.right.val
                    curr_node.right = curr_node.right.right

                elif curr_node.right.left is not None:


                    pom_node = curr_node.right.left
                    pom_prev_node = curr_node.right

                    while pom_node.left is not None:
                        pom_node = pom_node.left
                        pom_prev_node = pom_prev_node.left

                    curr_node.key = pom_node.key
                    curr_node.val = pom_node.val

                    if pom_node.right is not None:
                        pom_prev_node.left = pom_node.right
                    elif pom_node.right is None:
                        pom_prev_node.left = None


    def height(self, node, i=0):
        if node is None:
            return i
        left = self.height(node.left, i+1)
        right = self.height(node.right, i+1)
        return left if left > right else right

class Child:

    def __init__(self, key, val, right=None, left=None):
        self.key = key
        self.val = val
        self.right = right
        self.left = left


def main():

    tree = Root()
    dict = {50: 'A', 15: 'B', 62: 'C', 5: 'D', 20: 'E', 58: 'F', 91: 'G', 3: 'H', 8: 'I', 37: 'J', 60: 'K', 24: 'L'}

    for key in dict:
        tree.insert(key, dict[key])

    tree.print_tree()
    print(tree.list_2d())
    print(tree.search(24, tree.head))
    tree.insert(20, 'AA')
    tree.insert(6, 'M')
    tree.print_tree()
    tree.delete(62)
    tree.insert(59, 'N')
    tree.insert(100, 'P')
    tree.delete(8)
    tree.delete(15)
    tree.insert(55, 'R')
    tree.print_tree()
    tree.delete(50)
    tree.print_tree()
    tree.delete(5)
    tree.delete(24)
    print(tree.height(tree.head))
    print(tree.list_2d())
    tree.print_tree()


