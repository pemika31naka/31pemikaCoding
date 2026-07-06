print("โปรแกรมเขียนสูตรคูณแม่เดี่ยวค่ะ  \n ")
num1 = int(input("ตัวเลขเริ่มต้นของคุณ   :  "))
num2 = int(input("ตัวเลขสุดท้ายของคุณ  :  "))

for m  in range (num1, num2 +1)  :
    print(f" \n [สูตรคูณแม่ {m}]")
    for i in range(1,13) :
        print(m,"x" ,i, "=" , m*i)

print (" \n By pemika 4/4 no.31")