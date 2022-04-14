def sum(*argu):  # 몇개의 인자가 들어와도 ㅇㅋ, 튜플형태로 들어오나봄
    sum=0
    for i in range(len(argu)):
        sum+=argu[i]
    return sum


print(sum(1,2,3,4,5,6,2,1,2,23,1))

