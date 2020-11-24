import random

print('Rules to win:\n'
      'paper vs stone ==> paper is win\n'
      'paper va scissor ==> scissor is win\n'
      'stone vs scissor ==> stone is win')
print('choice is :\n'
      '1.stone \n'
      '2.paper \n'
      '3.scissor')


while True:
    choice = int(input('use choice: '))

# choice should be between 1 and 3

    while choice > 3 or choice < 1:
        choice = int(input('please enter valid input: '))

# condition of user choice

    if choice == 1:
        choice_name = 'stone'
    elif choice ==2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
    print('user choice is,', choice_name)
    print('computer turn...')

# computer choice is random between one and three

    choice_com = random.randint(1,3)

# while this condition is true , computer choice randomly

    while choice == choice_com:
        choice_com = random.randint(1,3)

# condition for computer choice

    if choice_com == 1:
        choice_name_com = 'stone'
    elif choice_com == 2:
        choice_name_com = 'paper'
    else:
        choice_name_com = 'scissor'
        print('user choice is,', choice_name_com)

# condition for winner

    if (choice == 1 and choice_com == 2) or (choice == 2 and choice_com ==1):
        print('paper win')
        result = 'paper'
    elif (choice_com == 1 and choice == 3) or (choice_com == 3 and choice == 1):
        print('stone win')
        result = 'stone'
    else:
        print('scissor win')
        result = 'scissor'

# print winner

    if result == choice_name_com:
        print('computer is win')
    else:
        print('user is win')

# if you want to continue the game, please enter N or n

        print('Do you want to countinue?')
    ans = input()
    if ans == 'n' or ans == 'N':
        break