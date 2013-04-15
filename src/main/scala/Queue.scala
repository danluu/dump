package snippets.algorithms

class StrictQueue() {
  var front = List[Int]()
  var back = List[Int]()

  def enqueue(x: Int) = {
    front = x :: front
  }

  def dequeue(): Unit = back match {
    case Nil => front match {
      case Nil => Nil
      case xs => back = front.reverse; front = List[Int](); dequeue()
    }
    case x::xs => back = xs; println(x); println(s"front ${front.mkString(" ")} back ${back.mkString(" ")}")
  }
}

object StrictQueue {
  import StrictQueue._

  def main(args: Array[String]){
    val q = new StrictQueue()
    (0 until 10). foreach { i => q.enqueue(i) }
    (0 until 10). foreach { i => q.dequeue }
    q.enqueue(10)
    q.enqueue(11)
    q.dequeue
    q.enqueue(12)
    q.dequeue
    q.dequeue

  }
}
