clear
echo "Nhap ten thu muc "
read a
mkdir $a
if test $? -eq 0;
then
echo "Da tao thu muc thanh cong"
else
echo "Khong the tao thu muc ten $a"
fi
