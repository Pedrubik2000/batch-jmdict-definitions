# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Definitions_getter(object):
    def setupUi(self, Definitions_getter):
        Definitions_getter.setObjectName("Definitions_getter")
        Definitions_getter.resize(400, 320)
        Definitions_getter.setAutoFillBackground(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Definitions_getter)
        self.buttonBox.setGeometry(QtCore.QRect(40, 270, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.TextField = QtWidgets.QTextBrowser(Definitions_getter)
        self.TextField.setGeometry(QtCore.QRect(60, 60, 141, 41))
        self.TextField.setObjectName("TextField")
        self.TextAction = QtWidgets.QTextBrowser(Definitions_getter)
        self.TextAction.setGeometry(QtCore.QRect(60, 150, 281, 61))
        self.TextAction.setObjectName("TextAction")
        self.TextNbDefinitions = QtWidgets.QTextBrowser(Definitions_getter)
        self.TextNbDefinitions.setGeometry(QtCore.QRect(60, 20, 191, 31))
        self.TextNbDefinitions.setAutoFillBackground(False)
        self.TextNbDefinitions.setObjectName("TextNbDefinitions")
        self.selector_NbDefinitions = QtWidgets.QSpinBox(Definitions_getter)
        self.selector_NbDefinitions.setGeometry(QtCore.QRect(260, 20, 81, 31))
        self.selector_NbDefinitions.setMinimum(1)
        self.selector_NbDefinitions.setMaximum(10)
        self.selector_NbDefinitions.setObjectName("selector_NbDefinitions")
        self.combo_action = QtWidgets.QComboBox(Definitions_getter)
        self.combo_action.setGeometry(QtCore.QRect(60, 220, 281, 26))
        self.combo_action.setObjectName("combo_action")
        self.combo_action.addItem("")
        self.combo_action.addItem("")
        self.combo_field_src = QtWidgets.QComboBox(Definitions_getter)
        self.combo_field_src.setGeometry(QtCore.QRect(60, 110, 141, 31))
        self.combo_field_src.setObjectName("combo_field_src")
        self.TextField_2 = QtWidgets.QTextBrowser(Definitions_getter)
        self.TextField_2.setGeometry(QtCore.QRect(210, 60, 131, 41))
        self.TextField_2.setObjectName("TextField_2")
        self.combo_field_dst = QtWidgets.QComboBox(Definitions_getter)
        self.combo_field_dst.setGeometry(QtCore.QRect(210, 110, 131, 31))
        self.combo_field_dst.setObjectName("combo_field_dst")

        self.retranslateUi(Definitions_getter)
        self.buttonBox.accepted.connect(Definitions_getter.accept) # type: ignore
        self.buttonBox.rejected.connect(Definitions_getter.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Definitions_getter)

    def retranslateUi(self, Definitions_getter):
        _translate = QtCore.QCoreApplication.translate
        Definitions_getter.setWindowTitle(_translate("Definitions_getter", "Definition getter"))
        self.TextField.setMarkdown(_translate("Definitions_getter", "Source Field\n"
"\n"
""))
        self.TextField.setHtml(_translate("Definitions_getter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Source Field</p></body></html>"))
        self.TextAction.setMarkdown(_translate("Definitions_getter", "Action (warning : overwrite erases all the previous data in the field)\n"
"\n"
""))
        self.TextAction.setHtml(_translate("Definitions_getter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Action (warning : overwrite erases all the previous data in the field)</p></body></html>"))
        self.TextNbDefinitions.setHtml(_translate("Definitions_getter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Number of definitions</span></p></body></html>"))
        self.combo_action.setItemText(0, _translate("Definitions_getter", "Overwrite"))
        self.combo_action.setItemText(1, _translate("Definitions_getter", "Append"))
        self.TextField_2.setMarkdown(_translate("Definitions_getter", "Dest. Field\n"
"\n"
""))
        self.TextField_2.setHtml(_translate("Definitions_getter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dest. Field</p></body></html>"))