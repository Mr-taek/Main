1. Working with 64bit 

![화면 캡처 2022-08-03 154647](https://user-images.githubusercontent.com/77142512/182542421-f6c639bd-d283-44d1-9619-a772839706ed.png)


- plt.savefig()
    - parameter
        1. fname : file Path, format parameter가 지정되어도 반드시 확장자를 지정해야함. .pdf,.png 등이 있음.
        2. dpi : default는 100. figure의 인치당 도트 해상도
        3. facecolor : 서브플롯 바깥 배경 색상. 기본 값은 'w'(white)
        4. format : 명시적 파일 포멧 필요한 것 같지는 않다.
        5. bbox_inches : 'tight' 지정시 figure 둘레에 비어있는 공간을 모두 제거한다.
