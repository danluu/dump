package snippets.algorithms

import org.scalatest.FunSuite

import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner

@RunWith(classOf[JUnitRunner])
class MultiTreeSuite extends FunSuite {
  import MTreeToy._

  test("Mutable find") {
    val t = MNode(List(Leaf(0), Leaf(1), Leaf(2),
      MNode(List(
        MNode(List
          (Leaf(3), Leaf(4))),
        Leaf(5), Leaf(6)))))
      (0 to 7).foreach{i =>
        if (i <= 6)
          assert(find(t,i) == Some(i))
        else
          assert(find(t,i) == None)
      }
  }

  test("Immutable find") {
    val t = MNode(List(Leaf(0), Leaf(1), Leaf(2),
      MNode(List(
        MNode(List
          (Leaf(3), Leaf(4))),
        Leaf(5), Leaf(6)))))
      (0 to 7).foreach{i =>
        if (i <= 6)
          assert(findImmutable(t,i) == Some(i))
        else
          assert(findImmutable(t,i) == None)
      }
  }
}
