struct Node {
    next: MaybeNode,
    prev: MaybeNode,
    data: int
}

enum MaybeNode {
    SomeNode(@mut Node),
    NoNode
}

fn print_nodes(x: @mut Node){
    println(fmt!("%d", x.data));
    match x.next {
        NoNode => println("Done!"),
        SomeNode(n) => print_nodes(n)
    }
    
}

// insert node y after node x
fn insert_after(x: @mut Node, y: @mut Node){
    match x.next {
        SomeNode(xn) => {
            xn.prev = SomeNode(y);
            x.next = SomeNode(y);
            y.prev = SomeNode(x);
            y.next = SomeNode(xn);
        }
        NoNode => {
            x.next = SomeNode(y);
            y.prev = SomeNode(x);
        }
    }
}

// insert node y before node x
fn insert_before(x: @mut Node, y: @mut Node){
    match x.prev {
        SomeNode(xp) => {
            x.prev = SomeNode(y);
            xp.next = SomeNode(y);
            y.prev = SomeNode(xp);
            y.next = SomeNode(x)
        }
        NoNode => {
            x.prev = SomeNode(y);
            y.next = SomeNode(x);
        }
    }
}

fn insert_balanced_helper(list: MaybeNode, x: @mut Node, prev: MaybeNode){
    match list {
        SomeNode(n) => {
            if (x.data < n.data) {
                insert_before(n, x);
            } else {
                insert_balanced_helper(n.next, x, list);
            }
        }
        NoNode => match prev {
            SomeNode(n) => insert_after(n, x),
            NoNode => println("FIXME: can't insert into empty list")
        }
    }
}

fn insert_balanced(list: MaybeNode, x: @mut Node){
    insert_balanced_helper(list, x, NoNode);
}

fn main() {
    let node100 = @mut Node { next: NoNode, prev: NoNode, data: 100 };
    let node150 = @mut Node { next: NoNode, prev: NoNode, data: 150 };
    let node200 = @mut Node { next: NoNode, prev: NoNode, data: 200 };
    let node250 = @mut Node { next: NoNode, prev: NoNode, data: 250 };
    let node300 = @mut Node { next: NoNode, prev: NoNode, data: 300 };

    insert_after(node100, node200);
    insert_after(node200, node300);
    insert_after(node200, node250);
    insert_before(node200, node150);

    let node75 =  @mut Node { next: NoNode, prev: NoNode, data: 75 };
    let node125 =  @mut Node { next: NoNode, prev: NoNode, data: 125 };
    let node325 =  @mut Node { next: NoNode, prev: NoNode, data: 325 };
    insert_balanced(SomeNode(node100), node75);
    insert_balanced(SomeNode(node75), node125);
    insert_balanced(SomeNode(node75), node325);

    print_nodes(node75);
}


