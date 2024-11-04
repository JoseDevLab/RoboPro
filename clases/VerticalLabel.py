from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QFontMetrics

class VerticalLabel(QLabel):
    def __init__(self, text, parent=None):
        super(VerticalLabel, self).__init__(text, parent)
        self.setMinimumWidth(self.fontMetrics().height())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.translate(self.sizeHint().width(), self.sizeHint().height())
        painter.rotate(-90)
        painter.drawText(0, 0, self.text())
        painter.end()

    def sizeHint(self):
        fm = QFontMetrics(self.font())
        return fm.size(Qt.TextSingleLine, self.text()).transposed()

    def minimumSizeHint(self):
        return self.sizeHint()