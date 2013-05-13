package snippets.algorithms

// Tree problem from Raul

sealed trait MultiTree 
case class Leaf(x: Int) extends MultiTree
case class Node(nodes: List[MultiTree]) extends MultiTree

object MTreeToy {
  def main(args: Array[String]) = {
    println(Node(List(Leaf(3), Leaf(10), Leaf(20), Node(List(Leaf(3), Leaf(4))))))
  }

}
