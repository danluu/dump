package snippets.algorithms

class RedBlack[T](implicit ord: Ordering[T]) {
  sealed abstract class Color
  case object Red extends Color
  case object Blk extends Color

  sealed abstract class Tree {
    def ins(x: T): Tree
  }

  case object End extends Tree {
    override def ins: Tree = Node(Red, End, x, End) 
  }

  case class Node(c: Color, l: Tree, a: T, r: Tree) extends Tree {

  }
}
