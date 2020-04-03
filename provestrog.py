import random
def intersect(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return len(lst3)
if __name__ == '__main__':
    lista = [[0, [2, 1, 0]], [1, [1, 2, 0]], [2, [3, 0, 2]], [3, [1, 2, 3]], [4, [3, 2, 1]], [5, [3, 0, 1]], [6, [3, 1, 2]], [7, [2, 3, 1]], [8, [1, 3, 0]], [9, [1, 0, 3]]]
    print(lista)
    elem = [10, [2,2,2]]
    j = len(lista) - 1
    while j > 0:
        if intersection(lista[j][1], elem[1])>0:
            lista.append(elem)
            print(lista[j])
            break
        j-=1

