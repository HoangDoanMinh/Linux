echo "Tinh Giai thua cua $1"
ia=1
GT=1
while [ $ia -lt $1 ]
do
ia=$(($ia +1))
GT=$(($GT*$ia))
done
echo "Giai thua cua $1 = $GT"
exit 0
