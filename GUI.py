from PyQt4 import QtCore, QtGui
import submodules
import sys, os

from Interface import Ui_MainWindow

class MyPopup(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

    def paintEvent(self, e):
        window = QtGui.QMainWindow()
        window.setGeometry(0, 0, 400, 200)

        pic = QtGui.QLabel(window)
        pic.setGeometry(10, 10, 400, 100)
        #use full ABSOLUTE path to the image, not relative
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/image20.jpg"))

        window.show()

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
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Image files (*.jpg *.gif)")
        self.ui.lineEdit.setText(filename)
        self.filename = filename

    def execute(self):
    	if(self.filename==None):
    		return
    	else:
    		message = submodules.execute_model(self.filename)
    	self.ui.DD.setText(message)		

        self.w = MyPopup()
        # self.w.setGeometry(QtCore.QRect(100, 100, 400, 200))
        self.w.setWindowTitle("Output Image")
        label = QtGui.QLabel(w)
        pixmap = QtGui.QPixmap(os.getcwd() + 'images/image20.jpg')
        label.setPixmap(pixmap)
        w.resize(pixmap.width(),pixmap.height())
        self.w.show()


app=QtGui.QApplication(sys.argv)
w=MainWindow()
def main():
    w.show()
    app.exec_()
    sys.exit(0)

if __name__=='__main__':
    main()