"""
-> Rules of Slicing:
        Step sign   |   Direction       |   Rule            |   Otherwise
            +       |   Left -> Right   |   Start < Stop    |       []
            -       |   Right -> Left   |   Start > Stop    |       []
-> Step = 0 not allowed it'll raise ValueError.

-> Negative Indexes: It'll count from end. -1 (last element), -2(second last element) etc.
        E.g:    a = [10, 20, 30, 40, 50]
                print(a[-1]) => 50
                print(a[-3:-1]) => [30, 40]

-> If slicing goes out of bound: No Error.
        E.g:    a = [1, 2, 3]
                print(a[1:10]) => [2, 3]
                print(a[-10:2]) => [1, 2]

-> Slicing in reverse:
        a[::-1] => Reverses the entire list
        E.g:    numbers = [1, 2, 3, 4, 5]
                reversed_numbers = numbers[::-1]
                print(reversed_numbers) => [5, 4, 3, 2, 1] 

-> Difference between Slicing & Indexing:
                Returns         E.g         O/P
Indexing    |   1 item      |   a[2]    |   30
Slicing     |   list        |   a[1:4]  |   [20, 30, 40]
"""