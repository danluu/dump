package snippets.algorithms

// View permutations as x/y coords. There are no row-row or col-col conflicts, so we only need to check diagonals
// y = x + c or y = -x + c => c = y - x or c = y + x. If there's a collision, that's a bad solution

object NQueens {
  def solve(n: Int) = {
    (0 until n).permutations.filter { p =>
      val xy = p.zipWithIndex
      (xy.map{x => x._1 + x._2}.toSet.size == n) && (xy.map{x => x._2 - x._1}.toSet.size == n)
    }.toList
  }

  def main(args: Array[String]){
    println(solve(8).length)
  }
}
