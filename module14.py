#demontrating the ue of __name__ == “__main__”

def add() :
    print('Result of Sum is: ', __name__)

def sub() :
    print('Result of sub is: ')


def main() :
    print('in module14 main')
    add()                       #calling both functions in a seperate function main()
    sub()

if __name__ == '__main__':
    main()
