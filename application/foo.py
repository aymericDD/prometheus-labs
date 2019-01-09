import unittest
from prometheus_client import Counter
from prometheus_client import REGISTRY

FOOS = Counter('foos_total', 'The number of foo calls.')

def foo():
  FOOS.inc()

class TestFoo(unittest.TestCase):
  def test_counter_inc(self):
    before = REGISTRY.get_sample_value('foos_total')
    foo()
    after = REGISTRY.get_sample_value('foos_total')
    self.assertEqual(1, after - before)


if __name__ == '__main__':
  unittest.main()

