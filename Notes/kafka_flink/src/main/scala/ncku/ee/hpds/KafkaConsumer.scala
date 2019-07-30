package ncku.ee.hpds

import java.util.Properties

import org.apache.flink.core.fs.FileSystem
import org.apache.flink.streaming.api.TimeCharacteristic
import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.windowing.time.Time
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer09
import org.apache.flink.streaming.util.serialization.SimpleStringSchema


object KafkaConsumer {

  def main(args: Array[String]): Unit = {

    val env = StreamExecutionEnvironment.getExecutionEnvironment
    env.setStreamTimeCharacteristic(TimeCharacteristic.ProcessingTime)

    val properties = new Properties()
    properties.setProperty("bootstrap.servers", "127.0.0.1:9092")
    //properties.setProperty("zookeeper.connect", "127.0.0.1:2181")
    properties.setProperty("group.id", "group1")
    properties.setProperty("auto.offset.reset","latest")

    val stream = env
      .addSource(new FlinkKafkaConsumer09[String]("udp_data", new SimpleStringSchema(), properties))
      //.map {x => ("group counting",1)}
      .map{x =>  if(x.length >1){("group counting",1)} else {("group counting",0)}}
      .keyBy(0)
      .timeWindow(Time.seconds(15))
      .sum(1)
      .writeAsText("/home/hpds/feng/group_out.txt", FileSystem.WriteMode.OVERWRITE)
    //if use print() --> output will be in yarn log-dir -> userlog



    env.execute("Flink Kafka Example")

  }

}
