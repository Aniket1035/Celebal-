def lower_triangular(n):
    for i in range(1, n + 1):
        for j in range(i):
            print('*', end=' ')
        print()

def upper_triangular(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end=' ')
        print()

def pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(' ', end='')
        # Print stars with spaces
        for k in range(i):
            print('* ', end='')
        print()
