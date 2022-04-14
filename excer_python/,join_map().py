# .join: list 에서 문자열로.
# map(dtype,variable): dtype으로 list 인덱스들의 type을 바꾼다. 변환 후엔 object 타입이므로 list든 튜플이든 dict든 형태변환을 시켜줘야 볼 수 있음.
a=[1,2,3,4,5]
c=list(map(str,a))
print(c)
b=','.join(c)
print(b,type(b))
