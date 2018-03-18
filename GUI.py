from PyQt4 import QtCore, QtGui
import submodules
import sys

from Interface import Ui_MainWindow

class MainWindow(QtGui.QMainWindow, Ui_MainWindow, QtGui.QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.filename = None
        self.ui.uploadButton.clicked.connect(self.getfiles)
        self.ui.submitButton.clicked.connect(self.execute)


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
    	self.ui.textBrowser.setText(message)		    


app=QtGui.QApplication(sys.argv)
w=MainWindow()
def main():
    w.show()
    app.exec_()
    sys.exit(0)

if __name__=='__main__':
    main()