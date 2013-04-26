package snippets.algorithms

import scala.collection.mutable

// Note: these algorithms are both n^2. There's an n log n algorithm
// scan linearly through the array
// we keep a side vector and maintiain the invariant that, on iteration i, side(n)
// is the highest number in xs(0:i) that completes a subsequences of length n
// we can update the side vector by binary searching and inserting at the right location,
// hence the log n

object LIS {
  def main(args: Array[String]) {
    println(solve(Array(7,3,8,4,2,6,7)))
    println(solveMemo(Array(7,3,8,4,2,6,7)))
  }

  // 1-d dynamic programming
  // keep track of all lengths. New max is max of all previous + 1,
  // for all elements that are < current
  def solve(xs: Array[Int]) = {
    val len = Array.fill(xs.length){0}
    val prev = Array.fill(xs.length){0}
    (1 until xs.length).foreach{ i =>
      val sublen = len.slice(0,i).zipWithIndex.map{ x =>
        if(xs(x._2) < xs(i)) //prev < current, so inc prev longest and save the index
          (1 + x._1, x._2)
        else 
          (1, i)
      }
      len(i) = sublen.maxBy(_._1)._1
      prev(i) = sublen.maxBy(_._1)._2
    }
    println(prev.mkString(" "))
    len.max
  }

  // try memoizing rather than explicitly walking through a table
  def solveMemo(xs: Array[Int]) = {
    // length and where we came from
    var mem: mutable.Map[Int, (Int, Int)] = mutable.Map.empty

    cost(xs.length-1)
    def cost(c: Int): (Int, Int) = {
      mem.get(c) match {
        case None =>
          val subCost = (0 until c).map{ i =>
            if(xs(c) > xs(i))
              (1 + cost(i)._1, cost(i)._2)
            else
              (1, i)
          }
          val len = subCost.maxBy(_._1)._1
          val prev = subCost.maxBy(_._1)._2
          mem(c) = (len,prev)
          (len, prev)
        case Some(n) => n
      }
    }
    mem
  }
}
