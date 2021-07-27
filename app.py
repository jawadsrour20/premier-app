from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QPixmap, QScreen, QFont
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication, QMainWindow, QLineEdit
import sys
from random import randint
# import printtt
from datetime import date, datetime, time
from pynput.keyboard import Key, Controller
from read_write import *
import copy
import os
import platform
from tabulate import tabulate
import win32api
import win32print
import os
import time
import shutil
import pandas as pd
import win32com.client as win32
keyboard = Controller()

row_num = 1

# portuguese is default
set_language = "PO"

def str_to_float(value):

    if ',' in str(value):
        value_arr = value.split(",")
        result = ""
        for val in value_arr:
            result += val
        return float(result)
    else:
        return float(value)


class Ui_MainWindow(object):

    def __init__(self, transaction):

        self.transaction = transaction

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(604, 622)
        MainWindow.setStyleSheet("background-color: green;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hora = QtWidgets.QLabel(self.centralwidget)
        self.hora.setGeometry(QtCore.QRect(240, 150, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.hora.setFont(font)
        self.hora.setAutoFillBackground(False)
        self.hora.setStyleSheet("background-color:none;")
        self.hora.setText("")
        self.hora.setObjectName("hora")
        self.flot_recebido_label = QtWidgets.QLabel(self.centralwidget)
        self.flot_recebido_label.setGeometry(QtCore.QRect(40, 240, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.flot_recebido_label.setFont(font)
        self.flot_recebido_label.setStyleSheet("background-color:none;")
        self.flot_recebido_label.setAlignment(QtCore.Qt.AlignCenter)
        self.flot_recebido_label.setObjectName("flot_recebido_label")
        self.nome_do_label = QtWidgets.QLabel(self.centralwidget)
        self.nome_do_label.setGeometry(QtCore.QRect(50, 70, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.nome_do_label.setFont(font)
        self.nome_do_label.setStyleSheet("background-color:none;")
        self.nome_do_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_do_label.setObjectName("nome_do_label")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(40, 180, 501, 16))
        self.line_8.setStyleSheet("background-color:none;")
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.nome_do_gerente = QtWidgets.QLabel(self.centralwidget)
        self.nome_do_gerente.setGeometry(QtCore.QRect(240, 60, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.nome_do_gerente.setFont(font)
        self.nome_do_gerente.setAutoFillBackground(False)
        self.nome_do_gerente.setStyleSheet("background-color:none;")
        self.nome_do_gerente.setText("")
        self.nome_do_gerente.setObjectName("nome_do_gerente")
        self.tpa_label = QtWidgets.QLabel(self.centralwidget)
        self.tpa_label.setGeometry(QtCore.QRect(40, 310, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.tpa_label.setFont(font)
        self.tpa_label.setStyleSheet("background-color:none;")
        self.tpa_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tpa_label.setObjectName("tpa_label")
        self.flot_inicial = QtWidgets.QLabel(self.centralwidget)
        self.flot_inicial.setGeometry(QtCore.QRect(240, 200, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.flot_inicial.setFont(font)
        self.flot_inicial.setAutoFillBackground(False)
        self.flot_inicial.setStyleSheet("background-color:none;")
        self.flot_inicial.setText("")
        self.flot_inicial.setObjectName("flot_inicial")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(230, 10, 20, 511))
        self.line_5.setStyleSheet("background-color:none;")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(40, 340, 501, 16))
        self.line_11.setStyleSheet("background-color:none;")
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.data_label = QtWidgets.QLabel(self.centralwidget)
        self.data_label.setGeometry(QtCore.QRect(40, 100, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.data_label.setFont(font)
        self.data_label.setStyleSheet("background-color:none;")
        self.data_label.setAlignment(QtCore.Qt.AlignCenter)
        self.data_label.setObjectName("data_label")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(40, 130, 501, 16))
        self.line_7.setStyleSheet("background-color:none;")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.hora_label = QtWidgets.QLabel(self.centralwidget)
        self.hora_label.setGeometry(QtCore.QRect(40, 150, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.hora_label.setFont(font)
        self.hora_label.setStyleSheet("background-color:none;")
        self.hora_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hora_label.setObjectName("hora_label")
        self.flot_recebido = QtWidgets.QLabel(self.centralwidget)
        self.flot_recebido.setGeometry(QtCore.QRect(240, 240, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.flot_recebido.setFont(font)
        self.flot_recebido.setAutoFillBackground(False)
        self.flot_recebido.setStyleSheet("background-color:none;")
        self.flot_recebido.setText("")
        self.flot_recebido.setObjectName("flot_recebido")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 10, 501, 511))
        self.graphicsView.setStyleSheet("background-color: rgb(224, 252, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.data = QtWidgets.QLabel(self.centralwidget)
        self.data.setGeometry(QtCore.QRect(240, 100, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.data.setFont(font)
        self.data.setAutoFillBackground(False)
        self.data.setStyleSheet("background-color:none;")
        self.data.setText("")
        self.data.setObjectName("data")
        self.confirmar_pagmento = QtWidgets.QPushButton(self.centralwidget)
        self.confirmar_pagmento.setGeometry(QtCore.QRect(40, 530, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.confirmar_pagmento.setFont(font)
        self.confirmar_pagmento.setStyleSheet("background-color: rgb(224, 252, 255);\n"
                                              "font: bold;\n"
                                              "")
        self.confirmar_pagmento.setObjectName("confirmar_pagmento")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(40, 310, 501, 16))
        self.line_10.setStyleSheet("background-color:none;")
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(40, 90, 501, 16))
        self.line_6.setStyleSheet("background-color:none;")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.flot_label = QtWidgets.QLabel(self.centralwidget)
        self.flot_label.setGeometry(QtCore.QRect(40, 200, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.flot_label.setFont(font)
        self.flot_label.setStyleSheet("background-color:none;")
        self.flot_label.setAlignment(QtCore.Qt.AlignCenter)
        self.flot_label.setObjectName("flot_label")
        self.tpa = QtWidgets.QLabel(self.centralwidget)
        self.tpa.setGeometry(QtCore.QRect(240, 320, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tpa.setFont(font)
        self.tpa.setStyleSheet("background-color:none;")
        self.tpa.setText("")
        self.tpa.setObjectName("tpa")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(40, 50, 501, 16))
        self.line_3.setStyleSheet("background-color:none;")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.nome_label = QtWidgets.QLabel(self.centralwidget)
        self.nome_label.setGeometry(QtCore.QRect(40, 20, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.nome_label.setFont(font)
        self.nome_label.setStyleSheet("background-color:none;")
        self.nome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_label.setObjectName("nome_label")
        self.nome_da_loja = QtWidgets.QLabel(self.centralwidget)
        self.nome_da_loja.setGeometry(QtCore.QRect(240, 10, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.nome_da_loja.setFont(font)
        self.nome_da_loja.setAutoFillBackground(False)
        self.nome_da_loja.setStyleSheet("background-color:none;")
        self.nome_da_loja.setText("")
        self.nome_da_loja.setObjectName("nome_da_loja")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(40, 230, 501, 16))
        self.line_12.setStyleSheet("background-color:none;")
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.total_label = QtWidgets.QLabel(self.centralwidget)
        self.total_label.setGeometry(QtCore.QRect(40, 350, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.total_label.setFont(font)
        self.total_label.setStyleSheet("background-color:none;")
        self.total_label.setAlignment(QtCore.Qt.AlignCenter)
        self.total_label.setObjectName("total_label")
        self.total_de_vandos = QtWidgets.QLabel(self.centralwidget)
        self.total_de_vandos.setGeometry(QtCore.QRect(240, 350, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.total_de_vandos.setFont(font)
        self.total_de_vandos.setStyleSheet("background-color:none;\n"
                                           "")
        self.total_de_vandos.setText("")
        self.total_de_vandos.setObjectName("total_de_vandos")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(40, 380, 501, 16))
        self.line_14.setStyleSheet("background-color:none;")
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.total_de_label = QtWidgets.QLabel(self.centralwidget)
        self.total_de_label.setGeometry(QtCore.QRect(40, 390, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.total_de_label.setFont(font)
        self.total_de_label.setStyleSheet("background-color:none;")
        self.total_de_label.setAlignment(QtCore.Qt.AlignCenter)
        self.total_de_label.setObjectName("total_de_label")
        self.valor_label = QtWidgets.QLabel(self.centralwidget)
        self.valor_label.setGeometry(QtCore.QRect(40, 440, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.valor_label.setFont(font)
        self.valor_label.setStyleSheet("background-color:none;")
        self.valor_label.setAlignment(QtCore.Qt.AlignCenter)
        self.valor_label.setObjectName("valor_label")
        self.total_de_pagamentos = QtWidgets.QLabel(self.centralwidget)
        self.total_de_pagamentos.setGeometry(QtCore.QRect(240, 390, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.total_de_pagamentos.setFont(font)
        self.total_de_pagamentos.setStyleSheet("background-color:none;")
        self.total_de_pagamentos.setText("")
        self.total_de_pagamentos.setObjectName("total_de_pagamentos")
        self.valor = QtWidgets.QLabel(self.centralwidget)
        self.valor.setGeometry(QtCore.QRect(240, 440, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.valor.setFont(font)
        self.valor.setStyleSheet("background-color:none;")
        self.valor.setText("")
        self.valor.setObjectName("valor")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(40, 430, 501, 16))
        self.line_15.setStyleSheet("background-color:none;")
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(40, 470, 501, 16))
        self.line_16.setStyleSheet("background-color:none;")
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.balanco_label = QtWidgets.QLabel(self.centralwidget)
        self.balanco_label.setGeometry(QtCore.QRect(40, 480, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.balanco_label.setFont(font)
        self.balanco_label.setStyleSheet("background-color:none;")
        self.balanco_label.setAlignment(QtCore.Qt.AlignCenter)
        self.balanco_label.setObjectName("balanco_label")
        self.balanco = QtWidgets.QLabel(self.centralwidget)
        self.balanco.setGeometry(QtCore.QRect(240, 480, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.balanco.setFont(font)
        self.balanco.setStyleSheet("background-color:none;")
        self.balanco.setText("")
        self.balanco.setObjectName("balanco")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(40, 280, 501, 16))
        self.line_13.setStyleSheet("background-color:none;")
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.flot_recebido_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.flot_recebido_label_2.setGeometry(QtCore.QRect(40, 280, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.flot_recebido_label_2.setFont(font)
        self.flot_recebido_label_2.setStyleSheet("background-color:none;")
        self.flot_recebido_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.flot_recebido_label_2.setObjectName("flot_recebido_label_2")
        self.flot_devolvido = QtWidgets.QLabel(self.centralwidget)
        self.flot_devolvido.setGeometry(QtCore.QRect(240, 290, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.flot_devolvido.setFont(font)
        self.flot_devolvido.setAutoFillBackground(False)
        self.flot_devolvido.setStyleSheet("background-color:none;")
        self.flot_devolvido.setText("")
        self.flot_devolvido.setObjectName("flot_devolvido")
        self.graphicsView.raise_()
        self.hora.raise_()
        self.flot_recebido_label.raise_()
        self.nome_do_label.raise_()
        self.line_8.raise_()
        self.nome_do_gerente.raise_()
        self.tpa_label.raise_()
        self.flot_inicial.raise_()
        self.line_5.raise_()
        self.line_11.raise_()
        self.data_label.raise_()
        self.line_7.raise_()
        self.hora_label.raise_()
        self.flot_recebido.raise_()
        self.data.raise_()
        self.confirmar_pagmento.raise_()
        self.line_10.raise_()
        self.line_6.raise_()
        self.flot_label.raise_()
        self.tpa.raise_()
        self.line_3.raise_()
        self.nome_label.raise_()
        self.nome_da_loja.raise_()
        self.line_12.raise_()
        self.total_label.raise_()
        self.total_de_vandos.raise_()
        self.line_14.raise_()
        self.total_de_label.raise_()
        self.valor_label.raise_()
        self.total_de_pagamentos.raise_()
        self.valor.raise_()
        self.line_15.raise_()
        self.line_16.raise_()
        self.balanco_label.raise_()
        self.balanco.raise_()
        self.line_13.raise_()
        self.flot_recebido_label_2.raise_()
        self.flot_devolvido.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setWindowTitle("Receipt")
        self.confirmar_pagmento.clicked.connect(self.confirm_pagamento)

        self.nome_da_loja.setText(self.transaction["nome_da_loja"])
        self.nome_da_loja.setAlignment(Qt.AlignCenter)
        self.nome_da_loja.setFont(QFont('Arial', 18))

        self.nome_do_gerente.setText(self.transaction["nome_do_gerente"])
        self.nome_do_gerente.setAlignment(Qt.AlignCenter)
        self.nome_do_gerente.setFont(QFont('Arial', 18))

        self.flot_devolvido.setText(self.transaction["flot_devolvido"])
        self.flot_devolvido.setAlignment(Qt.AlignCenter)
        self.flot_devolvido.setFont(QFont('Arial', 18))


        self.data.setText(self.transaction["data"])

        self.data.setAlignment(Qt.AlignCenter)
        self.data.setFont(QFont('Arial', 18))

        self.hora.setText(self.transaction["hora"])

        self.hora.setAlignment(Qt.AlignCenter)
        self.hora.setFont(QFont('Arial', 18))

        self.transaction["flot_inicial"] = str(self.transaction["flot_inicial"])
        self.flot_inicial.setText(self.transaction["flot_inicial"][:len(self.transaction["flot_inicial"]) - 2])
        self.flot_inicial.setAlignment(Qt.AlignCenter)
        self.flot_inicial.setFont(QFont('Arial', 18))

        self.flot_recebido.setText(self.transaction["flot_recebido"])
        self.flot_recebido.setAlignment(Qt.AlignCenter)
        self.flot_recebido.setFont(QFont('Arial', 18))

        self.tpa.setText(self.transaction["tpa"])
        self.tpa.setAlignment(Qt.AlignCenter)
        self.tpa.setFont(QFont('Arial', 18))

        self.total_de_vandos.setText(str(self.transaction["total_de_vendas"]))
        self.total_de_vandos.setAlignment(Qt.AlignCenter)
        self.total_de_vandos.setFont(QFont('Arial', 18))

        self.total_de_pagamentos.setText(str(self.transaction["total_de_pagamentos"]))
        self.total_de_pagamentos.setAlignment(Qt.AlignCenter)
        self.total_de_pagamentos.setFont(QFont('Arial', 18))

        self.valor.setText(str(self.transaction["valor_liquido"]))
        self.valor.setAlignment(Qt.AlignCenter)
        self.valor.setFont(QFont('Arial', 18))

        self.balanco.setText(str(self.transaction["balanco_final"]))
        self.balanco.setAlignment(Qt.AlignCenter)
        self.balanco.setFont(QFont('Arial', 18))

        if set_language == "EN":
            self.nome_label.setText("STORE NAME")
            self.nome_do_label.setText("MANAGER NAME")
            self.data_label.setText("DATE")
            self.hora_label.setText("HOUR")
            self.flot_label.setText("FLOT INITIAL")
            self.flot_recebido_label.setText("RECEIVED FLOT")
            self.total_label.setText("TOTAL SALES")
            self.total_de_label.setText("TOTAL PAYMENTS")
            self.valor_label.setText("NET VALUE")
            self.balanco_label.setText("ENDING BALANCE")
            self.confirmar_pagmento.setText("CONFIRM PAYMENT")
            self.flot_recebido_label_2.setText("FLOT RETURNED")
        elif set_language == "PO":
            self.nome_label.setText("NOME DA LOJA")
            self.nome_do_label.setText("NOME DO GERENTE")
            self.data_label.setText("DATA")
            self.hora_label.setText("HORA")
            self.flot_label.setText("FLOT INICIAL")
            self.flot_recebido_label.setText("FLOT RECEBIDO")
            self.total_label.setText("TOTAL DE VENDAS")
            self.total_de_label.setText("TOTAL DE PAGAMENTOS")
            self.valor_label.setText("VALOR LIQUIDO")
            self.balanco_label.setText("BALANCO FINAL")
            self.confirmar_pagmento.setText("CONFIRMAR PAGMENTO")
            self.flot_recebido_label_2.setText("FLOT DEVOLVIDO")
        elif set_language == "FR":
            self.nome_label.setText("NOM DU MAGASIN")
            self.nome_do_label.setText("NOM DU GERANT")
            self.data_label.setText("DATE")
            self.hora_label.setText("HEURE")
            self.flot_label.setText("FLOT INICIAL")
            self.flot_recebido_label.setText("FLOT RECEBIDO")
            self.total_label.setText("VENTES TOTALES")
            self.total_de_label.setText("PAIEMENTS TOTAUX")
            self.valor_label.setText("VALEUR NETTE")
            self.balanco_label.setText("solde de clôture")
            self.confirmar_pagmento.setText("CONFIRMER LE PAIEMENT")
            self.flot_recebido_label_2.setText("FLOTTEUR RETOURNÉ")






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.flot_recebido_label.setText(_translate("MainWindow", "FLOT RECEBIDO"))
        self.nome_do_label.setText(_translate("MainWindow", "NOME DO GERENTE"))
        self.tpa_label.setText(_translate("MainWindow", "TPA"))
        self.data_label.setText(_translate("MainWindow", "DATA:"))
        self.hora_label.setText(_translate("MainWindow", "HORA:"))
        self.confirmar_pagmento.setText(_translate("MainWindow", "Confirmar Pagmento"))
        self.flot_label.setText(_translate("MainWindow", "FLOT INICIAL"))
        self.nome_label.setText(_translate("MainWindow", "NOME DA LOJA"))
        self.total_label.setText(_translate("MainWindow", "TOTAL DE VENDAS"))
        self.total_de_label.setText(_translate("MainWindow", "TOTAL DE PAGAMENTOS"))
        self.valor_label.setText(_translate("MainWindow", "VALOR LIQUIDO"))
        self.balanco_label.setText(_translate("MainWindow", "BALANCO FINAL"))

    def confirm_pagamento(self):

        msg = QMessageBox()

        if set_language == "PO":
            msg.setWindowTitle("transacao confirmada")
            msg.setText("gostaria de imprimir o recibo?")
        elif set_language == "FR":
            msg.setWindowTitle("transaction confirmée")
            msg.setText("voulez-vous imprimer le reçu?")
        elif set_language == "EN":
            msg.setWindowTitle("confirmed transaction")
            msg.setText("would you like to print the receipt?")

        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)

        msg.buttonClicked.connect(self.print_receipt)
        msg.exec_()

    def print_receipt(self):

        with open("receipt.txt", 'w') as receipt:

            if set_language == "PG":
                receipt.write("+----------------+\n|  Premier Bet   |\n+----------------+\n")
                receipt.write(" Nome Da Loja:   \n " + self.nome_da_loja.text() + "\n")
                receipt.write("+----------------+\n")
                receipt.write(" Nome Do Gerente:\n " + self.nome_do_gerente.text()+ "\n")
                receipt.write("+----------------+\n")
                receipt.write(" DATA:  " + self.data.text()+ "\n")
                receipt.write("+----------------+\n")
                receipt.write(" HORA:   " + self.hora.text()+ "\n")
                receipt.write("+----------------+\n")
                receipt.write(" FLOT INICIAL:\n " + self.flot_inicial.text()+ "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" FLOT RECEBIDO:\n " + self.flot_recebido.text()+ "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" FLOT DEVOLVIDO:\n " + self.flot_devolvido.text() + "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" TPA:\n " + self.tpa.text()+ "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" TOTAL DE VENDAS:\n " + self.total_de_vandos.text()+ "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" TOTAL PAGAMENTOS:\n " + self.total_de_pagamentos.text()+ "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" VALOR LIQUIDO:\n " + self.valor.text()+ "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" BALANCO FINAL:\n " + self.balanco.text()+ "KZ\n")
                receipt.write("+----------------+\n   THANK YOU\n")
            elif set_language == "FR":
                receipt.write("+----------------+\n|  Premier Bet   |\n+----------------+\n")
                receipt.write(" Nome Du Magasin: \n " + self.nome_da_loja.text() + "\n")
                receipt.write("+----------------+\n")
                receipt.write(" NOM DU GESTIONNAIRE:\n " + self.nome_do_gerente.text() + "\n")
                receipt.write("+----------------+\n")
                receipt.write(" DATe:  " + self.data.text() + "\n")
                receipt.write("+----------------+\n")
                receipt.write(" HEURE:   " + self.hora.text() + "\n")
                receipt.write("+----------------+\n")
                receipt.write(" FLOT INITIAL:\n " + self.flot_inicial.text() + "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" FLOT REÇU:\n " + self.flot_recebido.text() + "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" FLOTTEUR RETOURNÉ:\n " + self.flot_devolvido.text() + "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" TPA:\n " + self.tpa.text() + "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" VENTES TOTALES:\n " + self.total_de_vandos.text() + "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" TOTAL DES PAIEMENTS:\n " + self.total_de_pagamentos.text() + "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" VALEUR NETTE:\n " + self.valor.text() + "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" SOLDE DE CLÔTURE:\n " + self.balanco.text() + "KZ\n")
                receipt.write("+----------------+\n   THANK YOU\n")
            elif set_language == "EN":
                receipt.write("+----------------+\n|  Premier Bet   |\n+----------------+\n")
                receipt.write(" Store Name:   \n " + self.nome_da_loja.text() + "\n")
                receipt.write("+----------------+\n")
                receipt.write(" Manager Name:\n " + self.nome_do_gerente.text() + "\n")
                receipt.write("+----------------+\n")
                receipt.write(" DATE:  " + self.data.text() + "\n")
                receipt.write("+----------------+\n")
                receipt.write(" HOUR:   " + self.hora.text() + "\n")
                receipt.write("+----------------+\n")
                receipt.write(" FLOT INITIAL:\n " + self.flot_inicial.text() + "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" FLOT RECEIVED:\n " + self.flot_recebido.text() + "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" FLOT RETURNED:\n " + self.flot_devolvido.text() + "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" TPA:\n " + self.tpa.text() + "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" TOTAL SALES:\n " + self.total_de_vandos.text() + "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" TOTAL PAYMENTS:\n " + self.total_de_pagamentos.text() + "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" NET VALUE:\n " + self.valor.text() + "KZ\n")
                receipt.write("+----------------+\n")
                receipt.write(" FINAL BALANCE:\n " + self.balanco.text() + "KZ\n")
                receipt.write("+----------------+\n   THANK YOU\n")


        try:
            # printing on Windows
            if platform.system() == "Windows":
                defaultPrinter = win32print.GetDefaultPrinter()
                printer_name = "EPSON TM-T20III Receipt"
                if defaultPrinter != printer_name:
                    win32print.SetDefaultPrinter(printer_name)
                p = win32print.OpenPrinter(printer_name)
                job = win32print.StartDocPrinter(p, 1, ("test of raw data", None, "RAW"))
                win32print.StartPagePrinter(p)
                with open(r"receipt.txt") as receipt_print:
                    win32print.WritePrinter(p, receipt_print.read())
                    win32print.EndPagePrinter(p)
            else:
                # printing on Mac or Linux
                os.system("lpr -P EPSON TM-T20III Receipt receipt.txt")


        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            if set_language == "PO":
                msg.setText("Erro da impressora. Certifique-se de que a impressora esteja conectada!")
            elif set_language == "FR":
                msg.setText("Erreur d'imprimante. Assurez-vous que l'imprimante est connectée !")
            else:
                msg.setText("Printer error. Make sure the printer is connected!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()


# add french

class Ui_transaction_report(QMainWindow):

    global set_language
    def __init__(self, store):

        super().__init__()

        self.gerente = store["gerente_da_loja"]
        self.nome = store["nome_da_loja"]
        self.fflot_inicial= store["Flot Inicial"]
        self.vvenda_sb = store["Vendas SB"]
        self.ppagamento_sb = store["Pagamentos SB"]
        self.vvendas_solidicon = store["Vendas Solidicon"]
        self.ppagamentos_solidicon = store["Pagementos Solidicon"]
        self.vvendas_gb = store["Vendas GB"]
        self.ppagamentos_gb = store["Pagamento GB"]
        self.ppagamentos_ts7 = store["Pagamento TS7"]
        self.vvendas_ts7 = store["Vendas TS7"]
        self.ttotal = store["total"]

    def setupUi(self, transaction_report):
        transaction_report.setObjectName("transaction_report")
        transaction_report.resize(1186, 761)
        font = QtGui.QFont()
        font.setPointSize(9)
        transaction_report.setFont(font)
        transaction_report.setStyleSheet("background-color: rgb(0, 128, 0);")
        self.centralwidget = QtWidgets.QWidget(transaction_report)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 350, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: none;")
        self.label_4.setObjectName("label_4")
        self.venda_sb = QtWidgets.QLabel(self.centralwidget)
        self.venda_sb.setGeometry(QtCore.QRect(230, 350, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.venda_sb.setFont(font)
        self.venda_sb.setAutoFillBackground(False)
        self.venda_sb.setStyleSheet("background-color: none;\n"
                                    "")
        self.venda_sb.setAlignment(QtCore.Qt.AlignCenter)
        self.venda_sb.setObjectName("venda_sb")
        self.pagamento_sb = QtWidgets.QLabel(self.centralwidget)
        self.pagamento_sb.setGeometry(QtCore.QRect(230, 390, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pagamento_sb.setFont(font)
        self.pagamento_sb.setAutoFillBackground(False)
        self.pagamento_sb.setStyleSheet("background-color: none;")
        self.pagamento_sb.setAlignment(QtCore.Qt.AlignCenter)
        self.pagamento_sb.setObjectName("pagamento_sb")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 390, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: none;\n"
                                   "")
        self.label_6.setObjectName("label_6")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 300, 391, 401))
        self.graphicsView.setStyleSheet("background-color: rgb(229, 255, 255);\n"
                                        "")
        self.graphicsView.setObjectName("graphicsView")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 470, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: none;")
        self.label_7.setObjectName("label_7")
        self.vendas_solidicon = QtWidgets.QLabel(self.centralwidget)
        self.vendas_solidicon.setGeometry(QtCore.QRect(230, 430, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.vendas_solidicon.setFont(font)
        self.vendas_solidicon.setAutoFillBackground(False)
        self.vendas_solidicon.setStyleSheet("background-color: none;")
        self.vendas_solidicon.setAlignment(QtCore.Qt.AlignCenter)
        self.vendas_solidicon.setObjectName("vendas_solidicon")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 430, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: none;")
        self.label_8.setObjectName("label_8")
        self.pagamentos_solidicon = QtWidgets.QLabel(self.centralwidget)
        self.pagamentos_solidicon.setGeometry(QtCore.QRect(230, 470, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pagamentos_solidicon.setFont(font)
        self.pagamentos_solidicon.setAutoFillBackground(False)
        self.pagamentos_solidicon.setStyleSheet("background-color: none;")
        self.pagamentos_solidicon.setAlignment(QtCore.Qt.AlignCenter)
        self.pagamentos_solidicon.setObjectName("pagamentos_solidicon")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 550, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: none;")
        self.label_9.setObjectName("label_9")
        self.vendas_gb = QtWidgets.QLabel(self.centralwidget)
        self.vendas_gb.setGeometry(QtCore.QRect(230, 510, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.vendas_gb.setFont(font)
        self.vendas_gb.setAutoFillBackground(False)
        self.vendas_gb.setStyleSheet("background-color: none;")
        self.vendas_gb.setAlignment(QtCore.Qt.AlignCenter)
        self.vendas_gb.setObjectName("vendas_gb")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 510, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: none;")
        self.label_10.setObjectName("label_10")
        self.pagamentos_gb = QtWidgets.QLabel(self.centralwidget)
        self.pagamentos_gb.setGeometry(QtCore.QRect(230, 550, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pagamentos_gb.setFont(font)
        self.pagamentos_gb.setAutoFillBackground(False)
        self.pagamentos_gb.setStyleSheet("background-color: none;")
        self.pagamentos_gb.setAlignment(QtCore.Qt.AlignCenter)
        self.pagamentos_gb.setObjectName("pagamentos_gb")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(220, 300, 20, 361))
        self.line_5.setStyleSheet("background-color: none;\n"
                                  "color: black;")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(40, 340, 391, 16))
        self.line_6.setStyleSheet("background-color: none;")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(40, 380, 391, 16))
        self.line_7.setStyleSheet("background-color: none;")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(40, 420, 391, 16))
        self.line_8.setStyleSheet("background-color: none;")
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(40, 460, 391, 16))
        self.line_9.setStyleSheet("background-color: none;")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(40, 500, 391, 16))
        self.line_10.setStyleSheet("background-color: none;")
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(40, 540, 391, 16))
        self.line_11.setStyleSheet("background-color: none;")
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(60, 310, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: none;")
        self.label_15.setObjectName("label_15")
        self.flot_inicial = QtWidgets.QLabel(self.centralwidget)
        self.flot_inicial.setGeometry(QtCore.QRect(230, 300, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.flot_inicial.setFont(font)
        self.flot_inicial.setStyleSheet("background-color: none;")
        self.flot_inicial.setAlignment(QtCore.Qt.AlignCenter)
        self.flot_inicial.setObjectName("flot_inicial")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(790, 80, 371, 561))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.fiveButton = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fiveButton.sizePolicy().hasHeightForWidth())
        self.fiveButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.fiveButton.setFont(font)
        self.fiveButton.setStyleSheet("background-color: rgb(229, 255, 255);")
        self.fiveButton.setObjectName("fiveButton")
        self.gridLayout.addWidget(self.fiveButton, 2, 2, 1, 1)
        self.nineButton = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nineButton.sizePolicy().hasHeightForWidth())
        self.nineButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.nineButton.setFont(font)
        self.nineButton.setStyleSheet("background-color: rgb(229, 255, 255);")
        self.nineButton.setObjectName("nineButton")
        self.gridLayout.addWidget(self.nineButton, 1, 3, 1, 1)
        self.sixButton = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sixButton.sizePolicy().hasHeightForWidth())
        self.sixButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.sixButton.setFont(font)
        self.sixButton.setStyleSheet("background-color: rgb(229, 255, 255);")
        self.sixButton.setObjectName("sixButton")
        self.gridLayout.addWidget(self.sixButton, 2, 3, 1, 1)
        self.clearButton = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet("background-color: rgb(229, 255, 255);")
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 0, 2, 1, 2)
        self.backspaceButton = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backspaceButton.sizePolicy().hasHeightForWidth())
        self.backspaceButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.backspaceButton.setFont(font)
        self.backspaceButton.setStyleSheet("background-color: rgb(229, 255, 255);")
        self.backspaceButton.setObjectName("backspaceButton")
        self.gridLayout.addWidget(self.backspaceButton, 0, 1, 1, 1)
        self.sevenButton = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sevenButton.sizePolicy().hasHeightForWidth())
        self.sevenButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.sevenButton.setFont(font)
        self.sevenButton.setStyleSheet("background-color: rgb(229, 255, 255);")
        self.sevenButton.setObjectName("sevenButton")
        self.gridLayout.addWidget(self.sevenButton, 1, 1, 1, 1)
        self.threeButton = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threeButton.sizePolicy().hasHeightForWidth())
        self.threeButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.threeButton.setFont(font)
        self.threeButton.setStyleSheet("background-color: rgb(229, 255, 255);")
        self.threeButton.setObjectName("threeButton")
        self.gridLayout.addWidget(self.threeButton, 3, 3, 1, 1)
        self.fourButton = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fourButton.sizePolicy().hasHeightForWidth())
        self.fourButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.fourButton.setFont(font)
        self.fourButton.setStyleSheet("background-color: rgb(229, 255, 255);")
        self.fourButton.setObjectName("fourButton")
        self.gridLayout.addWidget(self.fourButton, 2, 1, 1, 1)
        self.eightButton = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eightButton.sizePolicy().hasHeightForWidth())
        self.eightButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.eightButton.setFont(font)
        self.eightButton.setStyleSheet("background-color: rgb(229, 255, 255);")
        self.eightButton.setObjectName("eightButton")
        self.gridLayout.addWidget(self.eightButton, 1, 2, 1, 1)
        self.twoButton = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twoButton.sizePolicy().hasHeightForWidth())
        self.twoButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.twoButton.setFont(font)
        self.twoButton.setStyleSheet("background-color: rgb(229, 255, 255);")
        self.twoButton.setObjectName("twoButton")
        self.gridLayout.addWidget(self.twoButton, 3, 2, 1, 1)
        self.oneButton = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oneButton.sizePolicy().hasHeightForWidth())
        self.oneButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.oneButton.setFont(font)
        self.oneButton.setStyleSheet("background-color: rgb(229, 255, 255);")
        self.oneButton.setObjectName("oneButton")
        self.gridLayout.addWidget(self.oneButton, 3, 1, 1, 1)
        self.zeroButton = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zeroButton.sizePolicy().hasHeightForWidth())
        self.zeroButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.zeroButton.setFont(font)
        self.zeroButton.setStyleSheet("background-color: rgb(229, 255, 255);")
        self.zeroButton.setObjectName("zeroButton")
        self.gridLayout.addWidget(self.zeroButton, 4, 1, 1, 3)
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(750, 60, 21, 621))
        self.line_12.setStyleSheet("background-color: none;\n"
                                   "")
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(40, 580, 391, 16))
        self.line_13.setStyleSheet("background-color: none;")
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(60, 600, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: none;")
        self.label_12.setObjectName("label_12")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(40, 620, 391, 16))
        self.line_14.setStyleSheet("background-color: none;")
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(60, 640, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: none;")
        self.label_13.setObjectName("label_13")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(40, 660, 391, 16))
        self.line_15.setStyleSheet("background-color: none;")
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.vendas_ts7 = QtWidgets.QLabel(self.centralwidget)
        self.vendas_ts7.setGeometry(QtCore.QRect(230, 590, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.vendas_ts7.setFont(font)
        self.vendas_ts7.setAutoFillBackground(False)
        self.vendas_ts7.setStyleSheet("background-color: none;")
        self.vendas_ts7.setAlignment(QtCore.Qt.AlignCenter)
        self.vendas_ts7.setObjectName("vendas_ts7")
        self.pagamentos_ts7 = QtWidgets.QLabel(self.centralwidget)
        self.pagamentos_ts7.setGeometry(QtCore.QRect(230, 630, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pagamentos_ts7.setFont(font)
        self.pagamentos_ts7.setAutoFillBackground(False)
        self.pagamentos_ts7.setStyleSheet("background-color: none;")
        self.pagamentos_ts7.setAlignment(QtCore.Qt.AlignCenter)
        self.pagamentos_ts7.setObjectName("pagamentos_ts7")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(60, 669, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: none;")
        self.label_14.setObjectName("label_14")
        self.total = QtWidgets.QLabel(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(230, 670, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.total.setFont(font)
        self.total.setAutoFillBackground(False)
        self.total.setStyleSheet("background-color: none;")
        self.total.setAlignment(QtCore.Qt.AlignCenter)
        self.total.setObjectName("total")
        self.detalhes = QtWidgets.QLabel(self.centralwidget)
        self.detalhes.setGeometry(QtCore.QRect(40, 260, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.detalhes.setFont(font)
        self.detalhes.setStyleSheet("background-color: #696969;\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font: bold;")
        self.detalhes.setAlignment(QtCore.Qt.AlignCenter)
        self.detalhes.setObjectName("detalhes")
        self.confirmar = QtWidgets.QPushButton(self.centralwidget)
        self.confirmar.setGeometry(QtCore.QRect(540, 490, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.confirmar.setFont(font)
        self.confirmar.setStyleSheet("color: white;\n"
                                     "font: bold;\n"
                                     "background-color: #696969;")
        self.confirmar.setObjectName("confirmar")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)




        self.flot_field = QtWidgets.QSpinBox(self.centralwidget)
        self.flot_field.setGeometry(QtCore.QRect(570, 180, 151, 31))
        self.flot_field.setStyleSheet("background-color: rgb(229, 255, 255);\n"
                                      "")
        self.flot_field.setObjectName("flot_field")
        self.tpa_field = QtWidgets.QSpinBox(self.centralwidget)
        self.tpa_field.setGeometry(QtCore.QRect(570, 240, 151, 31))
        self.tpa_field.setStyleSheet("background-color: rgb(229, 255, 255);\n"
                                     "")
        self.tpa_field.setObjectName("tpa_field")

        self.flot_devolvido = QtWidgets.QSpinBox(self.centralwidget)
        self.flot_devolvido.setGeometry(QtCore.QRect(570, 140, 151, 31))
        self.flot_devolvido.setStyleSheet("background-color: rgb(229, 255, 255);\n"
                                          "")
        self.flot_devolvido.setObjectName("flot_devolvido")
        self.flot_devolvido_label = QtWidgets.QLabel(self.centralwidget)
        self.flot_devolvido_label.setGeometry(QtCore.QRect(480, 140, 81, 31))
        self.flot_devolvido_label.setStyleSheet("color: rgb(229, 255, 255);\n"
                                                "font:bold;")
        self.flot_devolvido_label.setObjectName("flot_devolvido_label")

        self.flot_label = QtWidgets.QLabel(self.centralwidget)
        self.flot_label.setGeometry(QtCore.QRect(480, 180, 71, 31))
        self.flot_label.setStyleSheet("color: rgb(229, 255, 255);\n"
                                      "font:bold;")
        self.flot_label.setObjectName("flot_label")
        self.tpa_label = QtWidgets.QLabel(self.centralwidget)
        self.tpa_label.setGeometry(QtCore.QRect(520, 240, 41, 31))
        self.tpa_label.setStyleSheet("color: rgb(229, 255, 255);\n"
                                     "font:bold;")
        self.tpa_label.setObjectName("tpa_label")
        self.nome_da_loja_label = QtWidgets.QLabel(self.centralwidget)
        self.nome_da_loja_label.setGeometry(QtCore.QRect(40, 110, 101, 21))
        self.nome_da_loja_label.setStyleSheet("color: rgb(229, 255, 255);\n"
                                              "font:bold;")
        self.nome_da_loja_label.setObjectName("nome_da_loja_label")
        self.gerente_text_field = QtWidgets.QTextEdit(self.centralwidget)
        self.gerente_text_field.setGeometry(QtCore.QRect(40, 210, 221, 31))
        self.gerente_text_field.setStyleSheet("background-color: rgb(229, 255, 255);\n"
                                              "")
        self.gerente_text_field.setObjectName("gerente_text_field")
        self.gerente_da_loja_label = QtWidgets.QLabel(self.centralwidget)
        self.gerente_da_loja_label.setGeometry(QtCore.QRect(40, 180, 141, 21))
        self.gerente_da_loja_label.setStyleSheet("color: rgb(229, 255, 255);\n"
                                                 "font:bold;")
        self.flot_field.setMaximum(999999999)
        self.tpa_field.setMaximum(999999999)
        self.gerente_da_loja_label.setObjectName("gerente_da_loja_label")
        self.date_field = QtWidgets.QDateEdit(self.centralwidget)
        self.date_field.setGeometry(QtCore.QRect(40, 70, 181, 31))
        self.date_field.setStyleSheet("background-color: rgb(229, 255, 255);\n"
                                      "border-radius: 0px;")
        self.date_field.setAlignment(QtCore.Qt.AlignCenter)
        self.date_field.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 4, 14), QtCore.QTime(0, 0, 0)))
        self.date_field.setCalendarPopup(True)
        self.date_field.setObjectName("date_field")
        self.nome_field = QtWidgets.QTextEdit(self.centralwidget)
        self.nome_field.setGeometry(QtCore.QRect(40, 140, 221, 31))
        self.nome_field.setStyleSheet("background-color: rgb(229, 255, 255);\n"
                                      "")
        self.nome_field.setObjectName("nome_field")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 211, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("premier-bet-logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")


        self.english_radiobtn = QtWidgets.QRadioButton(self.centralwidget)
        self.english_radiobtn.setGeometry(QtCore.QRect(920, 700, 99, 20))
        self.english_radiobtn.setStyleSheet("color:white;")
        self.english_radiobtn.setObjectName("english_radiobtn")
        self.french_radiobtn = QtWidgets.QRadioButton(self.centralwidget)
        self.french_radiobtn.setGeometry(QtCore.QRect(800, 700, 99, 20))
        self.french_radiobtn.setStyleSheet("color:white;")
        self.french_radiobtn.setObjectName("french_radiobtn")
        self.portuguese_radiobtn = QtWidgets.QRadioButton(self.centralwidget)
        self.portuguese_radiobtn.setGeometry(QtCore.QRect(1050, 700, 99, 20))
        self.portuguese_radiobtn.setStyleSheet("color:white;")
        self.portuguese_radiobtn.setChecked(True)
        self.portuguese_radiobtn.setObjectName("portuguese_radiobtn")



        self.graphicsView.raise_()
        self.label_4.raise_()
        self.venda_sb.raise_()
        self.pagamento_sb.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.vendas_solidicon.raise_()
        self.label_8.raise_()
        self.pagamentos_solidicon.raise_()
        self.label_9.raise_()
        self.vendas_gb.raise_()
        self.label_10.raise_()
        self.pagamentos_gb.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.line_8.raise_()
        self.line_9.raise_()
        self.line_10.raise_()
        self.line_11.raise_()
        self.label_15.raise_()
        self.flot_inicial.raise_()
        self.layoutWidget.raise_()
        self.line_12.raise_()
        self.line_13.raise_()
        self.label_12.raise_()
        self.line_14.raise_()
        self.label_13.raise_()
        self.line_15.raise_()
        self.vendas_ts7.raise_()
        self.pagamentos_ts7.raise_()
        self.label_14.raise_()
        self.total.raise_()
        self.detalhes.raise_()
        self.confirmar.raise_()
        self.english_radiobtn.raise_()
        self.portuguese_radiobtn.raise_()
        self.french_radiobtn.raise_()
        self.flot_devolvido.raise_()
        self.flot_devolvido_label.raise_()
        self.flot_field.raise_()
        self.tpa_field.raise_()
        self.flot_label.raise_()
        self.tpa_label.raise_()
        self.nome_da_loja_label.raise_()
        self.gerente_text_field.raise_()
        self.gerente_da_loja_label.raise_()
        self.date_field.raise_()
        self.nome_field.raise_()
        self.label.raise_()
        transaction_report.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(transaction_report)
        self.statusbar.setObjectName("statusbar")
        transaction_report.setStatusBar(self.statusbar)

        self.retranslateUi(transaction_report)
        QtCore.QMetaObject.connectSlotsByName(transaction_report)

        transaction_report.setWindowTitle("Transactions Report")

        self.zeroButton.clicked.connect(self.zero)
        self.oneButton.clicked.connect(self.one)
        self.twoButton.clicked.connect(self.two)
        self.threeButton.clicked.connect(self.three)
        self.fourButton.clicked.connect(self.four)
        self.fiveButton.clicked.connect(self.five)
        self.sixButton.clicked.connect(self.six)
        self.sevenButton.clicked.connect(self.seven)
        self.eightButton.clicked.connect(self.eight)
        self.nineButton.clicked.connect(self.nine)
        self.backspaceButton.clicked.connect(self.backspace)
        self.clearButton.clicked.connect(self.clear)
        self.confirmar.clicked.connect(self.confirm)

        self.flot_inicial.setText(self.fflot_inicial)
        self.venda_sb.setText(self.vvenda_sb)
        self.pagamento_sb.setText(self.ppagamento_sb)
        self.vendas_solidicon.setText(self.vvendas_solidicon)
        self.pagamentos_solidicon.setText(self.ppagamentos_solidicon)
        self.vendas_gb.setText(self.vvendas_gb)
        self.pagamentos_gb.setText(self.ppagamentos_gb)
        self.vendas_ts7.setText(self.vvendas_ts7)
        self.pagamentos_ts7.setText(self.ppagamentos_ts7)
        self.total.setText(self.ttotal)




        self.english_radiobtn.toggled.connect(lambda: self.btnstate(self.english_radiobtn))
        self.portuguese_radiobtn.toggled.connect(lambda: self.btnstate(self.portuguese_radiobtn))
        self.french_radiobtn.toggled.connect(lambda: self.btnstate(self.french_radiobtn))

        # self.flot_field.editingFinished.connect(self.format_field("flot"))
        # self.tpa_field.editingFinished.connect(self.format_field("tpa"))

    def retranslateUi(self, transaction_report):
        _translate = QtCore.QCoreApplication.translate
        transaction_report.setWindowTitle(_translate("transaction_report", "MainWindow"))
        self.label_4.setText(_translate("transaction_report", "VENDAS SB"))
        self.venda_sb.setText(_translate("transaction_report", "0.000.000KZ"))
        self.pagamento_sb.setText(_translate("transaction_report", "0.000.000KZ"))
        self.label_6.setText(_translate("transaction_report", "PAGAMENTO SB"))
        self.label_7.setText(_translate("transaction_report", "PAGAMENTOS SOLIDICON"))
        self.vendas_solidicon.setText(_translate("transaction_report", "0.000.000KZ"))
        self.label_8.setText(_translate("transaction_report", "VENDAS SOLIDICON"))
        self.pagamentos_solidicon.setText(_translate("transaction_report", "0.000.000KZ"))
        self.label_9.setText(_translate("transaction_report", "PAGAMENTOS GB"))
        self.vendas_gb.setText(_translate("transaction_report", "0.000.000KZ"))
        self.label_10.setText(_translate("transaction_report", "VENDAS GB"))
        self.pagamentos_gb.setText(_translate("transaction_report", "0.000.000KZ"))
        self.label_15.setText(_translate("transaction_report", "FLOT INICIAL"))
        self.flot_inicial.setText(_translate("transaction_report", "0.000.000KZ"))
        self.fiveButton.setText(_translate("transaction_report", "5"))
        self.nineButton.setText(_translate("transaction_report", "9"))
        self.sixButton.setText(_translate("transaction_report", "6"))
        self.clearButton.setText(_translate("transaction_report", "APAGAR"))
        self.backspaceButton.setText(_translate("transaction_report", "Backspace"))
        self.sevenButton.setText(_translate("transaction_report", "7"))
        self.threeButton.setText(_translate("transaction_report", "3"))
        self.fourButton.setText(_translate("transaction_report", "4"))
        self.eightButton.setText(_translate("transaction_report", "8"))
        self.twoButton.setText(_translate("transaction_report", "2"))
        self.oneButton.setText(_translate("transaction_report", "1"))
        self.zeroButton.setText(_translate("transaction_report", "0"))
        self.label_12.setText(_translate("transaction_report", "VENDAS TS7"))
        self.label_13.setText(_translate("transaction_report", "PAGAMENTOS TS7"))
        self.vendas_ts7.setText(_translate("transaction_report", "0.000.000KZ"))
        self.pagamentos_ts7.setText(_translate("transaction_report", "0.000.000KZ"))
        self.label_14.setText(_translate("transaction_report", "TOTAL"))
        self.total.setText(_translate("transaction_report", "0.000.000KZ"))
        self.detalhes.setText(_translate("transaction_report", "DETALHES DA TRANSAÇÃO"))
        self.confirmar.setText(_translate("transaction_report", "CONFIRMAR"))
        self.english_radiobtn.setText(_translate("transaction_report", "English"))
        self.portuguese_radiobtn.setText(_translate("transaction_report", "Portuguese"))
        self.french_radiobtn.setText(_translate("transaction_report", "French"))
        self.flot_devolvido_label.setText(_translate("transaction_report", " FLOT\n"
                                                                           " DEVOLVIDO"))


        self.flot_label.setText(_translate("transaction_report", " FLOT\nRECEBIDO"))
        self.tpa_label.setText(_translate("transaction_report", "TPA"))
        self.nome_da_loja_label.setText(_translate("transaction_report", "NOME DA LOJA"))
        self.gerente_text_field.setHtml(_translate("transaction_report",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.gerente_da_loja_label.setText(_translate("transaction_report", "GERENTE DA LOJA"))
        self.date_field.setDisplayFormat(_translate("transaction_report", "M/d/yyyy"))
        self.nome_field.setHtml(_translate("transaction_report",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))

        self.nome_field.setDisabled(True)
        self.gerente_text_field.setDisabled(True)

        self.nome_field.setText(self.nome)
        self.gerente_text_field.setText(self.gerente)
        today = date.today()
        self.date_field.setDate(QDate(today.year, today.month, today.day))

    # function factory --> AKA closure or wrapper-function
    # def format_field(self, src):
    #
    #     def formatter():
    #         if src == "flot":
    #
    #             self.flot_field.setValue(int("{:,}".format(int(str_to_float(self.flot_field.text())))))
    #         elif src == "tpa":
    #             self.tpa_field.setValue(int("{:,}".format(int(str_to_float(self.tpa_field.text())))))
    #     return formatter

    def btnstate(self, btn):

        global set_language

        if btn.text() == "English" and btn.isChecked():
            set_language = "EN"
            self.label_15.setText("INITIAL FLOT")
            self.label_4.setText("SALES SB")
            self.label_6.setText("PAYMENTS SB")
            self.label_8.setText("SOLIDICON SALES")
            self.label_7.setText("PAYMENTS SOLIDICON")
            self.label_10.setText("SALES GB")
            self.label_9.setText("PAYMENTS GB")
            self.label_12.setText("SALES TS7")
            self.label_13.setText("PAYMENTS TS7")
            self.clearButton.setText("CLEAR")
            self.nome_da_loja_label.setText("STORE NAME")
            self.gerente_da_loja_label.setText("STORE MANAGER")
            self.detalhes.setText("TRANSACTION DETAILS")
            self.confirmar.setText("CONFIRM")
            self.flot_devolvido_label.setText(" FLOT\n RETURNED")
            self.flot_label.setText(" FLOT\n RECEIVED")


        elif btn.text() == "Portuguese" and btn.isChecked():
            set_language = "PO"
            self.label_15.setText("FLOT INICIAL")
            self.label_4.setText("VENDAS SB")
            self.label_6.setText("PAGAMENTOS SB")
            self.label_8.setText("VENDAS SOLIDICON")
            self.label_7.setText("PAGAMENTOS SOLIDICON")
            self.label_10.setText("VENDAS GB")
            self.label_9.setText("PAGAMENTOS GB")
            self.label_12.setText("VENDAS TS7")
            self.label_13.setText("PAGAMENTOS TS7")
            self.clearButton.setText("APAGAR")
            self.nome_da_loja_label.setText("NOME DA LOJA")
            self.gerente_da_loja_label.setText("GERENTE DA LOJA")
            self.detalhes.setText("DETALHES DA TRANSAÇÃO")
            self.confirmar.setText("CONFIRMAR")
            self.flot_devolvido_label.setText(" FLOT\n DEVOLVIDO")
            self.flot_label.setText(" FLOT\n RECEBIDO")

        elif btn.text() == "French" and btn.isChecked():
            set_language = "FR"
            self.label_15.setText("FLOT INITIAL")
            self.label_4.setText("VENTES SB")
            self.label_6.setText("Paiements SB")
            self.label_8.setText("Ventes SOLIDICON")
            self.label_7.setText("Paiements SOLIDICON")
            self.label_10.setText("Ventes GB")
            self.label_9.setText("Paiements GB")
            self.label_12.setText("Ventes TS7")
            self.label_13.setText("Paiements TS7")
            self.clearButton.setText("ÉTEINDRE")
            self.nome_da_loja_label.setText("NOM MAGASIN")
            self.gerente_da_loja_label.setText("GÉRANT DE MAGASIN")
            self.detalhes.setText("DÉTAILS DE LA TRANSACTION")
            self.confirmar.setText("CONFIRMER")
            self.flot_devolvido_label.setText(" FLOT\n RETOURNÉ")
            self.flot_label.setText(" FLOT\n REÇU")

    def confirm(self):

        global row_num

        if str_to_float(self.flot_field.text()) == float(0) or str_to_float(self.tpa_field.text()) == float(0) \
                or str_to_float(self.flot_devolvido.text() == float(0)):

            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            if set_language == "PO":
                msg.setText("Os valores de entrada devem ser maiores que zero!")
            elif set_language == "FR":
                msg.setText("Les valeurs d'entrée doivent être supérieures à zéro!")
            else:
                msg.setText("Input values should be greater than zero!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

        else:

            total_vendas = str_to_float(str(self.vendas_ts7.text())[:len(str(self.vendas_ts7.text())) - 2]) \
                           + str_to_float(str(self.vendas_gb.text())[:len(str(self.vendas_gb.text())) - 2]) \
                           + str_to_float(str(self.venda_sb.text())[:len(str(self.venda_sb.text())) - 2]) \
                           + str_to_float(str(self.vendas_solidicon.text())[:len(str(self.vendas_solidicon.text())) - 2])

            total_pagamentos = str_to_float(self.pagamentos_ts7.text()[:len(self.pagamentos_ts7.text()) - 2]) \
                               + str_to_float(self.pagamentos_gb.text()[:len(self.pagamentos_gb.text()) - 2]) \
                               + str_to_float(self.pagamento_sb.text()[:len(self.pagamento_sb.text()) - 2]) \
                               + str_to_float(
                self.pagamentos_solidicon.text()[:len(self.pagamentos_solidicon.text()) - 2])
            valor_liquido = float(self.flot_field.value()) \
                            + str_to_float(self.flot_inicial.text()[:len(self.flot_inicial.text()) - 2]) \
                            + total_vendas - total_pagamentos
            balanco_final = float(valor_liquido) + float(self.tpa_field.value())

            temp_date = self.date_field.dateTime().toPyDateTime()
            temp_flot_inicial = str_to_float(self.flot_inicial.text()[:len(self.flot_inicial.text()) - 2])
            temp_flot_inicial = temp_flot_inicial +  float(self.flot_field.value()) - float(self.flot_devolvido.value())
            premier.update(f'B{row_num + 1}:R{row_num + 1}', [
                [
                 f"{temp_date.month}/{temp_date.day}/{temp_date.year}",
                 str(temp_flot_inicial),
                 self.venda_sb.text()[:len(self.venda_sb.text()) - 2],
                 self.pagamento_sb.text()[:len(self.pagamento_sb.text()) - 2],
                 self.vendas_solidicon.text()[:len(self.vendas_solidicon.text()) - 2],
                 self.pagamentos_solidicon.text()[:len(self.pagamentos_solidicon.text()) - 2],
                 self.vendas_gb.text()[:len(self.vendas_gb.text()) - 2],
                 self.pagamentos_gb.text()[:len(self.pagamentos_gb.text()) - 2],
                 self.vendas_ts7.text()[:len(self.vendas_ts7.text()) - 2],
                 self.pagamentos_ts7.text()[:len(self.pagamentos_ts7.text()) - 2],
                 self.flot_field.value(),
                 self.flot_devolvido.text()[:len(self.flot_devolvido.text()) - 2],
                 self.tpa_field.value(),
                 total_vendas, total_pagamentos, valor_liquido, balanco_final]
            ])

            transaction = {"nome_da_loja": self.nome_field.toPlainText(),
                           "nome_do_gerente": self.gerente_text_field.toPlainText(),
                           "data": f"{temp_date.month}/{temp_date.day}/{temp_date.year}",
                           "hora": datetime.now().strftime("%H:%M:%S"),
                           "flot_inicial": temp_flot_inicial, "flot_recebido": self.flot_field.text(),
                           "flot_devolvido": self.flot_devolvido.text(),
                           "tpa": self.tpa_field.text(), "total_de_vendas": total_vendas,
                           "total_de_pagamentos": total_pagamentos, "valor_liquido": valor_liquido,
                           "balanco_final": balanco_final}

            # transaction_report.hide()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow(transaction)
            self.ui.setupUi(self.window)
            self.window.show()



    def zero(self):
        key = "0"

        keyboard.press(key)
        keyboard.release(key)

    def one(self):
        key = "1"

        keyboard.press(key)
        keyboard.release(key)

    def two(self):
        key = "2"

        keyboard.press(key)
        keyboard.release(key)

    def three(self):
        key = "3"

        keyboard.press(key)
        keyboard.release(key)

    def four(self):
        key = "4"

        keyboard.press(key)
        keyboard.release(key)

    def five(self):
        key = "5"

        keyboard.press(key)
        keyboard.release(key)

    def six(self):
        key = "6"

        keyboard.press(key)
        keyboard.release(key)

    def seven(self):
        key = "7"

        keyboard.press(key)
        keyboard.release(key)

    def eight(self):
        key = "8"

        keyboard.press(key)
        keyboard.release(key)

    def nine(self):
        key = "9"

        keyboard.press(key)
        keyboard.release(key)

    def backspace(self):
        key = "1"

        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)

    def clear(self):
        key = "a"

        keyboard.press(Key.ctrl)
        keyboard.press(key)

        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)

        keyboard.release(key)
        keyboard.release(Key.ctrl)

class Ui_UserLogin(object):
    def setupUi(self, UserLogin):
        UserLogin.setObjectName("UserLogin")
        UserLogin.resize(498, 600)
        UserLogin.setAutoFillBackground(False)
        UserLogin.setStyleSheet("background-color: green;")

        self.user_id = QtWidgets.QLineEdit(UserLogin)
        self.user_id.setGeometry(QtCore.QRect(70, 380, 341, 51))
        self.user_id.setStyleSheet("QLineEdit {\n"
                                   "    border: 1px solid rgb(238, 238, 236);\n"
                                   "    border-radius: 20px;\n"
                                   "    padding: 15px;\n"
                                   "    background-color: #fff;\n"
                                   "    color: rgb(200, 200, 200);\n"
                                   "}\n"
                                   "QLineEdit:hover {\n"
                                   "    border: 1px solid rgb(186, 189, 182);\n"
                                   "}\n"
                                   "QLineEdit:focus {\n"
                                   "    border: 1px solid   rgb(114, 159, 207);\n"
                                   "    color: rgb(100, 100, 100);\n"
                                   "}")
        self.user_id.setText("")
        self.user_id.setObjectName("user_id")
        self.user_password = QtWidgets.QLineEdit(UserLogin)
        self.user_password.setGeometry(QtCore.QRect(70, 460, 341, 51))
        self.user_password.setStyleSheet("QLineEdit {\n"
                                         "    border: 1px solid rgb(238, 238, 236);\n"
                                         "    border-radius: 20px;\n"
                                         "    padding: 15px;\n"
                                         "    background-color: #fff;\n"
                                         "    color: rgb(200, 200, 200);\n"
                                         "}\n"
                                         "QLineEdit:hover {\n"
                                         "    border: 1px solid rgb(186, 189, 182);\n"
                                         "}\n"
                                         "QLineEdit:focus {\n"
                                         "    border: 1px solid   rgb(114, 159, 207);\n"
                                         "    color: rgb(100, 100, 100);\n"
                                         "}")
        self.user_password.setText("")
        self.user_password.setObjectName("user_password")
        self.login_button = QtWidgets.QPushButton(UserLogin)
        self.login_button.setGeometry(QtCore.QRect(180, 540, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.login_button.setFont(font)
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_button.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 15px;\n"
                                        "    background-color: rgb(255, 51, 102);\n"
                                        "    color:#fff;\n"
                                        "    font-size:15px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(255, 50, 121);\n"
                                        "    border-radius: 15px;\n"
                                        "    border:1px solid rgb(255, 51, 102);\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.login_button.setObjectName("login_button")
        self.label = QtWidgets.QLabel(UserLogin)
        self.label.setGeometry(QtCore.QRect(110, 110, 281, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("premier-bet-logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(UserLogin)
        QtCore.QMetaObject.connectSlotsByName(UserLogin)

        self.user_password.setEchoMode(QLineEdit.Password)

        self.label.setStyleSheet("background: transparent;")
        self.login_button.clicked.connect(self.log_in)


    def retranslateUi(self, UserLogin):
        _translate = QtCore.QCoreApplication.translate
        UserLogin.setWindowTitle(_translate("UserLogin", "UserLogin"))
        self.user_id.setPlaceholderText(_translate("UserLogin", "User ID"))
        self.user_password.setPlaceholderText(_translate("UserLogin", "Password"))
        self.login_button.setText(_translate("UserLogin", "LOGIN"))

    def log_in(self):

        global row_num
        temp_users = get_users()
        isAuthenticated = False
        for temp_user in temp_users:
            if str(self.user_id.text()).lower() == str(temp_user["uid"]).lower() and \
                    str(self.user_password.text()).lower() == str(temp_user["password"]).lower():

                manager_obj = {
                    "gerente_da_loja": temp_user["Gerente Da Loja"],
                    "nome_da_loja": temp_user["Nome da Loja"]
                }

                premier_records = get_premier_data()

                try:
                    ids_column = premier.col_values(1)
                    row_num = ids_column.index(temp_id) + 1
                except Exception as ignore:
                    pass

                for record in premier_records:
                    if int(record["ID"]) == int(self.user_id.text()):
                        isAuthenticated = True
                        temp_sum = 0
                        manager_obj["Flot Inicial"] = str(record["Flot Inicial"]) + "KZ"
                        manager_obj["Vendas SB"] = str(record["Vendas SB"]) + "KZ"
                        manager_obj["Pagamentos SB"] = str(record["Pagamentos SB"]) + "KZ"
                        manager_obj["Vendas Solidicon"] = (str(record["Vendas Solidicon"]) + "KZ")
                        manager_obj["Pagementos Solidicon"] = (str(record["Pagementos Solidicon"]) + "KZ")
                        manager_obj["Vendas GB"] = (str(record["Vendas GB"]) + "KZ")
                        manager_obj["Pagamento GB"] = (str(record["Pagamento GB"]) + "KZ")
                        manager_obj["Vendas TS7"] = (str(record["Vendas TS7"]) + "KZ")
                        manager_obj["Pagamento TS7"] = (str(record["Pagamento TS7"]) + "KZ")
                        temp_sum += str_to_float(record["Flot Inicial"]) + str_to_float(record["Vendas SB"]) - \
                                    str_to_float(record["Pagamentos SB"]) + str_to_float(record["Vendas Solidicon"]) \
                                    + str_to_float(record["Vendas TS7"]) - str_to_float(record["Pagamento TS7"]) \
                                    - str_to_float(record["Pagamento GB"]) + str_to_float(record["Vendas GB"]) + \
                                    str_to_float(record["Pagementos Solidicon"])
                        manager_obj["total"] = (str(round(temp_sum, 2)) + "KZ")



                if isAuthenticated:
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_transaction_report(manager_obj)
                    self.ui.setupUi(self.window)
                    login.hide()
                    self.window.show()
        if not isAuthenticated:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("WRONG ID OR PASSWORD!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_UserLogin()
    ui.setupUi(login)
    login.show()
    # transaction_report = QtWidgets.QMainWindow()
    # ui = Ui_transaction_report()
    # ui.setupUi(transaction_report)
    # transaction_report.show()
    sys.exit(app.exec_())


