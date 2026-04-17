"""
-> Some List methods:
    -> append(): Adds a single item to the end of the list.
        E.g:    fruits = ['apple', 'orange']
                fruits.append('cherry')
                print(fruits) => ['apple', 'orange', 'cherry']
        -> We can append only one item in a single shot.
        -> If we append([1, 2]), it adds it as a sublist.
    -> extend(): Adds each item of an iterable to a list.
        E.g:    a = [1, 2]
                a.extend([3, 4])
                print(a) => [1, 2, 3, 4]
    -> insert(index, value): Inserts an item at a specified position. Existing items shifts to the right.
        E.g:    a = [1, 2, 4]
                a.insert(2, 3)
                print(a) => [1, 2, 3, 4]
    -> remove(value): Removes the first matching item from the list. If value isn't found it raises ValueError.
        E.g:    colors = ['red', 'blue', 'green', 'red']
                colors.remove('red')
                print(colors) => ['blue', 'green', 'red']


"""