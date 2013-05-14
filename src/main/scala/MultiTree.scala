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
  def main(args: Array[String]) = {
    val t = MNode(List(Leaf(0), Leaf(1), Leaf(2), 
      MNode(List(
        MNode(List
          (Leaf(3), Leaf(4))),
        Leaf(5), Leaf(6)))))
    (0 to 7).foreach{i =>
      println(find(t,i))
      println(findImmutable(t,i))
    }
  }


  def find(t: MultiTree, x: Int) = {
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
    try {
      findHelper(t, x)
      None
    } catch {
      case FoundMatch(_, _, y) => Some(y)
    }
  }

  // inspiried by Raul
  def findImmutable(t: MultiTree, x: Int) = {
    def findImmutableHelper(t: MultiTree, x: Int): PolyReturn = t match {
      case Leaf(y) =>
        if (x == 0)
          Found(y)
        else
          Continue(x - 1)
      case MNode(List()) =>
        Continue(x)
      case MNode(nodes) =>
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
