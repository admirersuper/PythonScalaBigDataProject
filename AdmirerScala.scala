

object AdmirerScala {
  def main(args: Array[String]): Unit = {
    println("heelo")
    System.out.println("java hello")
    //var变量 val常量
    val a = 3
    val b = 0.3f
    val c = 0.9d
    var d = "你好"
    var e = 'a'
    val f = true
    val a1 = Array(1,2,3,4,-10)
    val a2 = Array(1,2,4,'a',"b")
    val a3 = Array[Int](1,2,10)
    val b1 = List[Int](1,2,8)//list所有元素类型相同，且值一旦定义不可以更改
    val b2 = List[String]("a","b","c")
    //""
    val t1 = Tuple2(1,2)//元祖的值一旦定义也不可以改变，但是元素类型可以不同
    val t3 = ('a','b',1,"ad")//元祖也可以通过圆括号定义
    val t2 = Tuple2("1","2")//限定元祖长度为2，最大22
    //print elements
    println(a,b,c);
    println(a1(1),a2(1),a3(2)) //数组不能直接输出
    println(b1) //列表能直接输出
    println(b2(2))//通过圆括号下标访问元素
    println(f)
    println(t3)//元祖也能直接输出
    //access elements
    println(b1(2))
    println("元祖t1的第一个第二个元素："+t1._1+","+t2._2)
    println(a3(0)+a3(1))//+号一定要匹配的类型才能一起用
//    new JSONObject()
    val writer = new PrintWriter(new File("test.txt" ))
    writer.write(t2.toString())//t2._1+" "+t2._2+"\n"
    writer.write("hello")
    writer.close()
  }
}
