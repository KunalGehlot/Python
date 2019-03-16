name = ['India', 'Italy', 'Japan', 'Iran', ['China', 'Russia']]

for i in name:
    print(i)

for k in name:
    try:
        k.remove('China')
    except AttributeError:
        pass

for i in name:
    print(i)

number = [2, 4, 6, 8, 10]

sum = 1

for j in number:
    sum *= j

print(sum)
