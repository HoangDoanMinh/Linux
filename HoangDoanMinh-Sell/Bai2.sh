clear
echo -n "Moi Nhap Ho cua ban :"
read ho
echo -n "Moi Nhap Ten cua ban :"
read ten
if [ $ho = "hoangdoan" -a $ten = "minh" ] 
then
echo "Xin Chao $ho $ten"
else
echo "Khong trung voi ten cua ban"
fi

