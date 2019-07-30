package ncku.ee.hpds

import org.apache.flink.api.java.utils.ParameterTool
import org.apache.flink.core.fs.FileSystem
import org.apache.flink.streaming.api.TimeCharacteristic
import org.apache.flink.streaming.api.scala._

import scala.collection.immutable.HashSet

//usage example:
//in Linux   bin/flink run -c ncku.ee.hpds.NetflowIPCount flink_project-1.0-SNAPSHOT.jar --input ./part-r-00000 --output ./count.txt

//in windows bin\flink.bat run -c ncku.ee.hpds.NetflowIPCount flink_project-1.0-SNAPSHOT.jar --input .\part-r-00000 --output .\count.txt

object NetflowIPCount {

  def main(args: Array[String]): Unit = {
    val parameters = ParameterTool.fromArgs(args)

    val env = StreamExecutionEnvironment.getExecutionEnvironment
    env.setStreamTimeCharacteristic(TimeCharacteristic.ProcessingTime)


    val inputStream = env.readTextFile(parameters.get("input")) // windows -> in log dir
    val ipstream = inputStream.map{ x =>
      var netflow = x.split("\t").toSeq

      //return
      netflow(4)
    }
    // filter words out which we have already seen
    // filterWithState need  (Boolean, Option[S])
    // seenWordsState => like a long-term  variable you can use to do some judgement or counting
    // true => word can pass through ; false => drop
    val uniqueWords = ipstream.keyBy(x => x).filterWithState {
      (word, seenWordsState: Option[Set[String]]) => seenWordsState match {
        case None => (true, Some(HashSet(word))) //initial state
        case Some(seenWords) => (!seenWords.contains(word), Some(seenWords + word)) //(false , hashset add duplicate elem.)
      }                                                                             //(true , hashset add new elem.)
    }
    //uniqueWords.print()


    // count the number of incoming (first seen) words
    val numberUniqueWords = uniqueWords.keyBy(x => 0).mapWithState {
      (word, counterState: Option[Int]) =>
        counterState match {
          case None => (1, Some(1)) //initial state
          case Some(counter) => (counter + 1, Some(counter + 1))
        }
    }.map{x=> var tmp = "Counting unique IP numbers :" + x.toString; tmp}

    numberUniqueWords.writeAsText(parameters.get("output"), FileSystem.WriteMode.OVERWRITE)



    env.execute()

  }}
