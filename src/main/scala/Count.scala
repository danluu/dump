package snippets.algorithms

// Note: we can do better, using HyperLogLog: http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf

// TODO: write this down in Verilog.
// For implementing performance counters (or counter where we can sacrifice precision), we can use a Linear Counter or a HyperLogLog counter
// if we want perfect precision at low counts we can have an extra bit, and flip into imprecise mode when we overflow the regular counter.
// This seems often superior to the current x86 perf counter mechanism for events that may happen very often, in terms of storage space
// We often don't need a perfect count for counters that get very large, so we can save some bits, which usually matters more in hardware than in software

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
    Iterator.continually(linc.inc).takeWhile(_ < 200.0).foreach { i =>
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


  // for len = k,
  // Pr(bit i == 0) after hashing on item: 1 - 1/k
  // after n items: (1 - 1/k)^n
  // by linearity of expectation, E[empty] = k(1 - 1/k)^n
  // lim as k,n -> inf
  // k(1 - 1/k)^n = 
  // by log transform + L'Hopital's rule
  // ke^(-n/k)
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
