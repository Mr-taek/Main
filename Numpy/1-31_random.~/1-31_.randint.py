# np.random.randint(low,high,size,dtype=l)
#정수만 가능, low~high 까지의 정수를 출력, 사이즈는 탠서개념가 같음. 그러나 소괄호() 로 묶어줘야함.
#If `high` is None (the default), then results are from [0, `low`). 0을 포함하고 low보다 미만인 수가 생성, 이것이 디폴트값이고,randint(low)만 치면 됨.

import numpy as np
a=np.random.randint(0,10,size=(5,5))
print(type(a[0]))
