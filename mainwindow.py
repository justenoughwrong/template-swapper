# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QGridLayout,
    QHBoxLayout, QMainWindow, QMenuBar, QRadioButton,
    QSizePolicy, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(823, 997)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.websiteRadioButton = QRadioButton(self.centralwidget)
        self.templateSelectionButtonGroup = QButtonGroup(MainWindow)
        self.templateSelectionButtonGroup.setObjectName(u"templateSelectionButtonGroup")
        self.templateSelectionButtonGroup.addButton(self.websiteRadioButton)
        self.websiteRadioButton.setObjectName(u"websiteRadioButton")
        self.websiteRadioButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.websiteRadioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.websiteRadioButton, 0, Qt.AlignmentFlag.AlignRight)

        self.gunbrokerRadioButton = QRadioButton(self.centralwidget)
        self.templateSelectionButtonGroup.addButton(self.gunbrokerRadioButton)
        self.gunbrokerRadioButton.setObjectName(u"gunbrokerRadioButton")
        self.gunbrokerRadioButton.setEnabled(True)
        self.gunbrokerRadioButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.gunbrokerRadioButton.setChecked(False)

        self.horizontalLayout.addWidget(self.gunbrokerRadioButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.templateSelect = QComboBox(self.centralwidget)
        self.templateSelect.setObjectName(u"templateSelect")
        self.templateSelect.setEditable(False)
        self.templateSelect.setMaxVisibleItems(30)
        self.templateSelect.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.templateSelect.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.verticalLayout.addWidget(self.templateSelect)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.verticalLayout.addWidget(self.textBrowser)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 823, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Template Swapper", None))
        self.websiteRadioButton.setText(QCoreApplication.translate("MainWindow", u"Website Templates", None))
        self.gunbrokerRadioButton.setText(QCoreApplication.translate("MainWindow", u"GunBroker Templates", None))
    # retranslateUi

