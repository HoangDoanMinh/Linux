from BaiTap5 import PhepToan
mang = []
m = input("Moi Ban Nhap So Thu Nhat :")
b = input("Moi Ban Nhap So Thu Hai :")
BaiTap5 = PhepToan(m,b)
mang.append(Minha)
a = int(input("Moi Ban Nhap phep toan :\n"
          "1. Phep Cong\n"
          "2.Phep Tru\n"
          "3.Phep Nhan\n"
          "4.Phep Chia\n"
          "5.close\n"
          "--------------------------------------\n"))
if(a == 1):
    print("Ban vua chon Phep cong")
    k = BaiTap5.PhepCong()
    print("KQ cua phep toan = ",k)
if(a == 2):
    print("Ban vua chon Phep Tru")
    kk=BaiTap5.PhepTru()
    print("KQ cua phep toan = ", kk)
if(a == 3):
    print("Ban vua chon Phep Nhan")
    kq = BaiTap5.PhepNhan()
    print("KQ cua phep toan = ", str(kq))
if(a == 4):
    print("Ban vua chon Phep Chia")
    kqq = BaiTap5.PhepChia()
    print("KQ cua phep toan = ", kqq)
if(a==5):
    print(output)
