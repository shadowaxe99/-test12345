```python
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QComboBox, QLineEdit
from PyQt5.QtCore import Qt
import sys

class AutoClickerGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Auto-Clicker")

        # Start button
        self.start_button = QPushButton('Start', self)
        self.start_button.move(50, 50)

        # Stop button
        self.stop_button = QPushButton('Stop', self)
        self.stop_button.move(150, 50)

        # Pause button
        self.pause_button = QPushButton('Pause', self)
        self.pause_button.move(50, 100)

        # Resume button
        self.resume_button = QPushButton('Resume', self)
        self.resume_button.move(150, 100)

        # Click type dropdown
        self.click_type_dropdown = QComboBox(self)
        self.click_type_dropdown.addItem("Left Click")
        self.click_type_dropdown.addItem("Right Click")
        self.click_type_dropdown.addItem("Middle Click")
        self.click_type_dropdown.move(50, 150)

        # Click interval input
        self.click_interval_input = QLineEdit(self)
        self.click_interval_input.move(150, 150)

        # Click position dropdown
        self.click_position_dropdown = QComboBox(self)
        self.click_position_dropdown.addItem("Fixed Position")
        self.click_position_dropdown.addItem("Variable Position")
        self.click_position_dropdown.move(50, 200)

        # Click limit input
        self.click_limit_input = QLineEdit(self)
        self.click_limit_input.move(150, 200)

        # Profile dropdown
        self.profile_dropdown = QComboBox(self)
        self.profile_dropdown.move(50, 250)

        # Status label
        self.status_label = QLabel('Status: Idle', self)
        self.status_label.move(50, 300)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            self.start_clicking()
        elif event.key() == Qt.Key_F2:
            self.stop_clicking()
        elif event.key() == Qt.Key_F3:
            self.pause_clicking()
        elif event.key() == Qt.Key_F4:
            self.resume_clicking()

    def start_clicking(self):
        self.status_label.setText('Status: Clicking')
        # TODO: Implement start clicking functionality

    def stop_clicking(self):
        self.status_label.setText('Status: Idle')
        # TODO: Implement stop clicking functionality

    def pause_clicking(self):
        self.status_label.setText('Status: Paused')
        # TODO: Implement pause clicking functionality

    def resume_clicking(self):
        self.status_label.setText('Status: Clicking')
        # TODO: Implement resume clicking functionality

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = AutoClickerGUI()
    window.show()

    sys.exit(app.exec_())
```