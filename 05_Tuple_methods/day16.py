"""
-> Unpacking tuples: When we create a tuple we assign values to it,
                     that's packing a tuple.
    ->  Extracting of values back into variables is unpacking.

        E.g:    fruits = ('apple', 'kiwi', 'cherry')
                (green, brown, red) = fruits
                print(green) => apple
                print(brown) => kiwi
                print(red) => cherry
        
    ->  If no of variables are less than no of values, we can use asterisk (*)
            to collect the remaining values as a list.
    E.g:    fruits = ('apple', 'banana', 'cherry', 'strawberry', 'raspberry')
            (green, yellow, *red) = fruits
            print(green) => apple
            print(yellow) => banana
            print(red) => ['cherry', 'strawberry', 'raspberry']

"""
