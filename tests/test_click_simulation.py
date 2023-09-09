```python
import unittest
from src import click_simulation

class TestClickSimulation(unittest.TestCase):

    def setUp(self):
        self.click_simulator = click_simulation.ClickSimulator()

    def test_single_click(self):
        self.click_simulator.simulate_click('single')
        self.assertEqual(self.click_simulator.click_count, 1)

    def test_double_click(self):
        self.click_simulator.simulate_click('double')
        self.assertEqual(self.click_simulator.click_count, 2)

if __name__ == '__main__':
    unittest.main()
```