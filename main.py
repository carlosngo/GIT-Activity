def make_sqaure():
    pass

def make_rectangle():
    pass

def make_triangle():
    pass

def main():
    print('Hello, please enter what to print')
    print('1\tsquare')
    print('2\trectangle')
    print('3\ttriangle')
    shape = (int)(input('Input: '))
    if(shape == 1):
        make_sqaure()
    elif(shape == 2):
        make_rectangle()
    elif(shape == 3):
        make_triangle()

main()