// Inspired by https://gist.github.com/happy4crazy/5489636

sealed trait Regex
case object Nil extends Regex
case object Empty extends Regex
case class Lit(c: Char) extends Regex
case class Union(left: Regex, right: Regex) extends Regex
case class Concat(right: Regex, left: Regex) extends Regex
case class Star(x: Regex) extends Regex
