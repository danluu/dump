package snippets.algorithms

class SillyList[T](x: List[T]) {
  def myAppend(y: List[T]): List[T] = {
    x ++ y
  }
}

object SillyFns {

  def myTime() = {
    println("Getting time")
    System.nanoTime
  }

  def byname(t: => Long) = {
    println(s"byname t=${t}")
    t
  }

  // with mutable internal state
  def myGroupBy[T, U](xs: Seq[T], f: T => U) = {
    var result = scala.collection.mutable.Map[U, List[T]]()
    xs.foreach{ x => result.update(f(x), x :: result.getOrElse(f(x), List[T]())) }
    result
  }

  def myForeach[T](xs: Seq[T], f: T => Unit): Unit = xs match {
    case Seq() => Unit
    case _ => f(xs.head); myForeach(xs.tail, f)
  }

  def myGroupBy0[T, U](xs: Seq[T], f: T => U) = {
    var result = scala.collection.mutable.Map[U, List[T]]()
    myForeach(xs, { x: T => result.update(f(x), x :: result.getOrElse(f(x), List[T]())) })
    result
  }

  // immutable
  def myGroupByImmutable[T, U](xs: Seq[T], f: T => U) = {
    xs.foldLeft(Map[U, List[T]]()){ (acc, x) => acc.updated(f(x), x :: acc.getOrElse(f(x), List[T]())) }
  }

  def myFoldLeft[U,T](xs: Seq[T], acc: U, f: (U,T) => U): U = {
    if (xs.isEmpty) {
      acc
    } else {
      myFoldLeft(xs.tail, f(acc, xs.head), f)
    }
  }

  def myGroupByImmutable0[T, U](xs: Seq[T], f: T => U) = {
    myFoldLeft(xs, Map[U, List[T]](), { (acc: Map[U, List[T]], x: T) => acc.updated(f(x), x :: acc.getOrElse(f(x), List[T]())) })
  }

  def flattenAll[T](xs: List[Any]): List[Any] = xs flatMap {
    case ys: List[_] => flattenAll(ys)
    case x => List(x)  
  }

  def flattenOnce[T](xs: List[Any]): List[Any] = xs.flatMap {
    case ys: List[_] => ys
    case x => List(x)
  }

//  def myFlatMap[T, U](xs: Seq[T], f: T => U): Seq[U] = {
//
//  }


  def main(args: Array[String]): Unit = {
    println(byname(myTime()))
    println(List(41, "cat") collect { case i: Int ⇒ i + 1 })
    println(List("abc","aa","bo","foo","!").groupBy(_.length))
    println(myGroupBy(List("abc","aa","bo","foo","!"),{x:String => x.length}))
    println(myGroupBy0(List("abc","aa","bo","foo","!"),{x:String => x.length}))
    println(myGroupByImmutable(List("abc","aa","bo","foo","!"),{x:String => x.length}))
    println(myGroupByImmutable0(List("abc","aa","bo","foo","!"),{x:String => x.length}))

    implicit def sillifyList[T](xs: List[T]) = new SillyList[T](xs)
    val a = List(1,2,3)
    val b = List(4,5,6)
    println(a.myAppend(b))

    println("flattens!")
    println(List(List(1, 1), 2, List(3, List(5, 8))))
    println(flattenAll(List(List(1, 1), 2, List(3, List(5, 8)))))
    println(flattenOnce(List(List(1, 1), 2, List(3, List(5, 8)))))

  }

}
