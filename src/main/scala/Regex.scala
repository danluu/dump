package snippets.algorithms
// Inspired by https://gist.github.com/happy4crazy/5489636

sealed trait Regex
case object Nil extends Regex
case object Empty extends Regex
case class Lit(c: Char) extends Regex
case class Union(left: Regex, right: Regex) extends Regex
case class Concat(right: Regex, left: Regex) extends Regex
case class Star(x: Regex) extends Regex

object Foo{
  def success(x: Regex): Boolean = x match {
    case Nil => false
    case Empty => true
    case Lit(_) => false
    case Union(l, r) => success(l) || success(r)
    case Concat(l, r) => success(l) && success(r)
    case Star(_) => true
  }

  def step(x: Regex, c: Char): Regex = x match {
    case Nil => Nil
    case Empty => Nil
    case Lit(regexC: Char) => 
      if (regexC == c) 
        Empty
      else 
        Nil
    case Union(left, right) => Union(step(left, c), step(right, c))
    case Concat(left, right) =>
      if (success(left)) 
        Union(Concat(step(left, c), right), step(right, c))
      else 
        Concat(step(left, c), right)
    case Star(regexX) => Concat(step(regexX, c), Star(regexX))
  }
}
