import math

T = 1
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    try:
        if a == -1:
            x_val = math.sqrt(c**2 - b**2)
            x = 'a'

        elif b == -1:
            x_val = math.sqrt(c**2 - a**2)
            x = 'b'

        elif c == -1:
            x_val = math.sqrt(a**2 + b**2)
            x = 'c'

        if x_val != 0.0:
            print(f'Triangle #{T}')
            print(f'{x} = {x_val:0.3f}')
            print()
        else:
            print(f'Triangle #{T}')
            print('Impossible.')
            print()

    except:
        print(f'Triangle #{T}')
        print('Impossible.')
        print()

    T += 1