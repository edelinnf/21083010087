function panjang {
	echo "masukkan panjang bidang persegi :"
	read panjang
}
function lebar {
	echo "masukkan lebar bidang persegi :"
	read lebar
}
function luas {
	let luas=$panjang*$lebar
	echo "luas bidang persegi :"
	echo $luas
}
#Memanggil fungsi
panjang
lebar
luas
