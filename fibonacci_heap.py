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


class FibonacciHeap(Heap):

    def insert(self, value: int) -> None:

        FibonacciHeap = []
        FibonacciHeap = [ 1, 2, 3, 4, 5, 6, 7 ]
        FibonacciHeap.insert(10)
        print(FibonacciHeap)


    def find_min(self) -> int:
        pass

    def delete_min(self) -> int:
        pass

    def merge(self, fibonnaci_heap: Heap) -> None:
        pass