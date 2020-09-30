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
    """
    Une fibonnaci heap est un arbre permettant de stocker et trier des donnés efficacement
    https://en.wikipedia.org/wiki/Fibonacci_heap
    L'implémentation est décrite en anglais : https://en.wikipedia.org/wiki/Fibonacci_heap#Implementation_of_operations
    et en français : https://fr.wikipedia.org/wiki/Tas_de_Fibonacci#Implémentation_des_opérations

    Faire une classe supplémentaire appelée Node :
    -> Liste de node pour ensuite faire .value

    Une racine est un noeud sans parent (rien au dessus)
    
    Garder une liste avec toutes les racines + fonction consolidate -> regarde la liste des racines

    Node / rajouter 2 variables (left/right) = 2 branches en dessous
    -> 1 enfant à la node = +1 compteur

    None = rien valeur nulle

    Insérer la class node + fonction consolidate dans la class fib_heap
    """

    def insert(self, value: int) -> None:

        # class Node:

        #     def __init__(self, heap):
        #         self.heap = heap
        #         self.left = None
        #         self.right = None
        #         self.parent = None

        #     def __str__(self):
        #         return str(self.heap)

    def find_min(self) -> int:
        
        # print("min value element : ", min(value))
        # pass

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: Heap) -> None:
        """
        Fusionne deux arbres
        """
        pass