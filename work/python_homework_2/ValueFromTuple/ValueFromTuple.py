def save(filename, x):
    with open(filename, 'w') as fn:
        fn.write(str(x))
def remove():
	Tuple1 = (11, [22, 3, 33, 7], 44, 55, 105)

	a = Tuple1[1]
	a.insert(1,Tuple1[2])
	save('output.txt', a)
	print(a)

def main():
	remove()

if __name__ == '__main__':
	main()