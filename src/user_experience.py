```python
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QComboBox, QSpinBox
from PyQt5.QtCore import Qt

class UserExperience(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Auto-Clicker")

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout(self.main_widget)

        self.click_type_label = QLabel("Click Type:")
        self.click_type_dropdown = QComboBox()
        self.click_type_dropdown.addItems(["Left Click", "Right Click", "Middle Click"])

        self.click_interval_label = QLabel("Click Interval (in seconds):")
        self.click_interval_input = QSpinBox()
        self.click_interval_input.setRange(1, 3600)

        self.click_position_label = QLabel("Click Position:")
        self.click_position_dropdown = QComboBox()
        self.click_position_dropdown.addItems(["Fixed Position", "Follow Mouse"])

        self.click_limit_label = QLabel("Click Limit:")
        self.click_limit_input = QSpinBox()
        self.click_limit_input.setRange(1, 10000)

        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.pause_button = QPushButton("Pause")
        self.resume_button = QPushButton("Resume")

        self.layout.addWidget(self.click_type_label)
        self.layout.addWidget(self.click_type_dropdown)
        self.layout.addWidget(self.click_interval_label)
        self.layout.addWidget(self.click_interval_input)
        self.layout.addWidget(self.click_position_label)
        self.layout.addWidget(self.click_position_dropdown)
        self.layout.addWidget(self.click_limit_label)
        self.layout.addWidget(self.click_limit_input)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.pause_button)
        self.layout.addWidget(self.resume_button)

        self.show()

if __name__ == "__main__":
    app = QApplication([])
    ux = UserExperience()
    app.exec_()
```