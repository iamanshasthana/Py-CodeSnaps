"""
-> add method:
        Syntax: 
                set_name.add(element)
        Features:
            ->  Adds single element to the set.
            ->  Ignores the element if it already exists.
        E.g:    s = {1, 2, 3}
                s.add(4)
                print(s)   => {1, 2, 3, 4}
                s.add(2)
                print(s)   => {1, 2, 3, 4} (no change)
-> update method:
        Syntax: 
                set_name.update(iterable)
        Features:
            ->  Adds multiple elements from iterable(list, tuple, set, string etc)
            ->  Ignores duplicate automatically.
        E.g:    s = {1, 2}
                s.update([2, 3, 4])
                print(s) => {1, 2, 3, 4}
                s.update("abc")
                print(s) => {1, 2, 3, 4, "a", "b", "c"}

-> Only immutable/hashable items are allowed.
            Valid       |       Invalid
        {1, 2, (3, 4)}  |   {1, 2, [3, 4]}
        set("abc")      |   set([[1, 2], [3, 4]])
"""