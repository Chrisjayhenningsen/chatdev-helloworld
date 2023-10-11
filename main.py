'''
This script creates a file named 'output.txt' and writes the string 'Hello, world!' to it.
'''
def create_file():
    with open('output.txt', 'w') as file:
        file.write('Hello, world!')
if __name__ == '__main__':
    create_file()