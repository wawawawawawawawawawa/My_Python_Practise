numbs = list()
a = 0
b = 1
i = 0
while i < 10:
    numbs.append(a)
    a, b = b, a + b
    i += 1
for numb in numbs:
    print(numb)