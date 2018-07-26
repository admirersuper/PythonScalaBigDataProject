import java.io.FileWriter

import org.apache.spark.{SparkConf, SparkContext}
import org.json.JSONObject

import scala.collection.mutable.ListBuffer

object TaobaoAnalysisiSortedSales {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setMaster("local").setAppName("TaobaoData")
    val sc = new SparkContext(conf)
    val category = List[String]("50006842","50510002","50019251","50024101","50012162","50005961","50023095","50012404","50012010","50012018","50010406","50014457","50104002","50025009","50023096","50023100","50014494","50014493","50015943","50014502","50014500","50014503","50014496","50014495","50050549","50012118","50018600","50012582","50012583","50050591","50024124","50020186","50008661","50005759","50012665","50020521","50026786","50007167","50025908","50017184","50012324","50012941","50017266","50017597","50017785","50017763","50016752","50016666","50023530","50014081","50019122","50014499","50015985","50013898","50012406","50012408","50015878","50012410","50012411","50450021","50017549","50015325","50098003","50122002","50214002","50284001","50012663","50012107","50022048","50022136","50022158","50050588","50050592","50050595","50050629","50050633","50025912","50050345","50025917","50023169","50025928","50025944","50025945","50022666","50010621","50016708","50016727","50019154","50019155","50019157","50019223","50019160","50008588","50025044","50025046","50015086","121434005","121400005","121384005","121392003","122690003","122654005","121386020","121384022","121456019","121398019","121462024","121434026","121408014","121462042","121410039","121416004","122674011","121384023","121420023","121386021","121400017","121368020","121382028","121424021","121388027","121418021","121404036")
    val res = sc.textFile("taobao_data.txt")
      .filter(line=>{
        val isJson = line.startsWith("{\"")&&line.endsWith("}")
        //filter "stauts":hide
        var isShow = false
        if(isJson) {
          val json = new JSONObject(line)
          val status = json.getJSONObject("mods").getJSONObject("itemlist").getString("status")
          isShow = status.equals("show")
        }
        isJson&&isShow
      })
      .flatMap(line=>{
        val json = new JSONObject(line)
        val goods = json.getJSONObject("mods").getJSONObject("itemlist").getJSONObject("data").getJSONArray("auctions")
        var list = ListBuffer[JSONObject]()
        for(i<-0 to goods.length()-1){
          val cate = goods.getJSONObject(i).getString("category")
          val isTmall = goods.getJSONObject(i).getJSONObject("shopcard").getBoolean("isTmall")
          val view_price = goods.getJSONObject(i).getString("view_price").toFloat
          if(view_price>1670) {
            if(category.contains(cate)&&(isTmall)){
              list.append(goods.getJSONObject(i))
            }
          }
//          }else if(view_price>=415){
//            price_name = "415-1670元"
//          }else if(view_price>=76){
//            price_name = "76-415元"
//          }else if(view_price>=11){
//            price_name = "11-76元"
//          }else{
//            price_name = "11元以下"
//          }
//          if(category.contains(cate)&&(isTmall)){
//            list.append(goods.getJSONObject(i))
//          }
        }
        list
      }).count()
    println(res)
  }
}
