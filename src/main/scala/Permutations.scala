package snippets.algorithms

object Permutations{
  def removeOne(x: Int, xs: List[Int]) = xs diff List(x)

  def permsRecursive(xs: List[Int]): List[List[Int]] = xs match {
    case Nil => List(List[Int]())
    case _ => xs.flatMap{x =>
      permsRecursive(removeOne(x,xs)).map{ys => x::ys}
    }
  }

  def main(args: Array[String]){
    println(permsRecursive(List(1,2,3)))
  }
}
