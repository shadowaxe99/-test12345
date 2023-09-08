```python
import sys
from PyQt5.QtWidgets import QApplication
from gui import AutoClickerGUI
from click_simulation import ClickSimulation
from click_type import ClickType
from click_interval import ClickInterval
from click_position import ClickPosition
from click_limit import ClickLimit
from hotkeys import Hotkeys
from user_profiles import UserProfiles

class AutoClicker:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.gui = AutoClickerGUI()
        self.click_simulation = ClickSimulation()
        self.click_type = ClickType()
        self.click_interval = ClickInterval()
        self.click_position = ClickPosition()
        self.click_limit = ClickLimit()
        self.hotkeys = Hotkeys()
        self.user_profiles = UserProfiles()

    def run(self):
        self.gui.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    auto_clicker = AutoClicker()
    auto_clicker.run()
```