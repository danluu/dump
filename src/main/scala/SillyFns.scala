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

  def main(args: Array[String]) = {
    println(byname(myTime()))
  }

}
