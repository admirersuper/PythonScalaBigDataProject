

object AnalysisTwo {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("admirer").setMaster("local")
    val sc = new SparkContext(conf)
    val ls = sc.textFile("all_data_4.txt")  //ls为返回列表
    .filter(line=>line.endsWith("status\":1}"))
      .flatMap(line=>{
        val json = new JSONObject(line)
        val jsonlist = json.getJSONArray("data")
        val list = ListBuffer[JSONObject]()
        for(i<-0 to jsonlist.length()-
          1){
          list.append(jsonlist.getJSONObject(i))
        }
        list
      })
      .map(line=>{
        var code = line.get("major_code").toString()
        val plan = line.getString("plan").toInt
        if(code=="null") {
          code = "null"
        }
        (code,plan)
      })
      .reduceByKey(_+_)
      .sortBy(line=>line._2)
      .foreach(line=>println(line))
  }
}
