"""
-> Updating the tuple:
        Tuples are unchangeable, that means we can't change, 
        add or remove items once the tuple is created.
    There are workarounds:
    -> Converting tuple into list:
        We can change tuple -> list, then change the list & cnvert the list -> tuple.
            E.g:    x = ('apple', 'orange', 'mango')
                    y = list(x)
                    y[1] = 'kiwi'
                    x = tuple(y)
                    print(x) => ('apple', 'kiwi', 'mango') 
    -> Add items:
        As tuples are unchangeable, so we can merge tuple together.
            E.g:    x = ('apple', 'orange', 'mango')
                    y = ('kiwi',)
                    x += y
                    print(x) => ('apple', 'orange', 'mango', 'kiwi')
    -> Remove items:
        We can't remove items but we can remove tuple completely.
            E.g:    x = (1, 2, 3)
                    del x
                    print(x) => it'll raise an error
"""
