from random import randint

class Sorting:

    def Quicksort(self, list):
        pivot = randint(1, len(list)-1)
        return pivot

    # BUBBLESORT -> O(n²)
    def Bubblesort(self, list):
        # Flag para detectar si hubo algún swap
        flag = True

        while flag:
            for x in range(len(list)-1):
                # Condición para hacer un swap.
                if list[x] > list[x+1]:
                    list[x], list[x+1] = list[x+1], list[x]
                    # Se marca false para marcar que hubo un swap.
                    flag = False
            # Si hubo un swap se repite el ciclo otra vez para verificar el orden.
            if(not flag):
                flag = True
            # Si no hubo significa que ya todo está ordenado y se sale del ciclo.
            else:
                flag = False

        return list


    def BucketSort(self, list):
        bucket = []
        for x in list:
            bucket[x] += 1

        return bucket

list = [9, 8, 7, 6, 5, 4, 3, 2, 1]

static = Sorting()
print(static.Bubblesort(list))
print(static.BucketSort(list))