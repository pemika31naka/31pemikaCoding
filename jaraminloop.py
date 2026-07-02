import random
print ("ยินดีต้อนรับสู่โปรแกรมทายเลขค่ะ \n")
random_number = random.randint(1,101)
count = 0
while True:

    guess = int(input("ทายตัวเลข  "))
    count += 1

    if guess > random_number :
        print("มากไป ลองใหม่")
    elif guess < random_number :
        print("น้อยไป ลองใหม่")
    else :
        print(f"ถูกต้อง เริ่ดมากค่ะ! ท้ายไปทั้งหมด {count} ครั้ง") 
        break
print ("\n By jasmin4/4 31")