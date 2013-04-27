package snippets.algorithms

object Count {
  def main(args: Array[String]) {
    val lc = new LogCount()
    Iterator.continually(lc.inc).takeWhile(_ < 33).foreach { i =>
      println(i)
    }
  }
}

class LogCount {
  // we store the exponent of the number (our actual count is 2^c)
  var c = 0
  val rng = new scala.util.Random()

  // we could store much larger numbers if we had some BigInt rng, or called the rng multiple times (we'd only need to do it c times) and just gave the result in 'count' as an exponent
  def inc() = {
    if (rng.nextInt(scala.math.pow(2,c).toInt) == 0)
      c = c + 1
    scala.math.pow(2, c).toInt
  }

  def count(): Int = {
    scala.math.pow(2, c).toInt
  }

  def reset() = {
    c = 0
  }
}
