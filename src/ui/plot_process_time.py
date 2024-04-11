# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_process_time.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_Plot_process_time(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(474, 167)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(11, 26, 417, 135))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_select = QtWidgets.QLabel(self.widget)
        self.label_select.setObjectName("label_select")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_select)
        self.label_name_file = QtWidgets.QLabel(self.widget)
        self.label_name_file.setObjectName("label_name_file")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_name_file)
        self.lineEdit_file = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_file.setObjectName("lineEdit_file")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_file)
        self.pushButton_Browse = QtWidgets.QPushButton(self.widget)
        self.pushButton_Browse.setObjectName("pushButton_Browse")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_Browse)
        self.pushButton_plot = QtWidgets.QPushButton(self.widget)
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_plot)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        # self.pushButton_Browse = QtWidgets.QPushButton(Form)
        # self.pushButton_Browse.clicked.connect(self.browsefile)
        # self.pushButton_plot = QtWidgets.QPushButton(Form)
        # self.pushButton_plot.clicked.connect(self.plot_)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Time process"))
        self.label_select.setText(_translate("Form", "select file:"))
        self.label_name_file.setText(_translate("Form", "real_<Left,Right>_<name>_<lastname>_<index>"))
        self.pushButton_Browse.setText(_translate("Form", "Browse"))
        self.pushButton_plot.setText(_translate("Form", "plot graph"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui =Ui_Plot_process_time()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec_())
