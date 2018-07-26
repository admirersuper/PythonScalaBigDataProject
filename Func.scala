

object Func {
  /**
    *Syntax1:Normal Functions
    *def FuncName(variable:Type)[:ReturnValueType]={
    *   //functions
    *   [return]Value
    *}
    */
  /**
    * Syntax2：lambda Functions
    * var func = (var1:Type,var2:Type,...)=>returnValue
    */
  /**
    * Syntax3:OneInstruction Functions
    * def FuncName(var1:Type,var2:Type,...)[:ReturnValueType]=OneInstruction
    */
  /**
    * Syntax4:Closure
    * def FuncName(var1:Type,var2:Type,...,opt:Type=DefaultValue)[:ReturnValueType]={
    *   //operations with opt
    * }
    */
  def main(args: Array[String]): Unit = { //unit 相当于返回值为空
    //Syntax1
    def addSyntax1(a:Int,b:Int):Int={
      a+b
    }
    println("Syntax1:a+b="+addSyntax1(56,88))
    //Syntax2
    val add2 = (a:Int,b:Int)=>a+b
    println("Syntax2:a+b="+add2(56,88))
    //Syntax3
    def addSyntax3(a:Int,b:Int)=a+b
    println("Syntax3:a+b="+addSyntax3(56,88))
    //Syntax4
    def addSyntax4(a:Int,b:Int,opt:String="+"):Int={
      a+b
    }
    println("Syntax4:a+b="+addSyntax4(56,88,"+"))
  }
}
