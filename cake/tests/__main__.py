import unittest
from .. import run, runnable
def echo(*args, capitalize = False):
    if capitalize:
        args = [a.upper() for a in args]
    return ' '.join(args)

def sum(*args):
    _sum = 0
    for arg in args:
        _sum += arg
    return _sum

class testRunnable(unittest.TestCase):
    def test_echo_simple_1(self):
        out = runnable(echo).runCLI(args=['Hello', 'World!','--capitalize'],print_output=False)
        self.assertEqual(out, "HELLO WORLD!")
    def test_echo_simple_2(self):
        wrapped = runnable(args=['Hello', 'World!'], print_output=False)(echo)
        self.assertEqual(wrapped.runCLI(), "Hello World!")
    def test_echo_kwargs(self):
        wrapped = runnable(args=['Hello', 'World!','--capitalize'], print_output=False)(echo)
        self.assertEqual(wrapped.runCLI(), "HELLO WORLD!")
    def test_sum(self):
        wrapped = runnable(args=['1','7','8'], print_output=False)(sum)
        self.assertEqual(wrapped.runCLI(), 16)
        self.assertEqual(wrapped(1,3,5,9), 18) # Test original function still works

if __name__ == '__main__':
    unittest.main()