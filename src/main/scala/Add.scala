package snippets.algorithms

// Ripple-carry adder, in software! :-)
object Adder {
  def main(args: Array[String]) {
    println(add(1,1))
    println(add(15,15))
    println(add(32432,438054))
  }

  def add(a: Int, b: Int): Int = b match {
    case 0 => a
    case _ => 
      val sum = a ^  b
      val carry = (a & b) << 1
      add(sum, carry)
  }
}

