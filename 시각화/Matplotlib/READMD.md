1. Worked by 64bit 

2. SUBPLOTS 예시
    1. EX 1)
        ```
        fig,axis=plt.subplots(2,2) -> 2행2열로 subplot이 만들어짐
        for i in range(2):
            for j in range(2):
                axis[i,j].hist/scatter(~)
        plt.show()
        ```