echo -n "Bilangan pertama = "
read bil1
echo -n "Bilangan kedua = "
read bil2
jumlah=`expr $bil1 + $bil2`
bagi=`expr $bil1 / $bil2`

echo "Jumlah kedua bilangan adalah $jumlah"
echo "Perkalian kedua bilangan adalah $bagi"

