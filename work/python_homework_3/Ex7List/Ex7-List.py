def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))

g = 'aabcddddadnss'
temp = list()
count = 1
index = 1
list_ = []
for x in g:
    try:
        if x == g[index]:
            count += 1
        else:
            if count == 1:
                temp.append(x)
                list_.append(x)
            else:
                temp.append([count,x])
                list_.append(count)
                list_.append(x)
                count = 1
        index += 1
    except IndexError:
        if count == 1:
            temp.append(x)
            list_.append(x)
        else:
            temp.append([count,x])
            list_.append(count)
            list_.append(x)
print(temp)
values = ', '.join(str(v) for v in list_)
save('real_output.txt', values)