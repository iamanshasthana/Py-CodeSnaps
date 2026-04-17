"""
-> Set: It's an unordered, unindexed, collection in python that stores only uniques elements.
        Syntax: 
                my_set = {1, 2, 3}
        Features:
                -> Unordered
                -> No duplication of values allowed.
                -> Unchangeable
                -> Indexing not allowed
        E.g:    emails = ['a@gmail.com', 'b@gmail.com', 'a@gmail.com']
                unique_emails = set(emails)
                => {'a@gmail.com', 'b@gmail.com'}
    -> It removes duplicate values for the list.
            E.g:    data = [1, 2, 2, 3, 4, 1]
                    print(set(data)) => {1, 2, 3, 4}

"""