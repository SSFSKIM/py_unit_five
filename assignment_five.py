#Steve
#11.07
import random

def get_number():
    '''
    call zero and one labeled pile as global and assign them a number.
    :return:
    '''
    global zero
    global one
    zero = random.randint(20,30)#random number between 20 and 30
    one = random.randint(20, 30)#random number between 20 and 30

get_number()#call random number pile
def game_start():
    global zero #use variable zero and one as global
    global one
    print("Hello. This is Nim game. There are two piles of stones between 20 and 30, each labeled with 0 and 1.")#explain rule to user
    print("You're going to take 1~3 stone from one of the files. one who take the last stone from any file loose")
    while True:
        print(f'each file of 0 and 1 is {zero}, {one}, respectively')#show how many left on each pile
        pile, num = input('which pile to remove(zero, one), and how many(1~3) (ex: zero 1)').split() #get input of which pile to remove and quantity of stones
        if 1 <= int(num) <= 3 and pile == 'zero' or 1 <= int(num) <= 3 and pile == 'one': #run game only when user gives right input
            if pile == 'zero':#when user says zero
                zero -= int(num) #subtract number from 'zero' pile
                if zero == 1: #if user make this file to 1, user wins
                    print('user won!')
                    break
                if zero % 4 - 1 != 0: #computer's strategy for wining: make number to be  remainder 1 when divided by 4
                    com = (zero-1)%4
                    print(com)
                    zero -= com
                else: #current stone in pile's remainder is not 1, just pick 1
                    print(1)
                    zero -= 1
            else:
                one -= int(num) #same thing with when user picks zero.
                if one == 1:
                    print('user won!')
                    break
                if (one - 1)%4 != 0:
                    com = (one - 1)%4
                    print(com)
                    one -= com
                else:
                    print(1)
                    one -= 1
            if zero == 1 and one == 1: #if both pile got 1, user has to pick one from both; thus, user loose.
                print(f'file left {zero}, {one}, your turn.')
                print('computer won!')
                break
        else: #if wrong input is on, get another input from user
            print('AGAIN, input proper number between 1 and 3 or pile name of zero and one')

def main():
    get_number()
    game_start()

main()