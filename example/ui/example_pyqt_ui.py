# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example.ui'
#
# Created: Fri Jan  9 16:47:47 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(880, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.East)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.toolBox = QtGui.QToolBox(self.groupBox)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 96, 42))
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout_4 = QtGui.QGridLayout(self.page)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lineEdit = QtGui.QLineEdit(self.page)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 404, 372))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.listWidget = QtGui.QListWidget(self.page_2)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout_5.addWidget(self.listWidget, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.toolBox)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.radioButton = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout_4.addWidget(self.radioButton)
        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_4.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_2.setTristate(True)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout_4.addWidget(self.checkBox_2)
        self.treeWidget = QtGui.QTreeWidget(self.groupBox_2)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.verticalLayout_4.addWidget(self.treeWidget)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuSubmenu_2 = QtGui.QMenu(self.menuMenu)
        self.menuSubmenu_2.setObjectName(_fromUtf8("menuSubmenu_2"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget1 = QtGui.QDockWidget(MainWindow)
        self.dockWidget1.setObjectName(_fromUtf8("dockWidget1"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.dockWidgetContents)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        self.toolButton = QtGui.QToolButton(self.dockWidgetContents)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBox = QtGui.QComboBox(self.dockWidgetContents)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox)
        self.textEdit = QtGui.QTextEdit(self.dockWidgetContents)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.progressBar = QtGui.QProgressBar(self.dockWidgetContents)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.dockWidget1.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget1)
        self.dockWidget2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget2.setObjectName(_fromUtf8("dockWidget2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tableWidget = QtGui.QTableWidget(self.dockWidgetContents_2)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(4)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.dockWidget2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget2)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAction = QtGui.QAction(MainWindow)
        self.actionAction.setObjectName(_fromUtf8("actionAction"))
        self.actionSub_menu = QtGui.QAction(MainWindow)
        self.actionSub_menu.setObjectName(_fromUtf8("actionSub_menu"))
        self.actionAction_C = QtGui.QAction(MainWindow)
        self.actionAction_C.setObjectName(_fromUtf8("actionAction_C"))
        self.menuSubmenu_2.addAction(self.actionSub_menu)
        self.menuSubmenu_2.addAction(self.actionAction_C)
        self.menuMenu.addAction(self.actionAction)
        self.menuMenu.addAction(self.menuSubmenu_2.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())
        self.toolBar.addAction(self.actionAction)
        self.toolBar.addAction(self.actionSub_menu)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Page 1", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "New Item", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Page 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))
        self.radioButton.setText(_translate("MainWindow", "RadioButton", None))
        self.checkBox.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox Tristate", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "qdz", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "qzd", None))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "effefe", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.menuSubmenu_2.setTitle(_translate("MainWindow", "Submenu 2", None))
        self.dockWidget1.setWindowTitle(_translate("MainWindow", "Dock widget 1", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_3.setText(_translate("MainWindow", "Disabled", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Item 0", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Item 2", None))
        self.dockWidget2.setWindowTitle(_translate("MainWindow", "Dock widget 2", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column 2", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionAction.setText(_translate("MainWindow", "Action", None))
        self.actionSub_menu.setText(_translate("MainWindow", "Action B", None))
        self.actionSub_menu.setToolTip(_translate("MainWindow", "submenu", None))
        self.actionAction_C.setText(_translate("MainWindow", "Action C", None))

