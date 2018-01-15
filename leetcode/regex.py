import unittest

# Full string match (no partial match) supporting . and *, incomplete.

class FSM():
    def __init__(self, state):
        self.states = [state]
        self.match = False
        
    def is_match(self):
        return self.match
        
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
    def __init__(self, pattern, is_end=False, next_states=[]):
        self.pattern = pattern
        self.next_states = next_states
        self.is_end = is_end
        
    def __repr__(self):
        return 'pattern:is_end {}:{} next_states {}'.format(self.pattern, self.is_end, self.next_states)
            
        
class TestRegex(unittest.TestCase):
    def test_trivial_no_match(self):
        s1 = State('',True)
        s0 = State('a', False, [s1])
        fsm = FSM(s0)
        fsm.process_char('x')
        fsm.process_char('')
        self.assertFalse(fsm.is_match())
        
    def test_trivial_match(self):
        s1 = State('',True)
        s0 = State('a', False, [s1])
        fsm = FSM(s0)
        fsm.process_char('a')
        fsm.process_char('')
        self.assertTrue(fsm.is_match())        
        
        
        

unittest.main()
