```python
'''
 display an image
on the window.
'''
from PyQt5.QtWidgets import (QWidget,QHBoxLayout,QLabel,QApplication)
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox=QHBoxLayout(self)
        pixmap=QPixmap('mute.png')
        lal=QLabel(self)
        lal.setPixmap(pixmap)

        hbox.addWidget(lal)
        self.setLayout(hbox)

        self.move(100,100)
        self.setWindowTitle('Mute')
        self.show()

def main():
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
```
