class Heap(object):
    """
    Une heap est une structure de données sous forme d'arbre.
    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        pass

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        pass

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def decrease_key(self, current_value: int, new_value :int) -> None:
        """
        Modify une valeur dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        """
        Fusionne deux arbres
        """
        pass


class Tree(object):
     def __init__(self):
        self.trees = []
        self.count = 0

    def add_value(self, tree):
        self.children.append(tree)
        self.size += 1

    def __repr__(self):
        return repr(self.children)

class FibonacciHeap(Heap):

    class __init__(self):
        self.nodes = []
        self.count = 0

    def insert(self, value: int) -> None:

        new_tree = Tree()
        new_tree.add_value(value)
        self.trees.append(new_tree)
        self.count += 1


    def find_min(self) -> int:
         return int(min(tree.children[0] for tree in self.trees))

    def delete_min(self) -> int:
        pass

    def merge(self, fibonnaci_heap: Heap) -> None:
        pass

fheap = FibonacciHeap()

data = [2, 3, 12, 56, 5, 11]

for value in data:
    fheap.insert(value)

print('First load :', fheap.trees)

print('Minimum value :', fheap.find_min())