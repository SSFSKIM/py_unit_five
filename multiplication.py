#Steve
#11.02
def multiplication_table(number):
    """
    Ex. multiplication_table(6) returns "6 12 18 24 30 36 42 48 54 60 66 72 "
    :param number: An integer
    :return: A string of 12 values representing the mulitiplication table of the parameter number.
    """
    table = '\"'
    for i in range(12):
        table = table + f'{number+number*i} '
    table = table + '\"'
    print (table)

number = int(input())
multiplication_table(number)