for i in c02 c03 c04 c05 c06 c07 c08 c21 c22 c33 c34 
do
	echo "==transfer to ${i}=="
	scp /home/hpds/feng/zookeeper-3.4.9.tar.gz hpds@${i}:/home/hpds/feng
	scp /home/hpds/feng/kafka_2.10-0.10.0.1.tgz hpds@${i}:/home/hpds/feng
	scp /home/hpds/feng/hadoop-2.7.2/etc/hadoop/*.xml hpds@${i}:/home/hpds/feng/hadoop-2.7.2/etc/hadoop/
	scp /home/hpds/feng/hadoop-2.7.2/etc/hadoop/*.sh hpds@${i}:/home/hpds/feng/hadoop-2.7.2/etc/hadoop/
	scp /home/hpds/feng/hadoop-2.7.2/etc/hadoop/slaves hpds@${i}:/home/hpds/feng/hadoop-2.7.2/etc/hadoop/
done
