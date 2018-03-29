from PyQt4 import QtCore, QtGui
import submodules
import sys, os
import write_in_image
from Interface import Ui_MainWindow
img_path = "images/image20.jpg"

class MyPopup(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

    def paintEvent(self, e):
        pass

class MainWindow(QtGui.QMainWindow, Ui_MainWindow, QtGui.QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.filename = None
        self.ui.uploadButton.clicked.connect(self.getfiles)
        self.ui.submitButton.clicked.connect(self.execute)
        self.setFixedSize(self.size())


    def getfiles(self):
        global img_path
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Image files (*.jpg *.gif)")
        img_path = str(filename)
        self.ui.lineEdit.setText(filename)
        self.filename = filename

    def execute(self):
        if(self.filename==None):
            print("Filename is None")
            return
        else:
            message, co_ords, texts = submodules.execute_model(self.filename)
        self.ui.DD.setText(message)     

        self.w = MyPopup()
        # self.w.setGeometry(QtCore.QRect(100, 100, 400, 200))
        self.w.setWindowTitle("Output Image")
        write_in_image.main(img_path, co_ords, texts)
        label = QtGui.QLabel(self.w)
        pixmap = QtGui.QPixmap("/home/vernwalrahul/my_project/Open Soft/images/final.jpg")
        label.setPixmap(pixmap)
        label.show()
        self.w.resize(pixmap.width(),pixmap.height())
        self.w.show()


app=QtGui.QApplication(sys.argv)
w=MainWindow()
def main():
    w.show()
    app.exec_()
    sys.exit(0)

if __name__=='__main__':
    main()