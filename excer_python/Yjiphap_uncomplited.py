a=[1,2,3,2,2,4,1,2,3,5,123,123,2,13,412,5,5,66,23]
b=[125,12,3,2,31,2245,1,25,2,34,123,12,31,5,52,6,435,73,1]

c=a+b

if len(a)>len(b):
    for i in a:
        if i in b:
            if i in c:
                while i not in c:
                    c.remove(i)
elif len(a)<len(b):
    for i in b:
        if i in a:
            if i in c:
                while i not in c:
                    c.remove(i)
else:
    for i in b:
        if i in a:
            if i in c:
                while i in c:
                    c.remove(i)
c.sort()
print(c)