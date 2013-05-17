package snippets.algorithms

import scala.collection.mutable

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


  def myTime2(x: Int) = {
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

/*
  def flattenAll0[T](xs: Any) : List[Any] = xs match {
    case List(x::xs0)::xs => x :: flattenAll0(xs0) ++ flattenAll0(xs)
    case x::xs => x :: flattenAll0(xs)
    case _ => List()
  }
 */

  def flattenOnce(xs: List[Any]): List[Any] = xs.flatMap {
    case ys: List[_] => ys
    case x => List(x)
  }

  def flattenAll0[T](xs: List[T]): List[Any] = xs match {
    case List() => List()
    case x::xs => 
      (x match {
        case l: List[_] => flattenAll0(l)
        case x => List(x)
      }) ++ flattenAll0(xs)
  }


  def flattenAll1[T](xs: List[T]): List[Any] = xs match {
    case List() => List()
    case (x:List[_])::xs => flattenAll1(x) ++ flattenAll1(xs)
    case x::xs => List(x) ++ flattenAll1(xs)
  }

  def memoize[U,T](f: U => T): U => T = {
    val mem = scala.collection.mutable.Map[U,T]()

    def g(input: U): T = mem.get(input) match {
      case Some(x) => x
      case None => mem.update(input,f(input)); mem(input)
    }

    g
  }

//  def myFlatMap[T](xs: List[Any], f: Any => Iterable[T]): List[T] = xs match {
//    f(xs.head).elements ++ myFlatMap(xs.tail, f)
//  }

//  def myFlatMap[T, U](xs: Seq[T], f: T => U): Seq[U] = {
//
//  }


  def main(args: Array[String]): Unit = {
    println(byname(myTime()))
    println(List(41, "cat") collect { case i: Int ⇒ i + 1 })


    implicit def sillifyList[T](xs: List[T]) = new SillyList[T](xs)
    val a = List(1,2,3)
    val b = List(4,5,6)
    println(a.myAppend(b))

    println("flattens!")

    println(flattenOnce(List(List(1, 1), 2, List(3, List(5, 8)))))
//    println(myTime())
//    println(myTime())
    val memTime = memoize(myTime2)
    println(memTime(0))
    println(memTime(1))
    println(memTime(2))
    println("memoized")
    println(memTime(0))
    println(memTime(1))
    println(memTime(2))

  }

}
