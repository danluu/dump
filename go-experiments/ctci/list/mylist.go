package mylist

type Node struct {
	val  int
	next *Node
}

type List struct {
	head *Node
	size int
}

func (node *Node) Insert(x int) *Node {
	newNode := new(Node)
	newNode.val = x

	newNode.next = node.next
	node.next = newNode

	return newNode
}
