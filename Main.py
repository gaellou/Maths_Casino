import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget, QPushButton, QRadioButton, QHBoxLayout
from PyQt5 import uic

import random

import time
from random import *
import math as math

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from Proba import *



class MainWindow(QtWidgets.QMainWindow):

    def Clicked01(self) :
        value = int(random() * 34)
        print(value)
        mise = int(self.pari.text())
        piece = self.Pieces.text()
        self.Result.setText(str(value))
        if int(piece) > 10:
            if value != mise :
                piece = int(piece)-10
                self.Error.setText("Perdu... (-10)")
                self.Error.setStyleSheet('color: red ; font: 20pt Arial;')
            else :
                piece = int(piece) + 150
                self.Error.setText("Gagné ! (+150)")
                self.Error.setStyleSheet('color: white ; font: 20pt Arial;')
        else :
            self.Error.setText("Pas assez de pièces !")
            self.Error.setStyleSheet('color: orange ; font: 20pt Arial;')
        self.Pieces.setText(str(piece))




    def Clicked02(self) :
        value = int( hgauss())
        print(value)
        mise = int(self.pari.text())
        piece = self.Pieces.text()
        self.Result.setText(str(value))
        if int(piece) > 10:
            if value != mise :
                piece = int(piece)-10
                self.Error.setText("Perdu... (-10)")
                self.Error.setStyleSheet('color: red ; font: 20pt Arial;')
            else :
                piece = int(piece) + 75
                self.Error.setText("Gagné !(+75)")
                self.Error.setStyleSheet('color: white ; font: 20pt Arial;')
        else :
            self.Error.setText("Pas assez de pièces !")
            self.Error.setStyleSheet('color: orange ; font: 20pt Arial;')
        self.Pieces.setText(str(piece))



    def Clicked03(self) :
        value=hpoisson(2)
        print(value)
        mise = int(self.pari.text())
        piece = self.Pieces.text()
        self.Result.setText(str(value))
        if int(piece) > 10:
            if value != mise :
                piece = int(piece)-10
                self.Error.setText("Perdu... (-10)")
                self.Error.setStyleSheet('color: red ; font: 20pt Arial;')
            else :
                piece = int(piece) + 100
                self.Error.setText("Gagné !(+100)")
                self.Error.setStyleSheet('color: white ; font: 20pt Arial;')
        else :
            self.Error.setText("Pas assez de pièces !")
            self.Error.setStyleSheet('color: orange; font: 20pt Arial;')
        self.Pieces.setText(str(piece))

    def Clicked04(self) :
        p=random()
        value= hbinom(38,p)
        print(value)
        mise = int(self.pari.text())
        piece = self.Pieces.text()
        self.Result.setText(str(value))
        if int(piece) > 10:
            if value != mise :
                piece = int(piece)-10
                self.Error.setText("Perdu... (-10)")
                self.Error.setStyleSheet('color: red ; font: 20pt Arial;')
            else :
                piece = int(piece) + 120
                self.Error.setText("Gagné ! (+120)")
                self.Error.setStyleSheet('color: white ; font: 20pt Arial;')
        else :
            self.Error.setText("Pas assez de pièces !")
            self.Error.setStyleSheet('color: orange; font: 20pt Arial;')
        self.Pieces.setText(str(piece))



    def Clicked05(self) :
        p = 18/35
        c = 0
        piece = self.Pieces.text()
        piece = int(piece) - 10
        for i in range (0,1) :
            t=random()
            if t<p :
                c=c+1
        if c == 2 :
            self.Error.setText("Gagné ! (+100)")
            pieces = int(piece)+100
        else :
            self.Error.setText("Perdu... (-10)")
        self.Pieces.setText(str(piece))




    def Clickedplus(self) :
        num_text = self.pari.text()
        num = int(num_text) + 1
        self.pari.setText(str(num))


    def Clickedmoin(self) :
        num_text = self.pari.text()
        num = int(num_text) - 1
        self.pari.setText(str(num))



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mainwindow.ui", self)

        self.setWindowTitle("MathProject")

        self.dialogs = list()

        win = QWidget()

        self.Pieces = QLabel("500",self)
        self.Pieces.move(900,20)
        self.Pieces.setStyleSheet("font: 30pt Arial")
        self.Pieces.setStyleSheet('color: white; font: 30pt Arial;')
        self.Pieces.show()

        self.Error = QLabel("",self)
        self.Error.move(380,100)
        self.Error.setFixedWidth(300)
        self.Error.setStyleSheet("font: 30pt Arial")
        self.Error.setStyleSheet('color: white; font: 30pt Arial;')
        self.Error.show()

        self.pari = QLabel("19", self)
        self.pari.move(140,22)
        self.pari.setStyleSheet("font: 30pt Arial")
        self.pari.setStyleSheet('color: white; font: 30pt Arial;')
        self.pari.show()

        self.TxtResult = QLabel("Result :  ",self)
        self.TxtResult.move(90,100)
        self.TxtResult.setStyleSheet("font: 20pt Arial")
        self.TxtResult.setStyleSheet('color: white; font: 20pt Arial;')
        self.TxtResult.show()

        self.Result = QLabel(" ",self)
        self.Result.move(190,100)
        self.Result.setStyleSheet("font: 20pt Arial")
        self.Result.setStyleSheet('color: white; font: 20pt Arial;')
        self.Result.show()


        buttonplus= QPushButton("+", self)
        buttonplus.move(200,20)
        buttonplus.setFixedHeight(50)
        buttonplus.setStyleSheet("background-color: white")
        buttonplus.clicked.connect(self.Clickedplus)

        buttonmoin= QPushButton("-", self)
        buttonmoin.move(20,20)
        buttonmoin.setFixedHeight(50)
        buttonmoin.setStyleSheet("background-color: white")
        buttonmoin.clicked.connect(self.Clickedmoin)

        button01= QPushButton("Chance 01", self)
        button01.move(100,200)
        button01.setFixedHeight(50)
        button01.setStyleSheet("background-color: white")
        button01.clicked.connect(self.Clicked01)

        button02= QPushButton("Chance 02", self)
        button02.move(290,200)
        button02.setFixedHeight(50)
        button02.setStyleSheet("background-color: white")
        button02.clicked.connect(self.Clicked02)

        button03= QPushButton("Chance 04", self)
        button03.move(690,200)
        button03.setFixedHeight(50)
        button03.setFixedWidth(125)
        button03.setStyleSheet("background-color: white")
        button03.clicked.connect(self.Clicked03)

        button04= QPushButton("Chance 03", self)
        button04.move(480,200)
        button04.setFixedHeight(50)
        button04.setFixedWidth(125)
        button04.setStyleSheet("background-color: white")
        button04.clicked.connect(self.Clicked04)


        button05= QPushButton("Chance 05", self)
        button05.move(900,200)
        button05.setFixedHeight(50)
        button05.setFixedWidth(125)
        button05.setStyleSheet("background-color: white")
        button05.clicked.connect(self.Clicked05)

        self.TxtColor = QLabel("Couleur : ",self)
        self.TxtColor.move(90,250)
        self.TxtColor.setStyleSheet("font: 10pt Arial")
        self.TxtColor.setStyleSheet('color: white; font: 10pt Arial;')
        self.TxtColor.show()
        self.Color = QLabel("None ",self)
        self.Color.move(150,250)
        self.Color.setStyleSheet("font: 10pt Arial")
        self.Color.setStyleSheet('color: white; font: 10pt Arial;')
        self.Color.show()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec_()

