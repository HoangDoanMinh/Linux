
echo “Chuong trinh tinh tong 1-$1”
tong=0
ia=0
while [ $ia -lt $1 ]
do
ia=$(($ia + 1))
tong=$(($tong + $ia))
done
echo "Tong 1-$1= $tong"
exit
