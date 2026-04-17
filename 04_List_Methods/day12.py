"""
-> Shallow Copy:    It creates a new list, but if the original list contains other lists,
                    then new list will still share references to those inner lists.
                    So changes to inner lists in one copy affects the other.
            E.g:    original = [1, [2, 3]]
                    shallow_copy = original.copy() 
                    shallow_copy[1][0] = 99
                    print(original) => [1, [99, 3]]
                    print(shallow_copy) => [1, [99, 3]]
-> Deep Copy:   Creates a completely independent new list,
                including making new copies of all nested lists.
                Changes to one copy, even its inner parts, will not affect the other.
            E.g:    import copy
                    original = [1, [2, 3]]
                    deep_copy = copy.deepcopy(original)
                    deep_copy[1][0] = 99
                    print(original) => 1, [2, 3]]
                    print(deep_copy) => [1, [99, 3]]
                    

"""
