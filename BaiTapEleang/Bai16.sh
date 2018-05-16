echo "Tinh Tong tu 1 toi $1"
tong=0
i=0
while [ $i -lt $1 ]
do
	i=$(($i + 1 ))
	tong=$(($tong + $i))
done
echo "Tong tu 1 toi $1 = $tong"
exit 0
