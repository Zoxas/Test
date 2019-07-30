for i in c02 c03 c04 c05 c06 c07 c08 c21 c22 c33 c34 
do
	echo "== now working at ${i} =="
	ssh ${i} 'tar -C  /home/hpds/feng/ -zxvf /home/hpds/feng/zookeeper-3.4.9.tar.gz'
	ssh ${i} 'tar -C /home/hpds/feng/ -zxvf /home/hpds/feng/kafka_2.10-0.10.0.1.tgz'
	ssh ${i} 'mv /home/hpds/feng/zookeeper-3.4.9/conf/zoo_sample.cfg  /home/hpds/feng/zookeeper-3.4.9/conf/zoo.cfg'
	ssh ${i} 'mkdir /home/hpds/feng/zookeeper-3.4.9/data'
	ssh ${i} 'mkdir /home/hpds/feng/zookeeper-3.4.9/datalog'
done
