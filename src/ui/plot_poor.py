# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_poor.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_plot_poor_body(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(551, 427)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 531, 401))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_alltime = QtWidgets.QLabel(self.widget)
        self.label_alltime.setObjectName("label_alltime")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_alltime)
        self.label_namealltimefile = QtWidgets.QLabel(self.widget)
        self.label_namealltimefile.setObjectName("label_namealltimefile")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_namealltimefile)
        self.lineEdit_filenamealltime = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_filenamealltime.setObjectName("lineEdit_filenamealltime")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_filenamealltime)
        self.pushButton_alltime = QtWidgets.QPushButton(self.widget)
        self.pushButton_alltime.setObjectName("pushButton_alltime")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton_alltime)
        self.verticalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_timepooralert = QtWidgets.QLabel(self.widget)
        self.label_timepooralert.setObjectName("label_timepooralert")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_timepooralert)
        self.label_nametimepooralertfile = QtWidgets.QLabel(self.widget)
        self.label_nametimepooralertfile.setObjectName("label_nametimepooralertfile")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_nametimepooralertfile)
        self.lineEdit_filetimepooralert = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_filetimepooralert.setObjectName("lineEdit_filetimepooralert")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_filetimepooralert)
        self.pushButton_timepooralert = QtWidgets.QPushButton(self.widget)
        self.pushButton_timepooralert.setObjectName("pushButton_timepooralert")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton_timepooralert)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_timepoor = QtWidgets.QLabel(self.widget)
        self.label_timepoor.setObjectName("label_timepoor")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_timepoor)
        self.label_nametimepoor = QtWidgets.QLabel(self.widget)
        self.label_nametimepoor.setObjectName("label_nametimepoor")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_nametimepoor)
        self.lineEdit_filetimepoor = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_filetimepoor.setObjectName("lineEdit_filetimepoor")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_filetimepoor)
        self.pushButton_timepoor = QtWidgets.QPushButton(self.widget)
        self.pushButton_timepoor.setObjectName("pushButton_timepoor")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton_timepoor)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Plot-poor"))
        self.label_alltime.setText(_translate("Form", "select file: "))
        self.label_namealltimefile.setText(_translate("Form", "all_Time_<name>_<lastname>_<index>.csv"))
        self.pushButton_alltime.setText(_translate("Form", "Browse.."))
        self.label_timepooralert.setText(_translate("Form", "select file: "))
        self.label_nametimepooralertfile.setText(_translate("Form", "time_poor_alert_<name>_<lastname>_<index>.csv"))
        self.pushButton_timepooralert.setText(_translate("Form", "Browse.."))
        self.label_timepoor.setText(_translate("Form", "select file: "))
        self.label_nametimepoor.setText(_translate("Form", "time_poor_<name>_<lastname>_<index>.csv"))
        self.pushButton_timepoor.setText(_translate("Form", "Browse.."))
        self.pushButton.setText(_translate("Form", "Plot graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_plot_poor_body()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
