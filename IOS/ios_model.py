import io
import os

arr = ['a1', 'a2', 'a3']

if __name__ == '__main__':
    workingspace = os.getcwd()
    print('workingspace is:', workingspace)
    # os.rmdir('source')
    # os.mkdir('source')
    ios = open('source/1.txt', 'w+')
    for x in arr:
        ios.write(x + '\n')
    ios.close()