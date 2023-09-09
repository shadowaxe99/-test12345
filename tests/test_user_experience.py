```python
import unittest
from PyQt5.QtWidgets import QApplication
from src.gui import AutoClickerGUI

app = QApplication([])

class TestUserExperience(unittest.TestCase):

    def setUp(self):
        self.gui = AutoClickerGUI()

    def test_start_button_exists(self):
        self.assertIsNotNone(self.gui.start_button)

    def test_stop_button_exists(self):
        self.assertIsNotNone(self.gui.stop_button)

    def test_pause_button_exists(self):
        self.assertIsNotNone(self.gui.pause_button)

    def test_resume_button_exists(self):
        self.assertIsNotNone(self.gui.resume_button)

    def test_click_type_dropdown_exists(self):
        self.assertIsNotNone(self.gui.click_type_dropdown)

    def test_click_interval_input_exists(self):
        self.assertIsNotNone(self.gui.click_interval_input)

    def test_click_position_dropdown_exists(self):
        self.assertIsNotNone(self.gui.click_position_dropdown)

    def test_click_limit_input_exists(self):
        self.assertIsNotNone(self.gui.click_limit_input)

    def test_profile_dropdown_exists(self):
        self.assertIsNotNone(self.gui.profile_dropdown)

if __name__ == '__main__':
    unittest.main()
```