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

    // 1. find largest k such that xs(k) < xs(k+1)
    var k: Int = -1
    (0 until (xs.length - 1)).foreach{ i =>
      if(xs(i) < xs(i+1))
        k = i
    }

    // 2. find largest l such that xs(k) < xs(l). We know this must exist, because xs(k) < xs(k+1)
    var l = -1
    if (k >= 0) {
      (0 until (xs.length)).foreach { i =>
        if (xs(k) < xs(i))
          l = i
      }
    }

    // 3. swap xs(k) and xs(l) and then reverse xs(k+1:)
    // from '1', we know that xs(k+1:) is decreasing, so reversing it will give us the smallest perm
    if (k >= 0) {
      swap(k,l)
      val base = k + 1
      var i = 0
      while(i + base < xs.length - i - 1) {
        swap(i + base, xs.length - i - 1)
        i = i + 1
      }
      return Some(xs)
    } else {
      return None
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
