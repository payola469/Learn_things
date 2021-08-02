correntNumber = 10
userinput = 0
while userinput != correntNumber:
    userinput = int(input("กรุณาสุ่มตัวเลข : "))
    if userinput > correntNumber:
        print("มากไป")
    elif userinput < correntNumber:
        print("น้อยไป")
    elif userinput == correntNumber:
        print("ถูกแล้ววววว")