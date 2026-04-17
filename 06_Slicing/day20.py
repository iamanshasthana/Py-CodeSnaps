"""
->  Slicing in Python (list, tuple, string): It's a concise way to extract a portion of a sequence,
            It creates a new sequence containing elements from the original within a specified range.

    Syntax: sequence[start:stop]

    ->  start:   A point from where the slicing will start, start included.
    ->  stop:   Index from where slicing will end, stop excluded.
    ->  It'll provide a sequence that won't change.

    E.g (1):    a = [10, 20, 30, 40, 50]
                result = a[1:4]
                print(result)   => [20, 30, 40]
    E.g (2):    t = (5, 10, 15, 20, 25)
                result = t[0:3]
                print(result)   => (5, 10, 15)
    E.g (3):    s = "PYTHON"
                result = s[2:5]
                print(result)   => THO
"""