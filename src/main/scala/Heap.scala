package snippets.algorithms

object ArrayHeap {
  def main(args: Array[String]) = {
    val h = new ArrayHeap()
    h.insert(1)
    println(h.toString)
    h.insert(2)
    println(h.toString)
    h.insert(-5)
    println(h.toString)
    h.insert(10)
    println(h.toString)
    h.deleteMin()
    println(h.toString)
    h.deleteMin()
    println(h.toString)
    h.deleteMin()
    println(h.toString)
    h.deleteMin()
    println(h.toString)
  }
}

class ArrayHeap {
  // FIXME: we should support resizing
  // For a node i, children are at 2i + 1 and 2i + 2
  // Parent is (i-1)/2
  var h = Array.fill(20){Int.MaxValue}
  var len = 0

  override def toString() = {
//    s"${len}: ${h.slice(0,len+2).mkString(" ")}"
    s"${len}: ${h.slice(0,len).mkString(" ")}"
  }

  // FIXME: Should return Some/None
  def min = h(0)

  def insert(x: Int) = {
    var i = len
    h(i) = x
    // bubble up
    while (h(i) < h((i-1)/2)) {
      swap(i, (i-1)/2)
      i = (i-1)/2
    }
    len = len + 1
  }

  def deleteMin() = {
    if (len > 0) {
      var i = 0
      swap(0,len - 1)
      // FIXME: this is a mess
      var left = math.min(2*i + 1, math.max(len-2,0))
      var right = math.min(2*i + 2, math.max(len-2,0))
      while (h(i) > h(left) || h(i) > h(right)) {
        println(s"pre swap ${this.toString()}")
        if (h(left) > h(right)) {
          println(s"swapping ${i} ${right} | ${h(i)} ${h(right)}")
          swap(i, right)
          i = right

        } else {
          println(s"swapping ${i} ${left} | ${h(i)} ${h(left)}")
          swap(i, left)
          i = left
        }
        left = math.min(2*i + 1, math.max(len-2,0))
        right = math.min(2*i + 2, math.max(len-2,0))
      }
      len = len - 1
    }
  }

  def left(i: Int) = 2*i + 1
  def right(i: Int) = 2*i + 2

  // Thought about using a recursive siftDown instead of the deleteMin
  // fn above, but this doesn't seem simpler
  def siftDown(i: Int): Unit = {
    var swapIdx = 0
    if (right(i) > (len - 1)) {
      if (left(i) > (len - 1))
        return
      else
        swapIdx = left(i)
    } else {
      if (h(right(i))  > h(left(i)))
        swapIdx = left(i)
      else
        swapIdx = right(i)
    }
    if (h(i) > h(swapIdx)) {
      swap(i,swapIdx)
      siftDown(swapIdx)
    } 
  }

  def swap(i: Int, j: Int) = {
    val temp = h(i)
    h(i) = h(j)
    h(j) = temp
  }

}

sealed abstract class Heap {
  def min: Int
}

case class Node(x: Int, l: Heap, r: Heap) extends Heap {
  override def min = x
}

case object End extends Heap {
  override def min = 0 //FIXME: return Some/None
}

object Node {
  def apply(x: Int): Node = Node(x, End, End)
}

