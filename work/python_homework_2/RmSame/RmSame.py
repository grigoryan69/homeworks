def save(filename, x):
    with open(filename, 'w') as fn:
        fn.write(str(x))
def remove():
	Set1 = {10, 20, 7, 36, 30}
	print('Set1 contais:', Set1)
	Set2 = {20, 36, 40, 3, 50}
	print('Set2 contais:', Set2)
	result = [] 
	for rm in Set1:
		for sec in Set2:
			if id(rm) == id(sec):
				result.append(rm)			
				
	print('the similarity between Set1 and Set2 is:', result)
	TheRes = set(result)
	Set1 = Set1 - TheRes
	print('now Set1 contains:', Set1)
	save('output.txt', Set1)

def main():
	remove()

if __name__ == '__main__':
	main()