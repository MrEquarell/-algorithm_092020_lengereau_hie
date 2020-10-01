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
        self.nodes = []
        self.count = 0

    def add_value(self, value):
        self.nodes.append(value)
        self.count = self.count + 1

    def __repr__(self):
        return repr(self.nodes)

class FibonacciHeap(Heap):

    def __init__(self):
        self.nodes = []
        self.count = 0

    def insert(self, value: int) -> None:

        new_tree = Tree()
        new_tree.add_value(value)
        self.nodes.append(new_tree)
        self.count = self.count + 1
        
        #FibonacciHeap = []
        #FibonacciHeap = [ 1, 2, 3, 4, 5, 6, 7 ]
        #FibonacciHeap.insert(10)
        #print(FibonacciHeap)


    def find_min(self) -> int:
        pass

    def delete_min(self) -> int:
        pass

    def merge(self, fibonnaci_heap: Heap) -> None:
        pass

new_heap = FibonacciHeap()
data = [10, 12, 14, 52, 54, 101, 152, 4, 7, 17]

# data = [[10, [17]], [12], [14], [52], [101], [152], [4], [7]]
# data = [[10, [17]], [14], [52], [101], [152], [4], [7, [12]]]

for value in data:
    new_heap.insert(value)

print(new_heap.nodes)
print(new_heap.find_min())