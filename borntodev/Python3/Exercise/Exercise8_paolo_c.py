usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "1234" and passwordInput == "1234":
    print("-----Hello-----")
    print("1. โปรแกรมคำนวณภาษี")
    print("2. โปรแกรมคำนวณผลรวม")
    chooseInput = input("เลือกโปรแกรม : ")
    if chooseInput == "1":
        vat = 7
        priceInput = int(input("ราคาสินค้า : "))
        sum = priceInput+(priceInput*7/100)
        print("ราคารวม Vat :",sum,"บาท")
    elif chooseInput == "2":
        priceInput1 = int(input("ราคาสินค้า 1 :"))
        priceInput2 = int(input("ราคาสินค้า 2 :"))
        print("ราคารวม : ",priceInput1+priceInput2,"บาท")
    else:
        print("คุณเลือกไม่ถูกต้อง")
else:
    print("รหัสผ่านผิด")