def make_sqaure(size):
  for i in range(size):
    print("*" * size)

def make_rectangle(length, width):
  for i in range(length):
    print("*" * width)

def make_triangle(size):
  for i in range(1,size*2,2):
    print("."*(size-1) + "*"*i + "."*(size-1))
    size-=1

def main():
    while(True):
        print('Hello, please enter what to print')
        print('1\tsquare')
        print('2\trectangle')
        print('3\ttriangle')
        shape = (int)(input('Input: '))
        if(shape == 1):
            size = (int)(input('Input size:'))
            make_sqaure(size)
        elif(shape == 2):
            length = (int)(input('Input length: '))
            width = (int)(input('Input width: '))
            make_rectangle(length, width)
        elif(shape == 3):
            size = (int)(input('Input size: '))
            make_triangle(size)

main()
