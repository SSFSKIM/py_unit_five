#Steve
#11.03
a = []
b = 0
while True:
    p = input()
    if p == 'q':
        for i in a:
            b += i
        print(b/len(a))
        break
    a.append(int(p))
