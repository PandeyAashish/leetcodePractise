""" Square star
        ****
        ****
        ****
        ****
"""


def pattern1(n):
    for i in range(n):
        print('*' * 4)


#
# pattern1(4)

"""
           ****
           *  *
           *  *
           ****
Hollow Square Star Pattern

"""


def pattern2(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print('*', end=' ')
            else:
                print(" ", end=" ")
        print()


# pattern2(10)

"""
           ****
            ****
             ****
              ****
Rhombus Star Pattern

"""


def pattern3(n):
    for i in range(n):
        for j in range(i):
            print(' ', end=" ")
        for j in range(n):
            print('*', end=' ')
        print()


def pattern3_1(n):
    for i in range(n):
        for j in range(n):
            print('*', end=' ')

        print()
        print('  ' * i, end=' ')


# pattern3(14)

"""
           ******
           ******
           ******
           ******
Rectangle Star Pattern (rows, cols)

"""


def pattern4(r, c):
    for i in range(r):
        for j in range(c):
            print('*', end=' ')
        print()


#
# pattern4(6, 4)

"""
           ******
           *    *
           *    *
           ******
Hollow Rectangle Star Pattern

"""


def pattern5(r, c):
    for i in range(r):
        for j in range(c):
            if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()


#
# pattern5(4, 20)

"""
           ****
          ****
         ****
        ****
        
Mirrored Rhombus Star Pattern

"""


def pattern6(n):
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        for j in range(n):
            print('*', end='')
        print()


# pattern6(20)


"""
           *
           **
           ***
           ****
           
Triangle Star Pattern
"""


def pattern7(n):
    for i in range(n):
        print('*' * (i + 1))


#
# pattern7(12)

"""
   *
  ***
 *****
*******
           
Pyramid Star Pattern

"""


def pattern8(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        for j in range(2*i+1):
            print('*', end='')
        print()


pattern8(16)