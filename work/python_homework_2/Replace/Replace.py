a = input('Input your file: ')
b = input('Your output file: ')
with open(a, 'r') as infile, \
     open(b, 'w') as outfile:
    data = infile.read()
    data = data.replace("\\n", "")
    outfile.write(data)
