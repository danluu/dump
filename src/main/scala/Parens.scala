package snippets.algorithms

// Generate all valid combinations of n-pairs of parens
// We'll think of these as lattice paths where we can move right or up
// right => "("
// up    => ")"
// But we then have to reverse the parens, because 
// List("").map{s => s + "1"}.map{s => s + "2"} = List("12")

object Parens {
  def parens(n: Int, x: Int, y: Int): List[String] = {
    if (x + y == 2*n) {
      List[String]("")
    } else if (x == n) {
      parens(n, x, y + 1).map(s => s + "(")
    } else if (x == y) {
      parens(n, x + 1, y).map(s => s + ")")
    } else {
      parens(n, x, y + 1).map(s => s + "(") ++ parens(n, x + 1, y).map(s => s + ")")
    }
  }

  def solve(n :Int) = parens(n, 0, 0)

  def main(args: Array[String]){
    println(solve(1))
    println(solve(2))
    println(solve(3))
  }
}
