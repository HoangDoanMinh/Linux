clear
function Nhap()
{
	echo "Nhap n: "
	read n
	for((i=0 ; i< n ; i++))
	do
		echo "a[$i] ="
		read a[$i]

	done
}
function SoLonNhatGiua2So()
{
	if( $1 -gt $2 );
	then
	max1=$1
	echo $1
	else
	max1=$2
	echo $2
	fi
return $max1
}
function SoLonTrongDay()
{
	max=${a[0]}
	for(( i=1 ; i<n ; i++ ))
	do
	max=$(SoLonNhatGiua2So ${a[$i]} $max)
	done
	echo "Max = $max"
}
Nhap
SoLonTrongDay

