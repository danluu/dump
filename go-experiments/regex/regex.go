package main

type State struct {
	match  byte
	isStar bool
	isLast bool
}

type Frag struct {
	start *State
	out   []**State
}

func post2nfa(postfix string) []State {
	stack := make([]State, 0)

	for i := range postfix {
		switch postfix[i] {
		case '.':
		case '|':
			/*
				e1 := stack[len(stack)-1]
				e2 := stack[len(stack)-2]
				st = State{nil, true, false, &e1, &e2, false}
				stack = stack[0 : len(stack)-3]
				stack = append(stack, Frag{&st, []**State{&e1.out, &e2.out}})
			*/
		case '?':
		case '*':
			stack[len(stack)-1].isStar = true
		default:
			st := State{postfix[i], false, false}
			stack = append(stack, st)
		}
	}

	matchState := State{0, false, true}
	stack = append(stack, matchState)
	return stack
}

type InputState struct {
	inpIdx int
	seqIdx int
}

func match(seq []State, inp string) bool {
	// Really want a list of these, but this is probably easier in go?
	inpStates := make(chan InputState, 128)
	initial := InputState{0, 0}
	inpStates <- initial
	for len(inpStates) > 0 {
		cur := <-inpStates
		if seq[cur.seqIdx].isLast {
			return true
		}
		// With our current setup, * can match off then end of the string.
		// Say we have some matching string and then match up to the end. Then we match .*.
		if seq[cur.seqIdx].isStar {
			if cur.inpIdx < len(inp) && inp[cur.inpIdx] == seq[cur.seqIdx].match {
				cur.inpIdx++
				inpStates <- cur
				cur.inpIdx--
			}
			cur.seqIdx++
			inpStates <- cur
		} else {
			if cur.inpIdx < len(inp) && inp[cur.inpIdx] == seq[cur.seqIdx].match {
				cur.inpIdx++
				cur.seqIdx++
				inpStates <- cur
			}
		}
	}
	return false
}
