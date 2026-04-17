"""
-> sort(reverse=False): Sorts the list in ascending order by default.
    E.g:    nums = [4, 2, 1, 3]
            nums.sort() / nums.sort(reverse=False)
            print(nums) => [1, 2, 3, 4]
-> sorted(list): Returns a new list, doesn't modify original list.
    E.g:    nums = [4, 2, 1, 3]
            new_list = sorted(nums)
            print(new_list) => [1, 2, 3, 4]
            print(nums) => [4, 2, 1, 3]
-> reverse(): Reverses the order in the list.
    E.g:    x = [1, 2, 3]
            x.reverse()
            print(x) => [3, 2, 1]
    -> This doesn't sorts in descending order.
-> copy(): Creates a shallow copy of the list.
    E.g:    a = [1, 2, 3]
            b = a.copy()
            print(b) => [1, 2, 3]
    -> b and a are now seperate lists.
"""