package snippets.algorithms

object Permutations{
  def removeOne(x: Int, xs: List[Int]) = xs diff List(x)

  def permsRecursive(xs: List[Int]): List[List[Int]] = xs match {
    case Nil => List(List[Int]())
    case _ => xs.flatMap{x =>
      permsRecursive(removeOne(x,xs)).map{ys => x::ys}
    }
  }


  // This is highly non-idiomatic
  def permsLexicographic(xs: List[Int]): List[List[Int]] = {    
    var first = xs.toArray
    var nextPerm = nextPermLexicographic(first)
    var result: List[List[Int]] = List(xs)
    while(nextPerm != None) {      
      result = nextPerm.get.toList :: result
      println(nextPerm.get.toList)
      nextPerm = nextPermLexicographic(nextPerm.get)
    }
    result.reverse
  }

  def nextPermLexicographic(xs: Array[Int]): Option[Array[Int]] = {
    def swap(i: Int, j: Int) = {
      val temp = xs(i)
      xs(i) = xs(j)
      xs(j) = temp
    }

    var k: Option[Int] = None
    (0 until (xs.length - 1)).foreach{ i =>
      if(xs(i) < xs(i+1))
        k = Some(i)
    }

    val l = k match {
      case None => None
      case Some(i) => 
        var ll: Option[Int] = None
        val x = xs(i)
        (0 until (xs.length)).foreach { i =>
          if (x < xs(i))
            ll = Some(i)
        }
        ll
    }

    (k,l) match {
      case (None,None) => return None
      case (Some(k), Some(l)) => swap(k,l)
//        println(s"k l ${k} ${l}")
        val base = k + 1
        var i = 0
//        println(s"reverse? i+b:${i + base} len:${xs.length} j:${xs.length - i - 1}")
//        println(s"pre-reverse ${xs.mkString(" ")}")
        while(i + base < xs.length - i - 1) {
//          println(s"swapping ${i+base} ${xs.length - i - 1}")
          swap(i + base, xs.length - i - 1)
          i = i + 1
        }
//        println(s"post-reverse ${xs.mkString(" ")}")
      return Some(xs)
    }
  }

  def main(args: Array[String]){
    println(permsRecursive(List(1,2,3)))
    println(nextPermLexicographic(Array(3,2,1)))
    println(nextPermLexicographic(Array(1,2,3)).get.mkString(" "))
    println(nextPermLexicographic(Array(1,4,3,2)).get.mkString(" "))
    println(permsLexicographic(List(1,2,3,4)))
    println(permsLexicographic(List(1,2,3,4)).length)
    println(permsRecursive(List(1,2,3,4)).length)
  }
}
