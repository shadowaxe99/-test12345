```python
import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import sys

# Assuming the GUI is implemented in gui.py
import src.gui as gui

app = QApplication(sys.argv)

class TestGui(unittest.TestCase):
    def setUp(self):
        self.form = gui.AutoClickerGUI()

    def test_start_button(self):
        self.assertEqual(self.form.start_button.text(), "Start")
        QTest.mouseClick(self.form.start_button, Qt.LeftButton)
        self.assertEqual(self.form.start_button.text(), "Stop")

    def test_pause_button(self):
        self.assertEqual(self.form.pause_button.text(), "Pause")
        QTest.mouseClick(self.form.pause_button, Qt.LeftButton)
        self.assertEqual(self.form.pause_button.text(), "Resume")

    def test_click_type_dropdown(self):
        self.assertEqual(self.form.click_type_dropdown.currentText(), "Left Click")
        QTest.keyClicks(self.form.click_type_dropdown, "Right Click")
        self.assertEqual(self.form.click_type_dropdown.currentText(), "Right Click")

    def test_click_interval_input(self):
        self.assertEqual(self.form.click_interval_input.text(), "1000")
        QTest.keyClicks(self.form.click_interval_input, "2000")
        self.assertEqual(self.form.click_interval_input.text(), "2000")

    def test_click_position_dropdown(self):
        self.assertEqual(self.form.click_position_dropdown.currentText(), "Fixed Position")
        QTest.keyClicks(self.form.click_position_dropdown, "Variable Position")
        self.assertEqual(self.form.click_position_dropdown.currentText(), "Variable Position")

    def test_click_limit_input(self):
        self.assertEqual(self.form.click_limit_input.text(), "Unlimited")
        QTest.keyClicks(self.form.click_limit_input, "100")
        self.assertEqual(self.form.click_limit_input.text(), "100")

    def test_profile_dropdown(self):
        self.assertEqual(self.form.profile_dropdown.currentText(), "Default")
        QTest.keyClicks(self.form.profile_dropdown, "Profile 1")
        self.assertEqual(self.form.profile_dropdown.currentText(), "Profile 1")

if __name__ == "__main__":
    unittest.main()
```