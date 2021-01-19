# -*- coding: utf-8 -*-

import random


def get_random_number():
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    try: 
        int(user_input_number)
        result = True
    except: result = False
    # ==================================
    return result


def is_between_100_and_999(user_input_number):
    if 99 < int(user_input_number) < 1000: result = True
    else: result = False

    # ==================================
    return result


def is_duplicated_number(three_digit):
    if len(set(three_digit)) != 3: result = False
    else: result = True
    # ==================================
    return result


def is_validated_number(user_input_number):
    if is_digit(user_input_number):
        if(is_between_100_and_999(user_input_number)):
            if(is_duplicated_number(user_input_number)):
                return  True
    # ==================================
    return False


def get_not_duplicated_three_digit_number():
    a = get_random_number()
    while not is_duplicated_number(str(a)):
        a = get_random_number()
    # ==================================
    return a


def get_strikes_or_ball(user_input_number, random_number):
    result = [0,0]
    for i in range(3):
        a = user_input_number[i]
        if a in random_number:
            if random_number[i] == a: result[0] += 1
            else: result[1] += 1
    return result

def is_yes(one_more_input):
    if one_more_input.lower() == 'y' or one_more_input.lower() == 'yes': result = True
    else: result = False
    return result


def is_no(one_more_input):
    if one_more_input.lower() == 'n' or one_more_input.lower() == 'no': result = True  
    else: result = False
    return result


def main():
    print("Play Baseball")
    # ===Modify codes below=============
    # 위의 코드를 포함하여 자유로운 수정이 가능함
    more = True
    while more:
        wrong, new = True, True
        random_number = str(get_not_duplicated_three_digit_number())
        print("Random Number is : ", random_number)
        while wrong:
            user_input = input('Input guess number : ')
            if is_validated_number(user_input):
                st, ball = get_strikes_or_ball(user_input, random_number)
                print(f'Strikes : {st} , Balls : {ball}')
                if st == 3:
                    wrong = False
            elif user_input == '0':
                wrong, new, more = False, False, False
            else:
                print('Wrong Input, Input again')
        while new:
            w = input('You win, on more(Y/N)?')
            if is_yes(w):
                new = False
            elif is_no(w):
                new = False
                more = False
            else:
                print('Wrong Input, Input again')

    # ==================================
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()
