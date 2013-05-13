package snippets.algorithms

// Tree problem from Raul

sealed trait MultiTree 
case class Leaf(x: Int) extends MultiTree
case class MNode(nodes: List[MultiTree]) extends MultiTree

class FoundMatch(message: String = null, cause: Throwable = null, item: Int) extends RuntimeException(message, cause)

object MTreeToy {
  def main(args: Array[String]) = {
    val t = MNode(List(Leaf(0), Leaf(1), Leaf(2), 
      MNode(List(
        MNode(List
          (Leaf(3), Leaf(4))),
        Leaf(5), Leaf(6)))))
    println(find(t, 3))
  }

  def find(t: MultiTree, x: Int) = {
    try {
      findHelper(t, x)
      None
    } catch {
      case FoundMatch(item=y) => Some(y)
    }
  }

  def findHelper(t: MultiTree, x: Int): Int = t match {
    case Leaf(y) => 
      if (x == 0)
        throw new FoundMatch(item = y)
      else 
        1
    case MNode(l) =>
      var i = 0
      l.foreach{ n =>
        val temp = findHelper(n, x - i)        
        i = i + temp
      }
      i
  }
}
