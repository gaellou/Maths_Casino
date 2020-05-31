import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget, QPushButton, QRadioButton, QHBoxLayout
from PyQt5 import uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

import sys
import time
import random
import pyaudio
import wave
import time
from random import *
import math as math

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import sqlite3



class MainWindow(QtWidgets.QMainWindow):

    #def WarmUpClicked(self) :
     #   dialog = ApplicationWindow(self)
       #  self.dialogs.append(dialog)
        #dialog.show()


    def PracticeClicked(self) :
        dialog = TraningWindow(self)
        self.dialogs.append(dialog)
        dialog.show()




    def SolfegeClicked(self) :
        dialog = SolfegeWindow(self)
        self.dialogs.append(dialog)
        dialog.show()


    def PhysicClicked(self) :
        dialog = PhysicWindow(self)
        self.dialogs.append(dialog)
        dialog.show()

    def RecordClicked(self) :
        dialog = RecordWindow(self)
        self.dialogs.append(dialog)
        dialog.show()




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mainwindow.ui", self)

        self.setWindowTitle("MusicTraining")

        self.dialogs = list()

       # buttonWarmUp= QPushButton("Je chauffe", self)
        #buttonWarmUp.move(270,500)
       # buttonWarmUp.setFixedHeight(50)
        #buttonWarmUp.setStyleSheet("background-color: white")
        #buttonWarmUp.clicked.connect(self.WarmUpClicked)

        buttonPractice= QPushButton("Je m'entraine", self)
        buttonPractice.move(320,500)
        buttonPractice.setFixedHeight(50)
        buttonPractice.setStyleSheet("background-color: white")
        buttonPractice.clicked.connect(self.PracticeClicked)

        buttonSolfege= QPushButton("Mémo de Solfège", self)
        buttonSolfege.move(690,500)
        buttonSolfege.setFixedHeight(50)
        buttonSolfege.setFixedWidth(125)
        buttonSolfege.setStyleSheet("background-color: white")
        buttonSolfege.clicked.connect(self.SolfegeClicked)

        buttonRecord= QPushButton("Je m'enregistre", self)
        buttonRecord.move(480,500)
        buttonRecord.setFixedHeight(50)
        buttonRecord.setFixedWidth(125)
        buttonRecord.setStyleSheet("background-color: white")
        buttonRecord.clicked.connect(self.RecordClicked)


        buttonPhysic= QPushButton("Physique du son", self)
        buttonPhysic.move(900,500)
        buttonPhysic.setFixedHeight(50)
        buttonPhysic.setFixedWidth(125)
        buttonPhysic.setStyleSheet("background-color: white")
        buttonPhysic.clicked.connect(self.PhysicClicked)


