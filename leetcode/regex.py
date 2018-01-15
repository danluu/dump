import unittest

# Full string match (no partial match) supporting . and *, incomplete.

class FSM():
    def __init__(self, states=[]):
        self.states = states
        self.reset_states = self.states
        self.match = False

    # parse pattern.
    def parse(self, s):
        tmp = []
        
        i = 0
        while i <= len(s):
            # print('parsing {}:{}'.format(i, s[i]))
            is_star = False
            if i+1 < len(s) and s[i+1] == '*':
                is_star = True

            cur_state = None
            if i == len(s):
                # Mark end of string with special end state.
                cur_state = State('',False,True)
            else:
                cur_state = State(s[i], is_star)
            for j in range (len(tmp) - 1, -1, -1):
                print('linking to {}'.format(j))
                prev_state = tmp[j]
                prev_state.next_states.append(cur_state)
                if not prev_state.is_star:
                    break

            tmp.append(cur_state)
            i += 1
            if is_star:
                i += 1

        self.states = [tmp[0]]
        self.reset_states = [tmp[0]]
        self.match = False

    def is_match(self):
        return self.match

    def reset(self):
        self.states = self.reset_states
        self.match = False
        
    def process_char(self, c):
        print('process_char {}'.format(c))
        next_states = []
        for state in self.states:
            print('IN A STATE', state)
            if c == '' and state.is_end:
                self.match = True
            elif state.pattern != '.' and state.pattern != c:
                print('miss')
                pass
            elif state.next_states:
                print('going to next states')
                for ns in state.next_states:
                    next_states.append(ns)
            else:
                print('fallthrough')
                    
        print('num new states: {}'.format(len(next_states)))
        self.states = next_states

class State():
    def __init__(self, pattern, is_star=False, is_end=False, next_states=[]):
        self.pattern = pattern
        self.is_star = is_star
        self.is_end = is_end
        self.next_states = next_states

        
        
    def __repr__(self):
        return 'pattern:is_end {}:{} next_states {}'.format(self.pattern, self.is_end, self.next_states)
            
        
class TestRegex(unittest.TestCase):
    def test_trivial_no_match(self):
        s1 = State('', False, True)
        s0 = State('a', False, False, [s1])
        fsm = FSM([s0])
        fsm.process_char('x')
        fsm.process_char('')
        self.assertFalse(fsm.is_match())
        
    def test_trivial_match(self):
        s1 = State('', False, True)
        s0 = State('a', False, False, [s1])
        fsm = FSM([s0])
        fsm.process_char('a')
        fsm.process_char('')
        self.assertTrue(fsm.is_match())

    def test_trivial_parse(self):
        fsm = FSM()
        fsm.parse('')

    def test_trivial_char_parse(self):
        fsm = FSM()
        fsm.parse('a')
        fsm.process_char('a')
        self.assertFalse(fsm.is_match())
        fsm.process_char('')
        self.assertTrue(fsm.is_match())

        fsm.reset()
        self.assertFalse(fsm.is_match())
        fsm.process_char('x')
        self.assertFalse(fsm.is_match())
        fsm.process_char('')
        self.assertFalse(fsm.is_match())

        fsm.reset()
        self.assertFalse(fsm.is_match())
        fsm.process_char('a')
        self.assertFalse(fsm.is_match())
        fsm.process_char('')
        self.assertTrue(fsm.is_match())


        fsm.reset()
        self.assertFalse(fsm.is_match())
        fsm.process_char('a')
        self.assertFalse(fsm.is_match())
        fsm.process_char('a')
        self.assertFalse(fsm.is_match())
        fsm.process_char('')
        self.assertFalse(fsm.is_match())


    def test_trivial_star_parse(self):
        fsm = FSM()
        fsm.parse('a*')

        
unittest.main()
