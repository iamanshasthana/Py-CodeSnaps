"""
->  Rules of Slicing:
        ->  Stop is exclusive.
        ->  If Start & Stop both are +ve then it'll be counted from left.
        ->  If Start >= Stop then result will be empty.
        ->  Slicing doesn't changes original sequence, it gives new sequence.
        ->  Slicing in python allows us to extract a portion from a list,
            tuple, or string using their index positions.
    Syntax: 
            sequence[start:stop:step]
    ->  step:  If step = 1  (every element)
               If step = 2  (skips 1)

        E.g (list):     a = [10, 20, 30, 40, 50]
                        print(a[1:4]) => [20, 30, 40]
                        print(a[:3]) => [10, 20, 30]
                        print(a[2:]) => [30, 40, 50]
                        print(a[::2]) => [10, 30, 50]
        E.g (tuple):    t = (1, 2, 3, 4, 5)
                        print(t[1:4]) => (2, 3, 4)     
                        print(t[::-1]) => (5, 4, 3, 2, 1) 
        E.g (string):   s = "PYTHON"
                        print(s[1:4]) => YTH
                        print(s[::-1]) => NOHTYP    
"""
