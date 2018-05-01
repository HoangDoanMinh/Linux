ten = input("Nhap Ten Cua Ban : ")
tenn = int(input("Nhap So Luong Ten: "))
m = []
for i in range(0,tenn):
    print("Ten ",i+1)
    a = input()
    m.append(a)
for chon in m:
    if(chon in ten):
        print("Trung Ten")
        break
    else:
        print("Khong co ten nao trung voi ban")
