"""
(iii)   pop: Removes & returns a random element.
        Syntax: element = set.pop()
        Behaviour:
            ->  Removes a random element (not truly random but unordered).
            ->  Raises a 'KeyError' if set is empty.
        E.g:    s = {10, 20, 30}
                x = s.pop() => Removes one element randomly
(iv)    remove: Removes a specific element.
        Syntax: set.remove(element)
        Behaviour:
            ->  Removes the specified element.
            ->  Raises 'KeyError' if element doesn't exist.
(v)     discard: Removes a specific element if it exists.
        Syntax:  set.discard(element)
        Behaviour:
            ->  Removes element if present.
            ->  Doesn't raises error if element is missing.
        E.g:    s = {1, 2, 3}
                s.discard(2) => {1, 3}
                s.discard(5) => No error   
"""