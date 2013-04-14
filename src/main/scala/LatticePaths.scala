package algorithms.roughgarden

/* Find # of lattice paths through an x*y lattice */

// writing this as a C-style dynamic program, just to get some practice

object LatticePaths{
  def main(args: Array[String]){
    val x = 4
    val y = 4
    val a = Array.fill(x,y){1}

    (0 until x).foreach{ i =>
      (0 until y).foreach{ j =>
        if(i == 0 || j == 0){
          a(i)(j) = 1
        } else {
          a(i)(j) = a(i-1)(j) + a(i)(j-1)
        }
      }
    }
    println(a.deep.mkString("\n"))
  }
}

