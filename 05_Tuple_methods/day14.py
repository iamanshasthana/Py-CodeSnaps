"""
-> Tuple:   It's a collection which is ordered and unchangeable.
        ->  These are used to store multiple items in a single variable.
        ->  Tuples are written within round brackets.
        E.g:    my_tuple = ('apple', 'banana', 'cherry')
                print(my_tuple) => ('apple', 'banana', 'cherry')
        
        -> Tuple can contain elements of any data type and elements can be of mixed data type.

-> Accessing tuple elements:
        We can access tuple elements by referring to the index no, inside square brackets [].
            E.g:    my_tuple = ("apple", "banana", "cherry")
                    print(my_tuple[1])  => banana

    -> Negative indexing means starting from the end of the tuple.
            E.g:    my_tuple = ("apple", "banana", "cherry")
                    print(my_tuple[-1]) => cherry
        We can specify a range of indexes by specifying where to start and end the range.
            E.g:    my_tuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
                    print(my_tuple[2:5])  => ('cherry', 'orange', 'kiwi')

"""