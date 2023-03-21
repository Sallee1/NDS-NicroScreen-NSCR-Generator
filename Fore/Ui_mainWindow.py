# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QSplitter,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_mainWidget(object):
    def setupUi(self, mainWidget):
        if not mainWidget.objectName():
            mainWidget.setObjectName(u"mainWidget")
        mainWidget.resize(1024, 768)
        mainWidget.setMinimumSize(QSize(1024, 768))
        self.horizontalLayout_5 = QHBoxLayout(mainWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_left = QWidget(mainWidget)
        self.widget_left.setObjectName(u"widget_left")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_left.sizePolicy().hasHeightForWidth())
        self.widget_left.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.widget_left)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox_Palette = QGroupBox(self.widget_left)
        self.groupBox_Palette.setObjectName(u"groupBox_Palette")
        self.groupBox_Palette.setMinimumSize(QSize(300, 350))
        self.groupBox_Palette.setMaximumSize(QSize(300, 350))
        self.gridLayout_2 = QGridLayout(self.groupBox_Palette)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 0, 5, 5)
        self.widget_paletteFilter = QWidget(self.groupBox_Palette)
        self.widget_paletteFilter.setObjectName(u"widget_paletteFilter")
        self.widget_paletteFilter.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_paletteFilter.sizePolicy().hasHeightForWidth())
        self.widget_paletteFilter.setSizePolicy(sizePolicy1)
        self.widget_paletteFilter.setMaximumSize(QSize(16777215, 258))
        self.verticalLayout = QVBoxLayout(self.widget_paletteFilter)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_Pal0 = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Pal0.setObjectName(u"checkBox_Pal0")
        self.checkBox_Pal0.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Pal0)

        self.checkBox_Pal1 = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Pal1.setObjectName(u"checkBox_Pal1")
        self.checkBox_Pal1.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Pal1)

        self.checkBox_Pal2 = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Pal2.setObjectName(u"checkBox_Pal2")
        self.checkBox_Pal2.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Pal2)

        self.checkBox_Pal3 = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Pal3.setObjectName(u"checkBox_Pal3")
        self.checkBox_Pal3.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Pal3)

        self.checkBox_Pal4 = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Pal4.setObjectName(u"checkBox_Pal4")
        self.checkBox_Pal4.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Pal4)

        self.checkBox_Pal5 = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Pal5.setObjectName(u"checkBox_Pal5")
        self.checkBox_Pal5.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Pal5)

        self.checkBox_Pal6 = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Pal6.setObjectName(u"checkBox_Pal6")
        self.checkBox_Pal6.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Pal6)

        self.checkBox_Pal7 = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Pal7.setObjectName(u"checkBox_Pal7")
        self.checkBox_Pal7.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Pal7)

        self.checkBox_Pal8 = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Pal8.setObjectName(u"checkBox_Pal8")
        self.checkBox_Pal8.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Pal8)

        self.checkBox_Pal9 = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Pal9.setObjectName(u"checkBox_Pal9")
        self.checkBox_Pal9.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Pal9)

        self.checkBox_Pala = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Pala.setObjectName(u"checkBox_Pala")
        self.checkBox_Pala.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Pala)

        self.checkBox_Palb = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Palb.setObjectName(u"checkBox_Palb")
        self.checkBox_Palb.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Palb)

        self.checkBox_Palc = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Palc.setObjectName(u"checkBox_Palc")
        self.checkBox_Palc.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Palc)

        self.checkBox_Pald = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Pald.setObjectName(u"checkBox_Pald")
        self.checkBox_Pald.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Pald)

        self.checkBox_Pale = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Pale.setObjectName(u"checkBox_Pale")
        self.checkBox_Pale.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Pale)

        self.checkBox_Palf = QCheckBox(self.widget_paletteFilter)
        self.checkBox_Palf.setObjectName(u"checkBox_Palf")
        self.checkBox_Palf.setMaximumSize(QSize(16, 16777215))

        self.verticalLayout.addWidget(self.checkBox_Palf)


        self.gridLayout_2.addWidget(self.widget_paletteFilter, 1, 1, 1, 1)

        self.widget_2 = QWidget(self.groupBox_Palette)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_loadPalette = QPushButton(self.widget_2)
        self.pushButton_loadPalette.setObjectName(u"pushButton_loadPalette")

        self.horizontalLayout.addWidget(self.pushButton_loadPalette)

        self.pushButton_savePalette = QPushButton(self.widget_2)
        self.pushButton_savePalette.setObjectName(u"pushButton_savePalette")

        self.horizontalLayout.addWidget(self.pushButton_savePalette)


        self.gridLayout_2.addWidget(self.widget_2, 2, 1, 1, 2)

        self.tableWidget_Palette = QTableWidget(self.groupBox_Palette)
        if (self.tableWidget_Palette.columnCount() < 16):
            self.tableWidget_Palette.setColumnCount(16)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_Palette.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_Palette.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_Palette.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_Palette.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_Palette.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget_Palette.rowCount() < 16):
            self.tableWidget_Palette.setRowCount(16)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_Palette.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_Palette.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_Palette.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_Palette.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_Palette.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_Palette.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_Palette.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_Palette.setVerticalHeaderItem(7, __qtablewidgetitem12)
        self.tableWidget_Palette.setObjectName(u"tableWidget_Palette")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget_Palette.sizePolicy().hasHeightForWidth())
        self.tableWidget_Palette.setSizePolicy(sizePolicy3)
        self.tableWidget_Palette.setMinimumSize(QSize(258, 258))
        self.tableWidget_Palette.setMaximumSize(QSize(258, 258))
        self.tableWidget_Palette.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_Palette.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_Palette.setAutoScroll(True)
        self.tableWidget_Palette.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_Palette.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_Palette.setRowCount(16)
        self.tableWidget_Palette.setColumnCount(16)
        self.tableWidget_Palette.horizontalHeader().setVisible(False)
        self.tableWidget_Palette.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Palette.horizontalHeader().setMinimumSectionSize(16)
        self.tableWidget_Palette.horizontalHeader().setDefaultSectionSize(16)
        self.tableWidget_Palette.verticalHeader().setVisible(False)
        self.tableWidget_Palette.verticalHeader().setMinimumSectionSize(16)
        self.tableWidget_Palette.verticalHeader().setDefaultSectionSize(16)

        self.gridLayout_2.addWidget(self.tableWidget_Palette, 1, 2, 1, 1)

        self.label_PaletteInfo = QLabel(self.groupBox_Palette)
        self.label_PaletteInfo.setObjectName(u"label_PaletteInfo")
        sizePolicy2.setHeightForWidth(self.label_PaletteInfo.sizePolicy().hasHeightForWidth())
        self.label_PaletteInfo.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_PaletteInfo, 0, 1, 1, 2)

        self.widget = QWidget(self.groupBox_Palette)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.checkBox_Use4bpp = QCheckBox(self.widget)
        self.checkBox_Use4bpp.setObjectName(u"checkBox_Use4bpp")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.checkBox_Use4bpp.sizePolicy().hasHeightForWidth())
        self.checkBox_Use4bpp.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.checkBox_Use4bpp)

        self.checkBox_UseAlpha = QCheckBox(self.widget)
        self.checkBox_UseAlpha.setObjectName(u"checkBox_UseAlpha")
        sizePolicy4.setHeightForWidth(self.checkBox_UseAlpha.sizePolicy().hasHeightForWidth())
        self.checkBox_UseAlpha.setSizePolicy(sizePolicy4)
        self.checkBox_UseAlpha.setChecked(True)

        self.horizontalLayout_7.addWidget(self.checkBox_UseAlpha)


        self.gridLayout_2.addWidget(self.widget, 3, 1, 1, 2)


        self.verticalLayout_3.addWidget(self.groupBox_Palette)

        self.groupBox_TileEditor = QGroupBox(self.widget_left)
        self.groupBox_TileEditor.setObjectName(u"groupBox_TileEditor")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_TileEditor.sizePolicy().hasHeightForWidth())
        self.groupBox_TileEditor.setSizePolicy(sizePolicy5)
        self.groupBox_TileEditor.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_3 = QGridLayout(self.groupBox_TileEditor)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_ColorView = QLabel(self.groupBox_TileEditor)
        self.label_ColorView.setObjectName(u"label_ColorView")
        self.label_ColorView.setMaximumSize(QSize(64, 64))
        self.label_ColorView.setFrameShape(QFrame.Box)

        self.gridLayout_3.addWidget(self.label_ColorView, 5, 0, 3, 1)

        self.spinBox_PaletteNo = QSpinBox(self.groupBox_TileEditor)
        self.spinBox_PaletteNo.setObjectName(u"spinBox_PaletteNo")
        self.spinBox_PaletteNo.setMaximum(15)

        self.gridLayout_3.addWidget(self.spinBox_PaletteNo, 6, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_TileEditor)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.label_4, 7, 1, 1, 1)

        self.widget_TileEditorButtoms = QWidget(self.groupBox_TileEditor)
        self.widget_TileEditorButtoms.setObjectName(u"widget_TileEditorButtoms")
        self.verticalLayout_2 = QVBoxLayout(self.widget_TileEditorButtoms)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ApplyTile = QPushButton(self.widget_TileEditorButtoms)
        self.pushButton_ApplyTile.setObjectName(u"pushButton_ApplyTile")
        sizePolicy3.setHeightForWidth(self.pushButton_ApplyTile.sizePolicy().hasHeightForWidth())
        self.pushButton_ApplyTile.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.pushButton_ApplyTile)

        self.pushButton_ResetTile = QPushButton(self.widget_TileEditorButtoms)
        self.pushButton_ResetTile.setObjectName(u"pushButton_ResetTile")
        sizePolicy3.setHeightForWidth(self.pushButton_ResetTile.sizePolicy().hasHeightForWidth())
        self.pushButton_ResetTile.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.pushButton_ResetTile)

        self.pushButton_DrawScreen = QPushButton(self.widget_TileEditorButtoms)
        self.pushButton_DrawScreen.setObjectName(u"pushButton_DrawScreen")
        sizePolicy3.setHeightForWidth(self.pushButton_DrawScreen.sizePolicy().hasHeightForWidth())
        self.pushButton_DrawScreen.setSizePolicy(sizePolicy3)
        self.pushButton_DrawScreen.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_DrawScreen)


        self.gridLayout_3.addWidget(self.widget_TileEditorButtoms, 3, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox_TileEditor)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.label_2, 6, 1, 1, 1)

        self.spinBox_tileNo = QSpinBox(self.groupBox_TileEditor)
        self.spinBox_tileNo.setObjectName(u"spinBox_tileNo")
        self.spinBox_tileNo.setMaximum(1023)

        self.gridLayout_3.addWidget(self.spinBox_tileNo, 5, 2, 1, 1)

        self.comboBox_flip = QComboBox(self.groupBox_TileEditor)
        self.comboBox_flip.addItem("")
        self.comboBox_flip.addItem("")
        self.comboBox_flip.addItem("")
        self.comboBox_flip.addItem("")
        self.comboBox_flip.setObjectName(u"comboBox_flip")

        self.gridLayout_3.addWidget(self.comboBox_flip, 7, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox_TileEditor)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.label_3, 5, 1, 1, 1)

        self.tableWidget_TileCanvas = QTableWidget(self.groupBox_TileEditor)
        if (self.tableWidget_TileCanvas.columnCount() < 16):
            self.tableWidget_TileCanvas.setColumnCount(16)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_TileCanvas.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_TileCanvas.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_TileCanvas.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_TileCanvas.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_TileCanvas.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        if (self.tableWidget_TileCanvas.rowCount() < 16):
            self.tableWidget_TileCanvas.setRowCount(16)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_TileCanvas.setVerticalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_TileCanvas.setVerticalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_TileCanvas.setVerticalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_TileCanvas.setVerticalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_TileCanvas.setVerticalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_TileCanvas.setVerticalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_TileCanvas.setVerticalHeaderItem(6, __qtablewidgetitem24)
        self.tableWidget_TileCanvas.setObjectName(u"tableWidget_TileCanvas")
        sizePolicy3.setHeightForWidth(self.tableWidget_TileCanvas.sizePolicy().hasHeightForWidth())
        self.tableWidget_TileCanvas.setSizePolicy(sizePolicy3)
        self.tableWidget_TileCanvas.setMinimumSize(QSize(130, 130))
        self.tableWidget_TileCanvas.setMaximumSize(QSize(130, 130))
        self.tableWidget_TileCanvas.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_TileCanvas.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_TileCanvas.setAutoScroll(True)
        self.tableWidget_TileCanvas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_TileCanvas.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_TileCanvas.setRowCount(16)
        self.tableWidget_TileCanvas.setColumnCount(16)
        self.tableWidget_TileCanvas.horizontalHeader().setVisible(False)
        self.tableWidget_TileCanvas.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_TileCanvas.horizontalHeader().setMinimumSectionSize(16)
        self.tableWidget_TileCanvas.horizontalHeader().setDefaultSectionSize(16)
        self.tableWidget_TileCanvas.verticalHeader().setVisible(False)
        self.tableWidget_TileCanvas.verticalHeader().setMinimumSectionSize(16)
        self.tableWidget_TileCanvas.verticalHeader().setDefaultSectionSize(16)

        self.gridLayout_3.addWidget(self.tableWidget_TileCanvas, 3, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.groupBox_TileEditor)

        self.groupBox_ImageOp = QGroupBox(self.widget_left)
        self.groupBox_ImageOp.setObjectName(u"groupBox_ImageOp")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_ImageOp.sizePolicy().hasHeightForWidth())
        self.groupBox_ImageOp.setSizePolicy(sizePolicy6)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_ImageOp)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_loadImg = QPushButton(self.groupBox_ImageOp)
        self.pushButton_loadImg.setObjectName(u"pushButton_loadImg")

        self.verticalLayout_6.addWidget(self.pushButton_loadImg)

        self.pushButton_saveImg = QPushButton(self.groupBox_ImageOp)
        self.pushButton_saveImg.setObjectName(u"pushButton_saveImg")

        self.verticalLayout_6.addWidget(self.pushButton_saveImg)

        self.widget_3 = QWidget(self.groupBox_ImageOp)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_GeneratePalette = QCheckBox(self.widget_3)
        self.checkBox_GeneratePalette.setObjectName(u"checkBox_GeneratePalette")

        self.gridLayout.addWidget(self.checkBox_GeneratePalette, 0, 1, 1, 1)

        self.checkBox_comperssTiles = QCheckBox(self.widget_3)
        self.checkBox_comperssTiles.setObjectName(u"checkBox_comperssTiles")

        self.gridLayout.addWidget(self.checkBox_comperssTiles, 0, 2, 1, 1)

        self.checkBox_NoClearTile = QCheckBox(self.widget_3)
        self.checkBox_NoClearTile.setObjectName(u"checkBox_NoClearTile")

        self.gridLayout.addWidget(self.checkBox_NoClearTile, 0, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_10, 0, 3, 1, 1)


        self.verticalLayout_6.addWidget(self.widget_3)


        self.verticalLayout_3.addWidget(self.groupBox_ImageOp)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addWidget(self.widget_left)

        self.frame_right = QFrame(mainWidget)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setFrameShape(QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.hboxLayout = QHBoxLayout(self.frame_right)
        self.hboxLayout.setSpacing(0)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.frame_right)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.groupBox_Screen = QGroupBox(self.splitter)
        self.groupBox_Screen.setObjectName(u"groupBox_Screen")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_Screen)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.groupBox_Screen)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 343, 672))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)

        self.widget_7 = QWidget(self.groupBox_Screen)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.checkBox_showScreenGrid = QCheckBox(self.widget_7)
        self.checkBox_showScreenGrid.setObjectName(u"checkBox_showScreenGrid")

        self.horizontalLayout_2.addWidget(self.checkBox_showScreenGrid)

        self.label_6 = QLabel(self.widget_7)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.spinBox_ScreenZoom = QSpinBox(self.widget_7)
        self.spinBox_ScreenZoom.setObjectName(u"spinBox_ScreenZoom")
        self.spinBox_ScreenZoom.setMinimum(100)
        self.spinBox_ScreenZoom.setMaximum(1600)
        self.spinBox_ScreenZoom.setSingleStep(50)

        self.horizontalLayout_2.addWidget(self.spinBox_ScreenZoom)

        self.pushButton_LoadScreen = QPushButton(self.widget_7)
        self.pushButton_LoadScreen.setObjectName(u"pushButton_LoadScreen")
        sizePolicy4.setHeightForWidth(self.pushButton_LoadScreen.sizePolicy().hasHeightForWidth())
        self.pushButton_LoadScreen.setSizePolicy(sizePolicy4)
        self.pushButton_LoadScreen.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_LoadScreen)

        self.pushButton_SaveScreen = QPushButton(self.widget_7)
        self.pushButton_SaveScreen.setObjectName(u"pushButton_SaveScreen")
        sizePolicy4.setHeightForWidth(self.pushButton_SaveScreen.sizePolicy().hasHeightForWidth())
        self.pushButton_SaveScreen.setSizePolicy(sizePolicy4)
        self.pushButton_SaveScreen.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_SaveScreen)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.widget_7)

        self.widget_5 = QWidget(self.groupBox_Screen)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.label_10 = QLabel(self.widget_5)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.spinBox_SceeenWd = QSpinBox(self.widget_5)
        self.spinBox_SceeenWd.setObjectName(u"spinBox_SceeenWd")
        self.spinBox_SceeenWd.setMinimum(32)
        self.spinBox_SceeenWd.setMaximum(1024)
        self.spinBox_SceeenWd.setSingleStep(8)
        self.spinBox_SceeenWd.setValue(256)

        self.horizontalLayout_4.addWidget(self.spinBox_SceeenWd)

        self.label_11 = QLabel(self.widget_5)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.spinBox_ScreenHt = QSpinBox(self.widget_5)
        self.spinBox_ScreenHt.setObjectName(u"spinBox_ScreenHt")
        self.spinBox_ScreenHt.setMinimum(32)
        self.spinBox_ScreenHt.setMaximum(1024)
        self.spinBox_ScreenHt.setSingleStep(8)
        self.spinBox_ScreenHt.setValue(256)

        self.horizontalLayout_4.addWidget(self.spinBox_ScreenHt)

        self.checkBox_showScreenAlpha = QCheckBox(self.widget_5)
        self.checkBox_showScreenAlpha.setObjectName(u"checkBox_showScreenAlpha")

        self.horizontalLayout_4.addWidget(self.checkBox_showScreenAlpha)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addWidget(self.widget_5)

        self.splitter.addWidget(self.groupBox_Screen)
        self.groupBox_Tiles = QGroupBox(self.splitter)
        self.groupBox_Tiles.setObjectName(u"groupBox_Tiles")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_Tiles)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.groupBox_Tiles)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 342, 672))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea_2)

        self.widget_8 = QWidget(self.groupBox_Tiles)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.checkBox_ShowTilesGrid = QCheckBox(self.widget_8)
        self.checkBox_ShowTilesGrid.setObjectName(u"checkBox_ShowTilesGrid")

        self.horizontalLayout_3.addWidget(self.checkBox_ShowTilesGrid)

        self.label_8 = QLabel(self.widget_8)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.spinBox_TilesZoom = QSpinBox(self.widget_8)
        self.spinBox_TilesZoom.setObjectName(u"spinBox_TilesZoom")
        self.spinBox_TilesZoom.setMinimum(100)
        self.spinBox_TilesZoom.setMaximum(1600)
        self.spinBox_TilesZoom.setSingleStep(50)

        self.horizontalLayout_3.addWidget(self.spinBox_TilesZoom)

        self.pushButton_LoadTiles = QPushButton(self.widget_8)
        self.pushButton_LoadTiles.setObjectName(u"pushButton_LoadTiles")
        self.pushButton_LoadTiles.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_LoadTiles)

        self.pushButton_SaveTiles = QPushButton(self.widget_8)
        self.pushButton_SaveTiles.setObjectName(u"pushButton_SaveTiles")
        self.pushButton_SaveTiles.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_SaveTiles)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addWidget(self.widget_8)

        self.widget_6 = QWidget(self.groupBox_Tiles)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.label = QLabel(self.widget_6)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.spinBox_TilePalNo = QSpinBox(self.widget_6)
        self.spinBox_TilePalNo.setObjectName(u"spinBox_TilePalNo")
        self.spinBox_TilePalNo.setEnabled(False)
        self.spinBox_TilePalNo.setMaximum(15)

        self.horizontalLayout_6.addWidget(self.spinBox_TilePalNo)

        self.checkBox_TilesAutoPal = QCheckBox(self.widget_6)
        self.checkBox_TilesAutoPal.setObjectName(u"checkBox_TilesAutoPal")
        self.checkBox_TilesAutoPal.setEnabled(False)
        self.checkBox_TilesAutoPal.setChecked(True)

        self.horizontalLayout_6.addWidget(self.checkBox_TilesAutoPal)

        self.checkBox_maskNoUseTile = QCheckBox(self.widget_6)
        self.checkBox_maskNoUseTile.setObjectName(u"checkBox_maskNoUseTile")

        self.horizontalLayout_6.addWidget(self.checkBox_maskNoUseTile)

        self.checkBox_showTilesAlpha = QCheckBox(self.widget_6)
        self.checkBox_showTilesAlpha.setObjectName(u"checkBox_showTilesAlpha")

        self.horizontalLayout_6.addWidget(self.checkBox_showTilesAlpha)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addWidget(self.widget_6)

        self.splitter.addWidget(self.groupBox_Tiles)

        self.hboxLayout.addWidget(self.splitter)


        self.horizontalLayout_5.addWidget(self.frame_right)


        self.retranslateUi(mainWidget)
        self.checkBox_Use4bpp.toggled.connect(self.spinBox_PaletteNo.setEnabled)
        self.tableWidget_Palette.cellClicked.connect(mainWidget.onPaletteClick)
        self.tableWidget_Palette.cellDoubleClicked.connect(mainWidget.onPaletteDoubleClick)
        self.pushButton_loadPalette.clicked.connect(mainWidget.onLoadPaletteButtom)
        self.pushButton_savePalette.clicked.connect(mainWidget.onSavePaletteButtom)
        self.tableWidget_TileCanvas.cellPressed.connect(mainWidget.onTileCanvasClick)
        self.pushButton_ApplyTile.clicked.connect(mainWidget.onApplyTileCanvasButtom)
        self.pushButton_ResetTile.clicked.connect(mainWidget.onResetTileCanvasButtom)
        self.pushButton_DrawScreen.toggled.connect(mainWidget.onSwitchScreenDrawButtom)
        self.spinBox_tileNo.valueChanged.connect(mainWidget.onChangeTileNoSpinBox)
        self.spinBox_PaletteNo.valueChanged.connect(mainWidget.onChangePaletteSpinBox)
        self.comboBox_flip.currentIndexChanged.connect(mainWidget.onChangeFlipGroupBox)
        self.pushButton_loadImg.clicked["bool"].connect(mainWidget.onClickLoadImgButtom)
        self.pushButton_saveImg.clicked.connect(mainWidget.onClickSaveImgButtom)
        self.checkBox_Pal0.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Pal1.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Pal2.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Pal3.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Pal4.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Pal5.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Pal6.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Pal7.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Pal8.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Pal9.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Pala.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Palb.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Palc.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Pald.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Pale.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Palf.toggled.connect(mainWidget.onChangePaletteFilter)
        self.checkBox_Use4bpp.toggled.connect(mainWidget.onSwitch4bbpChackBox)
        self.spinBox_ScreenZoom.valueChanged.connect(mainWidget.onChangeScreenZoomSpinBox)
        self.pushButton_LoadScreen.toggled.connect(mainWidget.onClickLoadScreenButtom)
        self.pushButton_SaveScreen.toggled.connect(mainWidget.onClickSaveScreenButtom)
        self.spinBox_SceeenWd.valueChanged.connect(mainWidget.onChangeScreenSizeSpinBox)
        self.spinBox_ScreenHt.valueChanged.connect(mainWidget.onChangeScreenSizeSpinBox)
        self.checkBox_UseAlpha.toggled.connect(mainWidget.onSwitchUseAlphaChackBox)
        self.checkBox_UseAlpha.toggled.connect(self.checkBox_showTilesAlpha.setEnabled)
        self.checkBox_UseAlpha.toggled.connect(self.checkBox_showScreenAlpha.setEnabled)
        self.checkBox_showScreenGrid.toggled.connect(mainWidget.onSwitchScreenGridChackBox)
        self.checkBox_ShowTilesGrid.toggled.connect(mainWidget.onSwitchTilesGridCheckBox)
        self.spinBox_TilesZoom.valueChanged.connect(mainWidget.onChangeTileSpinBox)
        self.pushButton_LoadTiles.clicked.connect(mainWidget.onClickLoadTilesButtom)
        self.pushButton_SaveTiles.clicked.connect(mainWidget.onClickSaveTilesButtom)
        self.checkBox_TilesAutoPal.toggled.connect(mainWidget.onSwitchAutoPaletteCheckBox)
        self.checkBox_maskNoUseTile.toggled.connect(mainWidget.onSwitchMaskNoUseTileCheckBox)
        self.checkBox_showScreenAlpha.toggled.connect(mainWidget.onSwitchShowScreenAlpha)
        self.checkBox_showTilesAlpha.toggled.connect(mainWidget.onSwitchShowTilesAlpha)
        self.checkBox_TilesAutoPal.toggled.connect(self.spinBox_TilePalNo.setDisabled)
        self.checkBox_Use4bpp.toggled.connect(self.checkBox_TilesAutoPal.setEnabled)
        self.checkBox_Use4bpp.toggled.connect(self.spinBox_TilePalNo.setEnabled)
        self.spinBox_TilePalNo.valueChanged.connect(mainWidget.onChangePalShowSpinBox)
        self.checkBox_NoClearTile.toggled.connect(mainWidget.onSwitchNoClearTilesCheckBox)
        self.checkBox_GeneratePalette.toggled.connect(mainWidget.onSwitchGeneratorPaletteCheckBox)
        self.checkBox_comperssTiles.toggled.connect(mainWidget.onSwitchCompressTilesCheckBox)

        QMetaObject.connectSlotsByName(mainWidget)
    # setupUi

    def retranslateUi(self, mainWidget):
        mainWidget.setWindowTitle(QCoreApplication.translate("mainWidget", u"Nitro Srceen(NSCR)\u751f\u6210\u5668", None))
        self.groupBox_Palette.setTitle(QCoreApplication.translate("mainWidget", u"\u8c03\u8272\u677f", None))
        self.checkBox_Pal0.setText("")
        self.checkBox_Pal1.setText("")
        self.checkBox_Pal2.setText("")
        self.checkBox_Pal3.setText("")
        self.checkBox_Pal4.setText("")
        self.checkBox_Pal5.setText("")
        self.checkBox_Pal6.setText("")
        self.checkBox_Pal7.setText("")
        self.checkBox_Pal8.setText("")
        self.checkBox_Pal9.setText("")
        self.checkBox_Pala.setText("")
        self.checkBox_Palb.setText("")
        self.checkBox_Palc.setText("")
        self.checkBox_Pald.setText("")
        self.checkBox_Pale.setText("")
        self.checkBox_Palf.setText("")
        self.pushButton_loadPalette.setText(QCoreApplication.translate("mainWidget", u"\u5bfc\u5165\u8272\u677f", None))
        self.pushButton_savePalette.setText(QCoreApplication.translate("mainWidget", u"\u5bfc\u51fa\u8272\u677f", None))
        self.label_PaletteInfo.setText(QCoreApplication.translate("mainWidget", u"\u52fe\u9009\u8c03\u8272\u677f\u524d\u65b9\u7684\u590d\u9009\u6846\u6765\u6dfb\u52a0/\u6392\u9664\u8272\u677f", None))
        self.label_9.setText(QCoreApplication.translate("mainWidget", u"\u8bbe\u7f6e\uff1a", None))
#if QT_CONFIG(tooltip)
        self.checkBox_Use4bpp.setToolTip(QCoreApplication.translate("mainWidget", u"\u6bcf\u4e2aTile\u4f7f\u7528\u72ec\u7acb\u768416\u8272\u8c03\u8272\u677f", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_Use4bpp.setText(QCoreApplication.translate("mainWidget", u"4bpp", None))
#if QT_CONFIG(tooltip)
        self.checkBox_UseAlpha.setToolTip(QCoreApplication.translate("mainWidget", u"\u5c06\u7b2c\u4e00\u4e2a\u989c\u8272\u7528\u4f5c\u900f\u660e\u8272", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_UseAlpha.setText(QCoreApplication.translate("mainWidget", u"\u900f\u660e\u5ea6", None))
        self.groupBox_TileEditor.setTitle(QCoreApplication.translate("mainWidget", u"Tile\u7f16\u8f91", None))
        self.label_ColorView.setText("")
        self.label_4.setText(QCoreApplication.translate("mainWidget", u"\u7ffb\u8f6c", None))
#if QT_CONFIG(tooltip)
        self.pushButton_ApplyTile.setToolTip(QCoreApplication.translate("mainWidget", u"\u5e94\u7528tile\u4fee\u6539\u7684\u7ed3\u679c", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_ApplyTile.setText(QCoreApplication.translate("mainWidget", u"\u5e94\u7528", None))
#if QT_CONFIG(tooltip)
        self.pushButton_ResetTile.setToolTip(QCoreApplication.translate("mainWidget", u"\u64a4\u9500\u4fee\u6539", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_ResetTile.setText(QCoreApplication.translate("mainWidget", u"\u8fd8\u539f", None))
#if QT_CONFIG(tooltip)
        self.pushButton_DrawScreen.setToolTip(QCoreApplication.translate("mainWidget", u"\u542f\u7528\u540e\uff0c\u53ef\u4ee5\u5c06tile\u753b\u5728\u547d\u540d\u8868\u4e2d", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_DrawScreen.setText(QCoreApplication.translate("mainWidget", u"\u7ed8\u5236\u547d\u540d\u8868", None))
        self.label_2.setText(QCoreApplication.translate("mainWidget", u"\u8272\u677f", None))
        self.comboBox_flip.setItemText(0, QCoreApplication.translate("mainWidget", u"\u65e0", None))
        self.comboBox_flip.setItemText(1, QCoreApplication.translate("mainWidget", u"\u6c34\u5e73\u7ffb\u8f6c", None))
        self.comboBox_flip.setItemText(2, QCoreApplication.translate("mainWidget", u"\u5782\u76f4\u7ffb\u8f6c", None))
        self.comboBox_flip.setItemText(3, QCoreApplication.translate("mainWidget", u"\u65cb\u8f6c180\u5ea6", None))

        self.label_3.setText(QCoreApplication.translate("mainWidget", u"Tile", None))
        self.groupBox_ImageOp.setTitle(QCoreApplication.translate("mainWidget", u"\u56fe\u50cf\u64cd\u4f5c", None))
#if QT_CONFIG(tooltip)
        self.pushButton_loadImg.setToolTip(QCoreApplication.translate("mainWidget", u"\u5bfc\u5165\u56fe\u50cf\uff0c\u5e76\u81ea\u52a8\u8ba1\u7b97\u547d\u540d\u8868\u548ctiles", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_loadImg.setText(QCoreApplication.translate("mainWidget", u"\u5bfc\u5165\u56fe\u50cf", None))
        self.pushButton_saveImg.setText(QCoreApplication.translate("mainWidget", u"\u5bfc\u51fa\u56fe\u50cf", None))
#if QT_CONFIG(tooltip)
        self.checkBox_GeneratePalette.setToolTip(QCoreApplication.translate("mainWidget", u"\u3010\u5b9e\u9a8c\u6027\u3011\u5c1d\u8bd5\u4ece\u56fe\u50cf\u4e2d\u63d0\u53d6\u8c03\u8272\u677f\u5e76\u66ff\u6362\u73b0\u6709\u7684\u8c03\u8272\u677f", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_GeneratePalette.setText(QCoreApplication.translate("mainWidget", u"\u81ea\u52a8\u751f\u6210\u8272\u677f", None))
#if QT_CONFIG(tooltip)
        self.checkBox_comperssTiles.setToolTip(QCoreApplication.translate("mainWidget", u"\u3010\u5b9e\u9a8c\u6027\u3011\u901a\u8fc7\u6709\u635f\u7684\u538b\u7f29\u51cf\u5c11tile\u6570\u636e\u7684\u5927\u5c0f", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_comperssTiles.setText(QCoreApplication.translate("mainWidget", u"\u538b\u7f29", None))
#if QT_CONFIG(tooltip)
        self.checkBox_NoClearTile.setToolTip(QCoreApplication.translate("mainWidget", u"\u5bfc\u5165\u65f6\u4e0d\u6e05\u7a7atile\uff0c\u800c\u662f\u7ee7\u7eed\u5f80\u540e\u8ffd\u52a0\uff0c\u9002\u7528\u591a\u4e2a\u547d\u540d\u8868\u5171\u7528\u4e00\u4e2atile\u56fe\u5f62\u7684\u60c5\u51b5", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_NoClearTile.setText(QCoreApplication.translate("mainWidget", u"\u4e0d\u6e05\u7a7atile", None))
        self.groupBox_Screen.setTitle(QCoreApplication.translate("mainWidget", u"\u547d\u540d\u8868\u9884\u89c8", None))
        self.label_5.setText(QCoreApplication.translate("mainWidget", u"\u5f53\u524d\u672a\u6253\u5f00\u547d\u540d\u8868", None))
        self.checkBox_showScreenGrid.setText(QCoreApplication.translate("mainWidget", u"\u7f51\u7edc\u7ebf", None))
        self.label_6.setText(QCoreApplication.translate("mainWidget", u"\u7f29\u653e", None))
        self.pushButton_LoadScreen.setText(QCoreApplication.translate("mainWidget", u"\u5bfc\u5165\u547d\u540d\u8868", None))
        self.pushButton_SaveScreen.setText(QCoreApplication.translate("mainWidget", u"\u5bfc\u51fa\u547d\u540d\u8868", None))
        self.label_10.setText(QCoreApplication.translate("mainWidget", u"\u5bbd", None))
        self.label_11.setText(QCoreApplication.translate("mainWidget", u"\u9ad8", None))
        self.checkBox_showScreenAlpha.setText(QCoreApplication.translate("mainWidget", u"\u900f\u660e", None))
        self.groupBox_Tiles.setTitle(QCoreApplication.translate("mainWidget", u"Tiles\u9884\u89c8", None))
        self.label_7.setText(QCoreApplication.translate("mainWidget", u"\u5f53\u524d\u6ca1\u6709Tile", None))
        self.checkBox_ShowTilesGrid.setText(QCoreApplication.translate("mainWidget", u"\u7f51\u7edc\u7ebf", None))
        self.label_8.setText(QCoreApplication.translate("mainWidget", u"\u7f29\u653e", None))
        self.pushButton_LoadTiles.setText(QCoreApplication.translate("mainWidget", u"\u5bfc\u5165Tile", None))
        self.pushButton_SaveTiles.setText(QCoreApplication.translate("mainWidget", u"\u5bfc\u51faTile", None))
        self.label.setText(QCoreApplication.translate("mainWidget", u"\u8272\u677f", None))
        self.checkBox_TilesAutoPal.setText(QCoreApplication.translate("mainWidget", u"\u81ea\u52a8\u8272\u677f", None))
        self.checkBox_maskNoUseTile.setText(QCoreApplication.translate("mainWidget", u"\u906e\u7f69\u672a\u4f7f\u7528", None))
        self.checkBox_showTilesAlpha.setText(QCoreApplication.translate("mainWidget", u"\u900f\u660e", None))
    # retranslateUi

