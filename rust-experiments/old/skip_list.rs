use core::rand::RngUtil;

struct Node {
    left: MaybeNode,
    right: MaybeNode,
    down: MaybeNode,
    up: MaybeNode,
    data: int
}

enum MaybeNode {
    SomeNode(@mut Node),
    NoNode
}

fn print_nodes(x: @mut Node){
    println(fmt!("%d", x.data));
    match x.right {
        NoNode => println("Done!"),
        SomeNode(n) => print_nodes(n)
    }
    
}

// insert a node into the skip list
// FIXME: currently doesn't do balanced insert
fn insert(data: int, top: @mut Node) {
    let y = @mut Node { right: NoNode, left: NoNode, up: NoNode, down: NoNode, data: data };
    let smaller_node = find_insert(y.data, top);
    insert_after(smaller_node, y)
}

// insert node y after node x
fn insert_after(x: @mut Node, y: @mut Node) {
    match x.right {
        SomeNode(xn) => {
            xn.left = SomeNode(y);
            x.right = SomeNode(y);
            y.left = SomeNode(x);
            y.right = SomeNode(xn);
            y.down = NoNode;
            y.up = NoNode
        }
        NoNode => {
            x.right = SomeNode(y);
            y.left = SomeNode(x);
        }
    }
}

// insert node y before node x
fn insert_before(x: @mut Node, y: @mut Node){
    match x.left {
        SomeNode(xp) => {
            x.left = SomeNode(y);
            xp.right = SomeNode(y);
            y.left = SomeNode(xp);
            y.right = SomeNode(x)
        }
        NoNode => {
            x.left = SomeNode(y);
            y.right = SomeNode(x);
        }
    }
}

fn main() {
    let rng = rand::Rng();
    println(fmt!("%f",rng.gen_float()));
  
    let mut max_height = 0;
    let mut top = NoNode;
}

// We have two find functions. The standard find function returns a node if it exists
// Find for insert returns a node regardless, because we want a reference to insert into

fn find_insert(k: int, n: @mut Node) -> @mut Node {
    fn find_down(k: int, n: @mut Node) -> @mut Node {
        match n.down {
            NoNode => {
                println(fmt!("Failed search at %d", n.data));
                return n
            },
            SomeNode(m) => find_insert(k, m)
        }
    }

    if(n.data == k) {
        println(fmt!("Found it! %d", n.data));
        return n
    } else {
        println(fmt!("Looking for %d at %d", k, n.data));
    }

    // Look right. If >=, must be at least in that column. Otherwise, go down one level and try again.
    // If we get to the bottom and can't find anything, we must have failed to find the correct value
    match n.right {
        NoNode => {
            println(fmt!("Move down: No right node at %d", n.data));
            find_down(k,n)
        },
        SomeNode(m) => {
            if (k >= m.data) {
                println(fmt!("Move right: >= right node (%d) at %d", m.data, n.data));
                find_insert(k, m)
            } else {
                println(fmt!("Move down: < right node (%d) at %d", m.data, n.data));
                find_down(k,n)
            }
        }
    }
}

fn find(k: int, n: @mut Node) -> MaybeNode {
    let res = find_insert(k, n);
    if (res.data == k) {
        println(fmt!("DEBUG: returning a node %d\n", res.data));
        return SomeNode(res);
    } else {
        println("DEBUG: returning NoNode\n");
        return NoNode;
    }
}

#[test]
fn search_simple() {
    let mut max_height = 0;

    let head0 = @mut Node { right: NoNode, left: NoNode, up: NoNode, down: NoNode, data: int::min_value };
    let head1 = @mut Node { right: NoNode, left: NoNode, up: NoNode, down: SomeNode(head0), data: int::min_value };
    let head2 = @mut Node { right: NoNode, left: NoNode, up: NoNode, down: SomeNode(head1), data: int::min_value };
    head0.up = SomeNode(head1);
    head1.up = SomeNode(head2);
    let mut top = head2;

    let node1000 = @mut Node { right: NoNode, left: SomeNode(head0), up: NoNode, down: NoNode, data: 1000 };
    head0.right = SomeNode(node1000);

    let node2000 = @mut Node { right: NoNode, left: SomeNode(node1000), up: NoNode, down: NoNode, data: 2000 };
    let node2000u = @mut Node { right: NoNode, left: SomeNode(head1), up: NoNode, down: SomeNode(node2000), data: 2000 };
    let node2000uu = @mut Node { right: NoNode, left: SomeNode(head2), up: NoNode, down: SomeNode(node2000u), data: 2000 };
    node1000.right = SomeNode(node2000);
    head1.right = SomeNode(node2000u);
    head2.right = SomeNode(node2000uu);
    node2000.up = SomeNode(node2000u);
    node2000u.up = SomeNode(node2000uu);

    let node3000 = @mut Node { right: NoNode, left: SomeNode(node2000), up: NoNode, down: NoNode, data: 3000 };
    node2000.right = SomeNode(node3000);

    println("---Find head");
    find(int::min_value, top);
    println("---Find 2000");
    find(2000, top);
//    assert!(find(2000, top) == SomeNode(node2000uu)); //FIXME: when I have internet access, figure out why this is illegal and how to fix it
    /* also doesn't work
    match find(2000, top) {
        NoNode => assert!(false),
        SomeNode(n) => assert!(&n == &node2000uu)
    }*/
    /*
    match find(2000, top) {
        NoNode => assert!(false),
        SomeNode(n) => {
            let an = &n;
            let a2000uu = &node2000uu;
            assert!(an == a2000uu);
        }
    }*/
    println("---Find 1000");
    find(1000, top);
    println("---Find 3000");
    find(3000, top);
    println("---Find 2500");
    find(2500, top);
    println("---insert 2750");
    insert(2750, top);
    println("---find 2750");
    find(2750, top);
    println("---display nodes: top");
    print_nodes(top);
    println("---display nodes: bottom");
    print_nodes(head0);

}
