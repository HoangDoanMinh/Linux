import time
a = time.localtime()
x=a[3]
print ("So Gio Hien Tai :" +str(x) + "h")
if(0<x & x<=9):
    print("Chao Buoi Sang")
if(9<x & x <= 12):
    print("Chao Buoi Trua")
if(12<x & x < 17):
    print("Chao Buoi Chieu")
