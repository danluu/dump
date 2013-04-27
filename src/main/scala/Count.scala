package snippets.algorithms

object Count {
  def main(args: Array[String]) {
    val lgc = new LogCount()
    var realI = 0
    Iterator.continually(lgc.inc).takeWhile(_ < 33).foreach { i =>
      realI = realI + 1
      println(s"${realI} ${i}")
    }

    val linc = new LinearCounter(100)
    realI = 0
    Iterator.continually(linc.inc).takeWhile(_ < 33.0).foreach { i =>
      realI = realI + 1
      println(s"${realI} ${i}")
    }
  }
}

class LinearCounter(len: Int) {
  val rng = new scala.util.Random()

  // using a java bitset because it has a built in cardinality method
  // we could calculate cardinality pretty easily, but why?
  val bits = new java.util.BitSet(len)

  def count(): Double = {
    if (len == bits.cardinality()) {
      Double.PositiveInfinity
    } else {
      len.toDouble * math.log(len.toDouble / (len.toDouble - bits.cardinality()))
    }
  }

  // if we were counting items, we'd want to use the hashcode for the items here
  def inc(): Double = {
    bits.set(rng.nextInt(len))
    count()
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
