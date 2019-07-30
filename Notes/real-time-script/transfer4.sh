echo "==set myid at c02 =="
ssh c02 'echo 2 > /home/hpds/feng/zookeeper-3.4.9/data/myid'
echo "==set myid at c03 =="
ssh c03 'echo 3 > /home/hpds/feng/zookeeper-3.4.9/data/myid'
echo "==set myid at c04 =="
ssh c04 'echo 4 > /home/hpds/feng/zookeeper-3.4.9/data/myid'
echo "==set myid at c05 =="
ssh c05 'echo 5 > /home/hpds/feng/zookeeper-3.4.9/data/myid'
echo "==set myid at c06 =="
ssh c06 'echo 6 > /home/hpds/feng/zookeeper-3.4.9/data/myid'
echo "==set myid at c07 =="
ssh c07 'echo 7 > /home/hpds/feng/zookeeper-3.4.9/data/myid'
echo "==set myid at c08 =="
ssh c08 'echo 8 > /home/hpds/feng/zookeeper-3.4.9/data/myid'
echo "==set myid at c21 =="
ssh c21 'echo 9 > /home/hpds/feng/zookeeper-3.4.9/data/myid'
echo "==set myid at c22 =="
ssh c22 'echo 10 > /home/hpds/feng/zookeeper-3.4.9/data/myid'
echo "==set myid at c33 =="
ssh c33 'echo 11 > /home/hpds/feng/zookeeper-3.4.9/data/myid'
echo "==set myid at c34 =="
ssh c34 'echo 12 > /home/hpds/feng/zookeeper-3.4.9/data/myid'

declare -i x
x=2
for i in c02 c03 c04 c05 c06 c07 c08 c21 c22 c33 c34 
do
	echo "==set config at ${i}=="
	ssh ${i} "echo ${x} > /home/hpds/feng/zookeeper-3.4.9/data/myid"
	ssh ${i} "less /home/hpds/feng/zookeeper-3.4.9/data/myid"
	x=x+1

done



