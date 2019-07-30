for i in c02 c03 c04 c05 c06 c07 c08 c21 c22 c33 c34 
do
	echo "==see zookeeper state ${i}=="
	ssh ${i} 'echo stat|nc 127.0.0.1 2181'
	ssh ${i} 'echo ruok|nc 127.0.0.1 2181'
	echo " "
done


