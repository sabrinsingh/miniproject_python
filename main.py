import random
def welcome():
    '''This creates the welcome page for the application'''
    for i in range(20):
        print('*\t', end='')
    print()
    for i in range(2):
        print('*',end='')
        for i in range(19):
            print('\t',end='')
        print('*')
    print('*', end='')
    for i in range(7):
        print('\t',end='')
    print('WELCOME TO THE PAGE', end='')
    for i in range(8):
        print('\t',end='')
    print('*')
    for i in range(2):
        print('*',end='')
        for i in range(19):
            print('\t',end='')
        print('*')
    for i in range(20):
        print('*\t', end='')

    print()
welcome()
print()
input('Press any key to start')
print('\n'*100)

def mainmenu():
    print('Play the game. \n 1. Rock Paper Scissors \n 2. Cows and Bulls \n 3. Exit')
    choice = (input('Enter your game choice : '))
    if choice == '1':
        rps()
    elif choice == '2':
        cnb()
    elif choice == '3':
        exit()
    else:
        print('Invalid Choice')
        mainmenu()


def rps():
    print('1. Play Game \n2. Return to main menu')
    choice = input('Enter your choice : ')
    if choice == '1':
        print('WELCOME TO ROCK PAPER SCISSORS GAME')
        user=input('Please enter 1 for rock , 2 for paper and 3 for scissors : ')
        lst=[1,2,3]

        comp=random.choice(lst)
        try:
            if user in '123':
                if comp == user:
                    print('Draw')
                elif (user == 1 and comp == 3) or (user == 2 and comp == 1) or (user ==3 or comp == 1):
                    print('You win')
                else:
                    print('You lose')
            else:
                print('Enter valid choice')
                rps()
        except Exception as e:
            print(e)
    elif choice == '2':
        mainmenu()
    else:
        print('Invalid Entry')
        rps()
def cnb():
    print('1. Play Game \n 2. Return to main menu')
    choice = input('Enter your choice : ')
    if choice == '1':
        pass
    elif choice == '2':
        mainmenu()
    else:
        print('Invalid Entry')
        cnb()

mainmenu()

