for i in c02 c03 c04 c05 c06 c07 c08 c21 c22 c33 c34 
do
	echo "==see jps ${i}=="
	ssh ${i} jps
	echo " "
done
