package snippets.algorithms

object Subsets{
  def subsets(xs: List[Int]): List[List[Int]] = xs match {
    case Nil => List(List[Int]())
    case x::xs1 => subsets(xs1) ++ subsets(xs1).map{ys => x::ys}
  }

  def main(args: Array[String]){
    println(subsets(List(1,2,3)))
  }
}
