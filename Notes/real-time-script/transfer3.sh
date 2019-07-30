declare -i x
x=2
for i in c02 c03 c04 c05 c06 c07 c08 c21 c22 c33 c34 
do
	echo "==set config at ${i}=="
	ssh ${i} "echo ${x} > /home/hpds/feng/zookeeper-3.4.9/data/myid"
	ssh ${i} "less /home/hpds/feng/zookeeper-3.4.9/data/myid"
	x=${x}+1
	scp /home/hpds/feng/zookeeper-3.4.9/conf/zoo.cfg hpds@${i}:/home/hpds/feng/zookeeper-3.4.9/conf/
	scp /home/hpds/feng/kafka_2.10-0.10.0.1/config/server.properties hpds@${i}:/home/hpds/feng/kafka_2.10-0.10.0.1/config/
done
