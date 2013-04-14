package snippets.algorithms

import scala.math.min

class Elevator{
}

object Elevator{
  def main(args: Array[String]){
    val numFloorsReal = 10
    val numStopsReal = 3
    val numFloors = numFloorsReal + 1
    val numStops = numStopsReal + 1
    val a = Array.fill(numFloors,numStops){Int.MaxValue} //table of costs
    val p = Array.fill(numFloors,numStops){-1} //table of parents

    val destinations = Array(0,1,4,4,8,10)

    def floorsWalked(prev: Int, curr: Int) = {
      var nsteps = 0;
      destinations.foreach{ s =>
        if (s > prev && s <= curr) {
          nsteps = nsteps + min(s - prev, curr - s)
        }
      }
      nsteps
    }

    (0 until numFloors).foreach { i =>
      println(s"initial loop ${floorsWalked(i, Int.MaxValue)}")
      a(i)(0) = floorsWalked(0, Int.MaxValue)
    }

    println(s"Starting main loop")
    (0 until numFloors).foreach { i =>
      (1 until numStops).foreach { j =>         
        var cost = Int.MaxValue
        (0 until (i+1)). foreach { k => 
          if (i == 2 && j == 1) {
            println(s"floor=${i} numStops ${j} ${k}: ${a(k)(j-1)} - ${floorsWalked(k, Int.MaxValue)} + ${floorsWalked(k, i)} + ${floorsWalked(i, Int.MaxValue)}")
          }
          cost = a(k)(j-1) - floorsWalked(k, Int.MaxValue) + floorsWalked(k, i) + floorsWalked(i, Int.MaxValue)
          if (cost < a(i)(j)) {
            a(i)(j) = cost
            p(i)(j) = k
          }
        }

      }
    }

    println(a.deep.mkString("\n"))
    println(p.deep.mkString("\n"))

    var lastStop = 0;
    (1 until numFloors).foreach { i =>
      println(s"Trying ${i} ${numStops}, ${lastStop} ${numStops}")
      if(a(i)(numStops - 1) < a(lastStop)(numStops - 1))
        lastStop = i
    }

    (0 until numFloors).foreach { i =>
      (0 until numStops).foreach { j => 
        print(a(i)(j))
        print("\t\t")
      }
      println("")
    }

    def findStops(lastStop: Int, n: Int): Unit = {
      println(lastStop)
      n match {
        case 0 => 
        case m => findStops(p(lastStop)(m), m-1)
      }
    }

    println("Stops")
    findStops(lastStop, numStops-1)
  }
}
