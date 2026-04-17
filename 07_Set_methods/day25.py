"""
-> Python set methods:
    (i)     add():  Adds a single element to the set.
            Syntax: set.add(element)
            Behaviour:
                ->  Adds element if it doesn't exists.
                ->  If the element already exists, nothing happens.
                ->  Only immutable(unchangeable) types can be added.
            E.g:    s = {1, 2}
                    s.add(3) => {1, 2, 3}
                    s.add(2) => no effect
                    print(s) => {1, 2, 3}
    (ii)    update():   Adds multiple elements from an iterable(list, tuple, string etc).
            Syntax:     set.update(itr1, itr2,....)
            Behaviour:  
                    ->  Adds all items from one or more iterables.
                    ->  Modifies the original set.
            E.g:    s = {1, 2}
                    s.update([3, 4], {5}) 
                    print(s) => {1, 2, 3, 4, 5}
"""