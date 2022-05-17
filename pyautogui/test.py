import pyautogui as pt


# 자동화중 시간ㅇ니 오래 걸리고..중간에 실패했을 때 중지를 해야하는데
# 일반적 파이썬은 ctrl +c 를 누르면 자동 종료가 됨.
# 그런데 이거는 메모장이니 excel이니 넘어가기 때문에 ctrl+c가 안 먹힘.
# 따라서 이럴 때는 .

for i in range(10):
    pt.move(100,100)
    pt.sleep(1)

    if i ==5:
        pt.moveTo(0,0)