list1 = [1, 7, 8, 'g', 'e']
def filter_list(l):
    list2 = []
    for el in range(len(l)):
        if isinstance(l[el], int):
            list2.append(l[el])
    print(list2)
filter_list(list1)        