import sys
import os
sys.path.append(f'{os.getcwd()}/filters')
from filters import Filters
from arithmetic.arithmetic_operation import ImageOperations


def main():
    print(bordered('> HI THERE <'))
    while(True):
        option = input('''Which Operation Do You Want:
        1- Arithmetic Operation
        2- Filters & Transformers
        ''')
        if option == '1':
            ari = ImageOperations()
            ari.main()
            break
        elif option == '2':
            filter = Filters()
            filter.main()
            break
        else:
            print('Invalid Option Try Agine!')
    

def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)


if __name__ == "__main__":
    main()