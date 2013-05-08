package snippets.algorithms

object SillyFns {

  def myTime() = {
    println("Getting time")
    System.nanoTime
  }

  def byname(t: => Long) = {
    println(s"byname t=${t}")
    t
  }

  def main(args: Array[String]): Unit = {
    println(byname(myTime()))
    println(List(41, "cat") collect { case i: Int ⇒ i + 1 })
    println(List("abc","aa","bo","foo","!").groupBy(_.length))
  }

}
