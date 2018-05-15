echo "Nhap so thu nhat :"
read a
echo "Nhap so thu hai :"
read b
let "c=$a +$b"
let "d = $a - $b"
let "e = $a * $b"
echo "Tham so ban vua truyen vao la : $a , $b"
echo "$a + $b =$c"
echo "$a - $b =$d"
echo "$a * $b =$e"
if test $b -eq 0;
then
echo "Khong chia duoc"
else
let "ee = $a % $b"
let "eee = $a / $b"
echo "$a % $b =$ee"
echo "$a / $b =$eee" 
fi
