#Steve
#11.02

def fibonacci(x):
    """
    Ex. fibonacci(5) returns "1 1 2 3 5 "
    :param number: The number of Fibonacci terms to return
    :return: A string consisting of a number of terms of the Fibonacci sequence.
    """
    a = [1, 1]
    for i in range(x):
        a.append(a[i] + a[i+1])
    table = '\"'
    for i in range(x):
        table = table + f'{a[i]} '
    table = table + '\"'
    print (table)

number = int(input())
fibonacci(number)