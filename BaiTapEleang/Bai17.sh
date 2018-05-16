echo "Tinh giai thua cua $1"
GT=1
i=1
while [ $i -lt $1 ]
do
	i=$(($i + 1))
	GT=$(($GT * $i))
done
echo "Giai thua cua $1 =$GT"
exit 0
