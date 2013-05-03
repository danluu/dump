package snippets.algorithms

import org.scalatest.FunSuite

import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner

@RunWith(classOf[JUnitRunner])
class TreeSuite extends FunSuite {
  import RegexEngine._
  test("Simple Regex Tests"){
    val a = Lit('a')
    val b = Lit('b')
    assert(matches(a, "a") == true)
    assert(matches(a, "aa") == false) // This is a classical regex
    val aStar = Star(a)
    assert(matches(aStar, "") == true)
    assert(matches(aStar, "a") == true)
    assert(matches(aStar, "aa") == true)
    val aPlus = Concat(a, aStar)
    assert(matches(aPlus, "") == false)
    assert(matches(aPlus, "a") == true)
    assert(matches(aPlus, "aa") == true)
    val aStarb = Concat(aStar, b)
    assert(matches(aStarb, "b") == true)
    assert(matches(aStarb, "ab") == true)
    assert(matches(aStarb, "aab") == true)
    assert(matches(aStarb, "aaba") == false)
    val aStara = Concat(aStar, a)
    assert(matches(aStara, "a") == true)
    assert(matches(aStara, "aa") == true)
    assert(matches(aStara, "aaa") == true)
    val aStarab = Concat(aStara, b)
    assert(matches(aStarab, "ab") == true)
    assert(matches(aStarab, "aab") == true)
    assert(matches(aStarab, "aaab") == true)
    assert(matches(aStarab, "aaa") == false)
    val ab = Concat(a, b)
    val abStar = Star(ab)
    assert(matches(abStar,"a") == false)
    assert(matches(abStar,"ab") == true)
    assert(matches(abStar,"aba") == false)
    assert(matches(abStar,"abab") == true)
  }
}
