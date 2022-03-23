yours = input('Input your file name: ')

with open(yours, 'r') as files:
    res = len(files.readlines())
    print('Total lines:', res)

with open('output.txt', 'w') as files:
    files.write(str(res))  