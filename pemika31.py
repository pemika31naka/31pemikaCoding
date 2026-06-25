print ("โปรแกรมตรวจสอบความปลอดภัยของความเร็วรถ \n")

speed = int(input("ค่าความเร็วรถของคุณคือ  :  "   ))

print ( "สถานะความปลอดภัยของคุณคือ   :   " )

if speed < 80 :
    print ("ปลอดภัย")

elif speed > 120 :
    print ("ผิดกฏหมาย (ปรับทันที)")

elif speed < 100 :
    print ("เตือน")

else :
    print (" เสี่ยงถูกปรับ ")

print ("\n By jasmin 4/4 no.31")