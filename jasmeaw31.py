print ( "โปรแกรมคำนวณคะแนนรวม3วิชาค่ะ")
point1 = float(input ("คะแนนคณิตศาสตร์ของคุณคือ  : "))
point2 = float(input("คะแนนวิชาวิทยาศาสตร์ของคุณคือ   :  "))
point3 = float(input("คะแนนวิชาอังกฤษของคุณคือ  :  "  ))
total_point = ( point1 + point2 + point3)
average = total_point/3 

print ("คะแนนรวมของคุณคือ")
print ( total_point)

print ("คะแนนเฉลี่ยของคุณคือ")
print ( average )

if  average < 60 :
    print("ควรปรับปรุง")
elif  average < 80 :
    print("ผ่าน")
else : 
    print("ดีเยี่ยม")

print( "by jasmin 4/4 no.31 เองค่ะ")