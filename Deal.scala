

object Deal {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("admirer").setMaster("local")
    val sc = new SparkContext(conf)
    val ls = sc.textFile("all_data_4.txt")  //ls为返回列表
      .filter(line=>line.endsWith("status\":1}"))
          .flatMap(line=>{
            val json = new JSONObject(line)
            val jsonlist = json.getJSONArray("data")
            val list = ListBuffer[JSONObject]()
            for(i<-0 to jsonlist.length()-1){
              list.append(jsonlist.getJSONObject(i))
            }
            list
          })
          .map(line=>(line.getString("school"),line.getString("plan").toInt))
          .reduceByKey(_+_)
//          .sortBy(line=>line._2,false)
        .take(2300)
    val writer = new FileWriter("group4_data_unsorted.txt")
    for(i<-0 to ls.length-1){
      writer.write(ls(i)._1+","+ls(i)._2+"\n")
    }
    //ls(i):(嘉兴学院南湖学院,1500)类似
    //访问第一个位置的就是ls(i)._1
    //访问第二个位置的就是ls(i)._2
    writer.close()
  }
}
