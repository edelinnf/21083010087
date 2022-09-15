echo "Bilangan pertama a= "
read a
echo "Bilangan kedua b= "
read b

if [ $a -eq $b ]
then
	echo "$a sama dengan $b"
elif [ $a -gt $b ]
then
	echo "$a lebih dari $b"
elif [ $a -lt $b ]
then
	echo "$a kurang dari $b"
else
	echo "Tidak ada kondisi yang memenuhi"
fi

