# 그렇게 중요해 보이지 않아서 대충 넘김.
import numpy as np
b=np.array([ [[111,112], [121,122]], # 3차원은 배열의 연속... 
            [[211,212], [221, 222]], # 여길 보면 [[]] 로 되어있는데.. 즉 행열인데 이것들이 3개 있다 .. 즉 하나씩 나열해서 깊이를 만든다.
            [[311, 312],[321, 322]] # 3차원은 이렇게 직관적으로 이해는 된다만.....
            ])
print(b.ndim)
