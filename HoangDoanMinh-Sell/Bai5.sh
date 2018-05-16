echo "Cong(+)";
echo "Tru(-)";
echo "Nhan(*)";
echo "Chia(/)";
echo "Thoat(q)";
echo -n "Ban chon phep tinh nao?";
read choose;
choose1="''$choose''"
if [ $choose1 != "''*''" ];
then
choose1=$choose;
fi

if [ $choose1 != "q" ]
then
if [ $choose1 = "+" -o $choose1 = "-" -o $choose1 = "''*''" -o $choose1 = "/" ]; then
echo -n "Nhap so thu nhat : "; read a;
echo -n "Nhap so thu hai : "; read b;
KQ="";
case $choose1 in
"+") KQ=$[ $a + $b ];;
"-") KQ=`expr $a - $b`;;
"''*''") KQ=`expr $a \* $b`;;
"/") KQ=`expr $a / $b`;;
*) echo "" ;
esac
echo "Ket qua =" $KQ;
fi
fi

