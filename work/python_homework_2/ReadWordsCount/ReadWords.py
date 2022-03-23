your = input('input your file name: ')
num = 0

with open(your,'r') as files:
	data = files.read()
	lines = data.split()
	num += len(lines)
print(num)

with open('output.txt', 'w') as files:
    files.write(str(num))