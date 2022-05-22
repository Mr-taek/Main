1. .moveTo() : it's absolute coordination depending on screens size
    - Argument
        1. x : coordinate of x axis
        2. y : coordinate of y axis
        3. duration : how long it take time to get to the coordiantes, it will take cursor being slow to move
    - return : None
2. .move(0) : it's relative coordination depending on the location where cursor pointed
    - Argument,return : same with .moveTo()

3. .click() : As a name it work clicking
    - Argument
        * Note : if there is no x,y argu, then following codes will follow current cursor location where it move
        1. x : Coordinate , if argument comes with Tuple or any sequance of Two coordination it will consider it as X,Y axis. Then no need of y argument
            - ex
            ```
            place=pt.moveTo(51,8)
            pt.click(place) # moveTo 가 51,8 을 리턴해서, 이 값을 받고 그 자리를 클릭.
            #pt.click(pt.position())
            ```
        2. y : - -
        3. clicks : How many times will click
        4. interval : How long will stop to click next
        5. duration : how long it take time to get to the coordiantes, it will take cursor being slow to move
    * Note 
        - .click() is result of thow func of .mouseDown() and .mouseUp()
4. .mouseDown() , .mouseUp() : both can use for Drag work
    - mouseDown : will stay by pressing mouse 
    - mouseUp : will remove pressing

5. .rightClick() : 오른쪽 마우스 클릭
6. .middleClick() : 휠클릭 누른 상태에서 위아래 스크롤 가능.
    - .scroll() : 그냥 마우스 스크롤 사용.
        - Argument
            1. clicks : 마우스 스크롤 위로 한 번이 1, 총 몇번 스크롤 할 것인 지 결정. + 는 위 , - 는 아래.
        - return : None
7. .drag() : 상대좌표 기준, 드래그 기능, 짬뽕가능. duration argu 필수.
    - ex
    ```
    pt.mouseDown(1689,10)
    pt.move(-200,0,duration=1) # if it's too fast then Drag won't work. that's a reason useing duration
    pt.mouseUp()
    ```
7. .dragTo() : 절대좌표 기준