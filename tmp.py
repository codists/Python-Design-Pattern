# @Filename: tmp.py
# @Author: codists
# @Created: 2025-07-24 10:58:56

def validate_age(name):
    age = None
    try:
        age_input = input(f'Welcome {name}. How old are you? ')
        age = int(age_input)
    except ValueError:
        print(f'Age {name} is invalid, please try again...')
        return False, age
    return True, age

if __name__ == '__main__':
    valid_input = False
    while not valid_input:
        valid, age = validate_age('codist')
        print(f'输出：{valid_input}-{age}')
    print('end')
