"""
TypeCasting Types:
            -> Implicit TypeCasting
            -> Explicit TypeCasting
(i) Implicit TypeCasting:
        Python automatically converts one data type to another (only valid numbers).
        Example:
                a = 5
                b = 3.2
                result = a + b
                print(result) => 8.2
        Here, python automatically converts 5 (which is of int data type) to 5.0 (float data type).
(ii) Explicit TypeCasting:
        User has to manually change data type using functions like:
                -> int(): it convert any data type into integer data type.
                -> float(): it converts any data type into float data type.
                -> str(): it converts any data type into string data type.
        Example:
                Converting string into integer:
                    age_str = "21"
                    age_int = int(age_str)
                    print(f"Age + 1 is: {age_int}") => Age + 1 is: 22        
                Converting float into integer:
                    pi = 3.14
                    value = int(pi)
                    print(f"Integer value of pi: {value}") => Integer value of pi: 3
-> A fact:
        Whenever we change a number data type from float to integer, it doesn't round off the number, it cuts off the decimal.
"""
