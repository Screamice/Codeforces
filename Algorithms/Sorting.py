from random import randint

class Sorting:

    def Quicksort(self, list):
        pivot = randint(1, len(list)-1)
        return pivot

list = [1,2,3,4,5,6,7,8,9]

static = Sorting()
pivot = static.Quicksort(list)
print(pivot)
print(list[pivot])