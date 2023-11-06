#Steve
#11.07
import random

def get_number():
    global zero
    global one
    zero = random.randint(20,30)
    one = random.randint(20, 30)
get_number()
while True:
    print(f'each file of 0 and 1 is {zero}, {one}, respectively')
    pile, num = input('which pile to remove(zero, one), and how many(1~3)').split()
    if 1 <= int(num) <= 3 or pile == 'zero' or pile == 'one':
        if pile == 'zero':
            zero -= int(num)
            if zero == 1:
                print('user won!')
                break
            if zero % 4 - 1 != 0:
                com = (zero-1)%4
                print(com)
                zero -= com
            else:
                print(1)
                zero -= 1
        else:
            one -= int(num)
            if one == 1:
                print('user won!')
                break
            if one%4 - 1 != 0:
                com = (one% - 1)%4
                print(com)
                one -= com
            else:
                print(1)
                one -= 1
    if zero == 1 or one == 1:
        print('computer won!')
        break
    else:
        print('AGAIN, input proper number between 1 and 3 or pile name of zero and one')