#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
import winshell
import os
import math
import shutil



class Ui_MainWindow(object):
    def setupUi(self, MainWindow, c):
        self.currentItem = None
        self.currentItemCheck = False
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 700))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 99, 900, 581))
        self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setColumnCount(1)
        # #         self.tableWidget.setRowCount(1)
        #-----------------------------------columns------------------
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        #-----------------------------------rows-------------------
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        #---------------------------------------------------------
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(220)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(150)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 100))
        self.label.setStyleSheet("background-image: url(:/header/images/Untitled-1.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(900, 269, 300, 411))
        self.label_2.setStyleSheet("\n"
"background-color: rgb(212, 212, 212); font: 63 10pt \"Segoe UI Semibold\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(940, 120, 200, 50))
        self.pushButton.setStyleSheet("background-image: url(:/header/images/btn-1_3.png);")
        self.pushButton.setText("")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(940, 190, 200, 50))
        self.pushButton_2.setStyleSheet("background-image: url(:/Buttons/images/btn-2_2.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(310, 700, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(900, 260, 301, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.pushButton_2.clicked.connect(self.RestoreButton)
        self.pushButton.clicked.connect(self.DeleteButton)

        #------------------------------------------------------
        # self.verticalLayoutWidget.hide()
        # self.verticalLayoutWidget_2.hide()
        self.tableWidget.cellClicked.connect(self.cellClicked)
        self.tableWidget.cellDoubleClicked.connect(self.cellDClicked)
        #-----------------------------------------------------
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.label_2.setWordWrap(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        if c == True:
            #---------------------------------------------------------Listing all the files from Trash---------------------




            r = list(winshell.recycle_bin())
            self.sizeOfList = len(r)
            if self.sizeOfList >= 4:
                self.tableWidget.setColumnCount(4)
                self.tableWidget.setRowCount(math.ceil(self.sizeOfList/4))

            else:
                self.tableWidget.setColumnCount(self.sizeOfList)
                self.tableWidget.setRowCount(1)

            class DeletedObject:
                def __init__(self, obj, typeOfObj,name, sahiPath, size, addOn, row, col):
                    self.obj = obj
                    self.typeOfObj = typeOfObj
                    self.name = name
                    self.sahiPath = sahiPath
                    self.size = size
                    self.addOn = addOn
                    self.row = row
                    self.col = col

            self.dictOfObjs = {}
            row = 0
            col = 0

            for i,v in enumerate(r):
                addOn = []
                col = i % 4
                if i != 0 and col == 0:
                    row += 1
                total = v.original_filename().split('\\')
                okPath = "\\\\".join(total)
                v.undelete()
                if os.path.isdir(okPath):
                    typee = "Folder"
                    size = self.get_dir_size(okPath)
                    addOn.append([file for file in os.listdir(okPath) if os.path.isdir(okPath + "\\" + file)])
                    addOn.append([file for file in os.listdir(okPath) if os.path.isfile(okPath + "\\" + file)])

                    self.FolderCreator(total[-1], row,col)
                elif os.path.isfile(okPath):
                    typee = "File"
                    size = os.path.getsize(okPath)
                    self.FileCreator(total[-1], row,col)
                winshell.delete_file(okPath)
                self.dictOfObjs[i] = DeletedObject(v,typee, total[-1], okPath, size, addOn, row, col)



                # item = QTableWidgetItem(str(total[-1]+"|"+typee))
                # item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                # self.tableWidget.setItem(row,col,item )
        elif c == False:
            if self.sizeOfList >= 4:
                self.tableWidget.setColumnCount(4)
                self.tableWidget.setRowCount(math.ceil(self.sizeOfList/4))

            else:
                self.tableWidget.setColumnCount(self.sizeOfList)
                self.tableWidget.setRowCount(1)
            for k, v in self.dictOfObjs.items():
                if v.typeOfObj == "File":
                    self.FileCreator(v.name, v.row, v.col)
                elif v.typeOfObj == "Folder":
                    self.FolderCreator(v.name, v.row, v.col)

    def get_dir_size(self,start_path='.'):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)

        return total_size
    def FileCreator(self,nameOfFile, fRow, fCol):
        # ----------------------------FILE------------------
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        # self.verticalLayoutWidget.setGeometry(QtCore.QRect(0,0,220, 150))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        # self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        # self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("\n"
                                   "image: url(:/pic/images/file.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.fileLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.fileLabel.setObjectName("fileLabel")
        self.verticalLayout.addWidget(self.fileLabel)
        _translate = QtCore.QCoreApplication.translate
        self.fileLabel.setText(_translate("MainWindow", str(nameOfFile)))
        self.tableWidget.setCellWidget(fRow, fCol, self.verticalLayoutWidget)

    def FolderCreator(self, nameOfFolder, fRow, fCol):
        # ----------------------FOLDER---------------------------
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        # self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(250, 100, 181, 151))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        # self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        # self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setStyleSheet("image: url(:/pic/images/folder.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.folderLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.folderLabel.setObjectName("folderLabel")
        self.verticalLayout_2.addWidget(self.folderLabel)
        _translate = QtCore.QCoreApplication.translate
        self.folderLabel.setText(_translate("MainWindow", str(nameOfFolder)))

        self.tableWidget.setCellWidget(fRow, fCol, self.verticalLayoutWidget_2)


    def cellClicked(self, row,col):
        try:
            strList = ["- PROPERTIES -"]
            index = (row*4)+col
            obj = self.dictOfObjs[index]
            self.currentItem = obj
            objPath = obj.sahiPath
            strList.append("NAME: "+ obj.name)
            if obj.typeOfObj == "File":
                strList.append("PATH: "+objPath)
                ext = objPath.split(".")
                if len(ext) == 1:
                    strList.append("Extension: FILE")
                else:
                    strList.append("Extension: "+ ext[1])
                strList.append("SIZE: "+ "{0:.1f}".format((obj.size / 1024) / 1024)+"MB")
            elif obj.typeOfObj == "Folder":

                strList.append("PATH: "+objPath)
                strList.append("SIZE: "+str("{0:.1f}".format((obj.size / 1024) / 1024))+ "MB")
                strList.append("No Of Folders: "+ str(len(obj.addOn[0])))
                strList.append("No Of Files: "+ str(len(obj.addOn[1])))
                # print(obj.addOn)
            strLabel = "\n\n".join(strList)
            _translate = QtCore.QCoreApplication.translate
            self.label_2.setText(_translate("MainWindow", strLabel))
        except:
            pass





    def cellDClicked(self, row,col):
        try:
            index = (row * 4) + col
            obj = self.dictOfObjs[index]
            self.currentItem = obj
            if obj.typeOfObj == "File":
                self.FileUI(MainWindow,None, obj, True, [])
            elif obj.typeOfObj == "Folder":
                self.FolderUi(MainWindow, obj, True, False, None, None)
        except:
            self.msgBox("Empty Cell", "Please select a valid cell")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main"))
       
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "--"))

    def FileUI(self, MainWindow, cont, selected, main, lst):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 700))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 100))
        self.label.setStyleSheet("background-image: url(:/header/images/Untitled-1.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(900, 269, 300, 411))
        self.label_2.setStyleSheet("\n"
                                   "background-color: rgb(212, 212, 212);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(940, 120, 200, 50))
        self.pushButton.setStyleSheet("background-image: url(:/header/images/btn-1_3.png);")
        self.pushButton.setText("")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(940, 190, 200, 50))
        self.pushButton_2.setStyleSheet("background-image: url(:/Buttons/images/btn-2_2.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(310, 700, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(900, 260, 301, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 100, 901, 71))
        self.label_5.setStyleSheet("\n"
                                   "background-image: url(:/pic/images/patti_5.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 118, 121, 41))
        self.pushButton_3.setStyleSheet("background-image: url(:/Buttons/images/back_3.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 118, 751, 41))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 63 14pt \"Segoe UI Semibold\";")
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 170, 900, 520))
        self.textEdit.setObjectName("textEdit")
        self.label_5.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.pushButton_3.raise_()
        self.label_6.raise_()
        self.textEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.textEdit.setReadOnly(True)

        # self.pushButton_2.clicked.connect(self.RestoreButton)
        # self.pushButton.clicked.connect(self.DeleteButton)

        try:
            self.lst = lst
            if cont == None:
                winshell.undelete(selected.obj.original_filename())
                file = open(selected.sahiPath, "r")
                content = file.read()
                file.close()
                winshell.delete_file(selected.obj.original_filename())
                self.textEdit.setPlainText(content)
            else:

                self.textEdit.setPlainText(cont)
        except:
            self.msgBox("ERROR", "Can't Open This Type of File")
        if main == True:
            self.pushButton_3.clicked.connect(self.goBack)
        else:

            self.pushButton_3.clicked.connect(self.goCustomBack)

    def goCustomBack(self):
        self.FolderUi(MainWindow, self.lst[0], self.lst[1], True, self.lst[3], self.lst[4])
        # self.setupUi(MainWindow, False)
    def goBack(self):
        self.setupUi(MainWindow, False)

    def FolderUi(self, MainW, selected, main, iter, path, lst ):
        MainWindow = MainW
        # MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.currentItemCheck = True
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 700))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 160, 900, 520))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(225)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(150)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 100))
        self.label.setStyleSheet("background-image: url(:/header/images/Untitled-1.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(900, 269, 300, 411))
        self.label_2.setStyleSheet("\n"
                                   "background-color: rgb(212, 212, 212);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(940, 120, 200, 50))
        self.pushButton.setStyleSheet("background-image: url(:/header/images/btn-1_3.png);")
        self.pushButton.setText("")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(940, 190, 200, 50))
        self.pushButton_2.setStyleSheet("background-image: url(:/Buttons/images/btn-2_2.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(310, 700, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(900, 260, 301, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 100, 901, 71))
        self.label_5.setStyleSheet("\n"
                                   "background-image: url(:/pic/images/patti_5.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 112, 121, 41))
        self.pushButton_3.setStyleSheet("background-image: url(:/Buttons/images/back_3.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 110, 751, 41))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 63 14pt \"Segoe UI Semibold\";")
        self.label_6.setObjectName("label_6")
        self.label_5.raise_()
        self.tableWidget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.pushButton_3.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.tableWidget.cellClicked.connect(self.FolderCellClicked)
        self.tableWidget.cellDoubleClicked.connect(self.folderCellDClicked)
        if iter == False:
            winshell.undelete(selected.obj.original_filename())
        if main == True:
            self.folderPath = selected.sahiPath
            self.listOfFolderItems = os.listdir(selected.sahiPath)
        elif main == False:
            self.folderPath = path
            self.listOfFolderItems = os.listdir(path)
        sizeOfList = len(self.listOfFolderItems)
        if sizeOfList >= 4:
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setRowCount(math.ceil(sizeOfList / 4))
        else:
            self.tableWidget.setColumnCount(sizeOfList)
            self.tableWidget.setRowCount(1)
        row =0
        col = 0
        for i,v in enumerate(self.listOfFolderItems):
            col = i % 4
            if i != 0 and col == 0:
                row += 1
            ext = v.split(".")
            if len(ext) == 1:
                self.FolderCreator(v, row, col)
            else:
                self.FileCreator(v, row, col)

        self.main = main
        self.selected = selected
        self.lst = lst
        self.lstOfParams = [selected, main, iter, path, lst]

        self.pushButton_3.clicked.connect(self.folderGopBack)

    def folderGopBack(self):
        if self.main == True:
            winshell.delete_file(self.selected.obj.original_filename())
            self.goBack()
        if self.main == False:
            self.FolderUi(MainWindow, self.lst[0], self.lst[1], True, self.lst[3], self.lst[4])

    def FolderCellClicked(self, row, col):
        try:
            strList = ["- PROPERTIES -"]
            index = (row * 4) + col
            obj = self.listOfFolderItems[index]
            objPath = self.folderPath + "\\\\" + obj
            strList.append("NAME: " + obj)
            extn = obj.split(".")
            if len(extn) != 1:
                strList.append("PATH: " + objPath)
                ext = objPath.split(".")
                if len(ext) == 1:
                    strList.append("Extension: FILE")
                else:
                    strList.append("Extension: " + ext[1])
                s = os.path.getsize(objPath)
                strList.append("SIZE: " + "{0:.1f}".format((s / 1024) / 1024) + "MB")
            elif len(extn) == 1:

                strList.append("PATH: " + objPath)
                strList.append("SIZE: " + str("{0:.1f}".format((self.get_dir_size(objPath) / 1024) / 1024)) + "MB")
                strList.append("No Of Folders: " + str(len([file for file in os.listdir(objPath) if os.path.isdir(objPath + "\\" + file)])))
                strList.append("No Of Files: " + str(len([file for file in os.listdir(objPath) if os.path.isfile(objPath + "\\" + file)])))
                # print(obj.addOn)
            # print(strList)
            strLabel = "\n\n".join(strList)
            _translate = QtCore.QCoreApplication.translate
            self.label_2.setText(_translate("MainWindow", strLabel))
        except:
            pass

    def folderCellDClicked(self, row, col):
        try:
            index = (row * 4) + col
            item = self.listOfFolderItems[index]
            objPath = self.folderPath + "\\\\" + item
            if os.path.isfile(objPath):
                try:
                    file = open(objPath, "r")
                    content = file.read()
                    file.close()
                    self.FileUI(MainWindow, content, None, False, self.lstOfParams)
                except:
                    self.msgBox("ERROR", "Can't Open This Type of File")
            elif os.path.isdir(objPath):
                self.FolderUi(MainWindow, None, False, True, objPath, self.lstOfParams)
        except:
            self.msgBox("Empty Cell", "Please select a valid cell")

    def RestoreButton(self):
        if self.currentItemCheck == False:
            winshell.undelete(self.currentItem.obj.original_filename())
        self.setupUi(MainWindow, True)
    def DeleteButton(self):
        if self.currentItemCheck == False:
            winshell.undelete(self.currentItem.obj.original_filename())
        if self.currentItem.typeOfObj == "File":
            os.remove(self.currentItem.sahiPath)
        elif self.currentItem.typeOfObj == "Folder":
            shutil.rmtree(self.currentItem.sahiPath)
        self.setupUi(MainWindow, True)

    def msgBox(self, title, msg):
        a = QtWidgets.QMessageBox()
        a.setWindowTitle(title)
        a.setText(msg)
        a.setStandardButtons(QtWidgets.QMessageBox.Ok)
        a.exec_()




import mainRes


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, True)
    MainWindow.show()
    sys.exit(app.exec_())
