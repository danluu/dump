package snippets.algorithms

object LazyQueue {
  import LazyQueue._

  def main(args: Array[String]){
    val a = new LazyQueue()
    val b = a.enqueue(1).enqueue(2)
    println(b.elements)
  }
}


class LazyQueue {
  val lenf: Int = 0
  val front: Stream[Int] = Stream.empty
  val lenr: Int = 0
  val rear: List[Int] = Nil

  def isEmpty() = lenf == 0
  def enqueue(x: Int) = exec(lenf, front, lenr + 1, x :: rear)
  def dequeue() = (front.head, exec(lenf - 1, front.tail, lenr, rear))

  def rotate(xs: Stream[Int], ys: List[Int], rys: Stream[Int]): Stream[Int] = ys match {
    case y :: ys1 =>
      if (xs.isEmpty) {
        Stream.cons(y, rys)
      } else {
        Stream.cons(xs.head, rotate(xs.tail, ys.tail, Stream.cons(y,rys)))
      }
    case Nil => xs
  }

  def exec(lenf1: Int, f: Stream[Int], lenr1: Int, r: List[Int]): LazyQueue = {
    if(lenr <= lenf) {
      new LazyQueue {
        override val lenf = lenf1
        override val front = f
        override val lenr = lenr1
        override val rear = r
      } 
    } else {
      new LazyQueue {
        override val lenf = lenf1 + lenr1
        override val front = rotate(f,r, Stream.empty)
        override val lenr = 0
        override val rear = Nil
      }
    }
  }

  def elements: List[Int] = front.toList ::: rear.reverse
}

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

/*
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
  }*/
}
