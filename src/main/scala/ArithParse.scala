package snippets.algorithms

import scala.util.parsing.combinator._

class Arith extends JavaTokenParsers {
  def expr: Parser[Any] = term~rep("+"~term | "-"~term)
  def term: Parser[Any] = factor~rep("*"~factor | "/"~factor) 
  def factor: Parser[Any] = floatingPointNumber | "("~expr~")"
}

object ParseExpr extends Arith {
  def main(args: Array[String]) {
    println(parseAll(expr, "(2+2)*5"))
    println(parseAll(expr, "(1)"))
  }
}
