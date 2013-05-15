package snippets.algorithms

// Tree problem from Raul

sealed trait MultiTree 
case class Leaf(x: Int) extends MultiTree
case class MNode(nodes: List[MultiTree]) extends MultiTree

sealed trait PolyReturn
case class Continue(x: Int) extends PolyReturn
case class Found(x: Int) extends PolyReturn

case class FoundMatch(message: String = null, cause: Throwable = null, item: Int) extends RuntimeException(message, cause)

object MTreeToy {
  def find(t: MultiTree, x: Int) = {
    def findHelper(t: MultiTree, x: Int): Int = (t, x) match {
      case (Leaf(y),  0) => throw new FoundMatch(item = y)
      case (Leaf(y),  _) => 1
      case (MNode(l), _) =>
        var i = 0
        l.foreach{ n => i = i + findHelper(n, x - i) }
        i
    }
    try {
      findHelper(t, x); None
    } catch {
      case FoundMatch(_, _, y) => Some(y)
    }
  }

  // inspiried by Raul
  def findImmutable(t: MultiTree, x: Int) = {
    def findImmutableHelper(t: MultiTree, x: Int): PolyReturn = (t, x) match {
      case (Leaf(y),       0) => Found(y)
      case (Leaf(y),       _) => Continue(x - 1)
      case (MNode(List()), _) => Continue(x)
      case (MNode(nodes),  _) =>
        findImmutableHelper(nodes.head, x) match {
          case Found(y) => Found(y)
          case Continue(x)  => findImmutableHelper(MNode(nodes.tail), x)
        }
    }
    findImmutableHelper(t, x) match {
      case Found(x) => Some(x)
      case _ => None
    }
  }
}
