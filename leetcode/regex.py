import unittest

# Full string match (no partial match) supporting . and *, incomplete.

class FSM():
    def __init__(self, states=None):
        if not states:
            states = []
        self.states = states
        self.reset_states = self.states
        self.match = False

    # parse pattern.
    def parse(self, s):
        tmp = []
        
        i = 0
        while i <= len(s):
            is_star = False
            if i+1 < len(s) and s[i+1] == '*':
                is_star = True

            cur_state = None
            if i == len(s):
                # Mark end of string with special end state.
                cur_state = State('',False,True)
            else:
                cur_state = State(s[i], is_star)

            print('cur', cur_state)
            for j in range (len(tmp) - 1, -1, -1):
                prev_state = tmp[j]
                prev_state.next_states.append(cur_state)
                print('prev', prev_state)
                print('cur', cur_state)
                print('linking {} to {} ({} total)'.format(j, i, len(prev_state.next_states)))

                if not prev_state.is_star:
                    break
                else:
                    if i == len(s):
                        print('marking old {} as end'.format(j))
                        prev_state.is_end = True

            tmp.append(cur_state)
            i += 1
            if is_star:
                i += 1

            if i <= len(s):
                print(tmp)

        self.states = [tmp[0]]
        self.reset_states = [tmp[0]]
        self.match = False

    def is_match(self, s=None):
        if s == None:
            return self.match

        self.reset()
        for x in s:
            self.process_char(x)
        print('-------------------wat')
        self.process_char('')
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
                print('going to {} next states'.format(len(state.next_states)))
                for ns in state.next_states:
                    next_states.append(ns)
            else:
                print('fallthrough')

            if state.is_star and state.pattern == c:
                print('star self loop')
                next_states.append(state)
                    
        print('num new states: {}'.format(len(next_states)))
        self.states = next_states

class State():
    def __init__(self, pattern, is_star=False, is_end=False, next_states=None):
        if next_states == None:
            next_states = []

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
        self.assertFalse(fsm.is_match('a'))
        self.assertFalse(fsm.is_match('aa'))
        self.assertTrue(fsm.is_match(''))

    def test_trivial_char_parse_manual(self):
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

    def test_tmp(self):
        fsm = FSM()
        fsm.parse('aa')
        self.assertFalse(fsm.is_match('a'))
        # self.assertFalse(fsm.is_match(''))
        # self.assertFalse(fsm.is_match('x'))

    def test_trivial_char_parse(self):
        fsm = FSM()
        fsm.parse('a')
        self.assertTrue(fsm.is_match('a'))
        self.assertFalse(fsm.is_match('x'))
        self.assertFalse(fsm.is_match('aa'))
        self.assertFalse(fsm.is_match(''))

        fsm.parse('aa')
        self.assertFalse(fsm.is_match('a'))
        self.assertFalse(fsm.is_match('xx'))
        self.assertTrue(fsm.is_match('aa'))
        self.assertFalse(fsm.is_match(''))

    def test_trivial_star_parse(self):
        fsm = FSM()
        fsm.parse('a*')
        self.assertTrue(fsm.is_match('a'))
        self.assertFalse(fsm.is_match('x'))
        self.assertTrue(fsm.is_match('aa'))
        self.assertTrue(fsm.is_match(''))

        self.assertFalse(fsm.is_match('ax'))
        self.assertFalse(fsm.is_match('xa'))

    def test_leetcode(self):
        pass
        
unittest.main()
