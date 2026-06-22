print ( "โปรแกรมคำนวณคะแนนรวม \n " )
Science = int(input("คะแนนวิชาวิทยาศาสตร์ของคุณคือ  "))
Physics = int(input("คะแนนวิชาฟิสิกส์ของคุณคือ  "))
Math= int(input("คะแนนวิชาคณิตศาสตร์ของคุณคือ  "))
total_point = ( Science + Physics + Math )
average =  total_point/3  
print ( "คะแนนรวมของคุณในครั้งนี้ \nคือ " , total_point , " คะแนน " )
print ( "คะแนนเฉลี่ยของคุณในครั้งนี้ \nคือ " , average , " คะแนน " )
if average < 60 :
    print ("ควรปรับปรุง")

elif average > 80 :
    print ("ดีเยี่ยม")
else :
    print ("ผ่าน")

print (" By pemika no.31 M.4/4")