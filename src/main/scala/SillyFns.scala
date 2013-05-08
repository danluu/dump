package snippets.algorithms

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
    case x if xs.isEmpty => Unit //too bad we can't just write Nil?
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

  def main(args: Array[String]): Unit = {
    println(byname(myTime()))
    println(List(41, "cat") collect { case i: Int ⇒ i + 1 })
    println(List("abc","aa","bo","foo","!").groupBy(_.length))
    println(myGroupBy(List("abc","aa","bo","foo","!"),{x:String => x.length}))
    println(myGroupBy0(List("abc","aa","bo","foo","!"),{x:String => x.length}))
    println(myGroupByImmutable(List("abc","aa","bo","foo","!"),{x:String => x.length}))
    println(myGroupByImmutable0(List("abc","aa","bo","foo","!"),{x:String => x.length}))
  }

}
