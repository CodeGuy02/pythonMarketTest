#ui TEST -

import matplotlib
matplotlib.use('Qt4Agg')

import sys
import requests
import time
import os
import xml.etree.ElementTree as ET
import sys
import shelve
import struct
import datetime
import random
import math
import platform

from colorama import init
from colorama import Fore, Back, Style
from subprocess import call

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.patches import Rectangle
from matplotlib.finance import candlestick_ohlc

import numpy as np
import timeit

from os import getpid
from multiprocessing import Process, Manager
from PyQt4 import QtGui, QtCore, uic
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from poloniex import poloniex

qtCreatorFile = "/home/user_name/Software/MarketBots.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)






class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    bot_slots_available = [True, True, True, True, True, True, True]
    num_bot_slots_available = 7
    bots = []

    market_slots_available = [True, True, True, True, True, True, True]
    num_market_slots_available = 7
    markets = []

    strategyTableFirstClick = [False, False, False, False, False, False, False]

    lastStrategyAvailableCellClicked = 0
    lastMarketSelected = 0

    # Connected States:
    connectedToPoloniex = False
    connectedToTDAmeritrade = False
    connectedToBinance = False





def handleButtonLogin(self):
    self.ActivityText.append('Logging In...')

    #call(["python Login.py"])
    self.launch_script()


def handleButtonLogout(self):
    self.ActivityText.append('Logging out...')

    global session
    global logout_state
    print('==================')
    print('Logging out now...')
    print('==================')

    url_logout = url + 'LogOut?source=SOURCEID'
    request = session.get(url_logout)
    print(request.content)
    logout_state = True

def launch_script(self):
        #self.panel = Login.runscript()
        #self.panel.show()
        global session
        print('================')
        print('=    Login     =')
        print('================')

        username = str(raw_input('User Name:'))
        password = str(raw_input('Password: '))
        post_data = {'userid': username, 'password': password, 'source': 'SOURCE_ID', 'version': '1001'}
        print('post_data = ')
        print(post_data)

        session = requests.session()
        request = session.post(url_login, post_data, headers)

        print('request.content = ')
        print(request.content)

        self.BalancesAndPositions()

        self.priceHistory()

def displaySystemStatus(self):
        self.AccountDetailsText.append('                                    Test Version 0.1                          ')
        self.AccountDetailsText.append('_____________________________________________________________________________________________')
        self.AccountDetailsText.append('Machine:    ' + str(platform.machine()))
        self.AccountDetailsText.append('System:     ' + str(platform.platform()))
        self.AccountDetailsText.append('_____________________________________________________________________________________________')


def updateUIwork(self,val):
        val = str(val)
        #self.ActivityText.append(val)

def MarketTableDefaultValues(self, default_string):
        rows = 7
        row = 0
        while row < rows:
            self.MarketTable.setItem(row, 0, QtGui.QTableWidgetItem(str(default_string)))
            row = row + 1

def updateUItestCompletion(self, percent):
        self.BackTestDataCompletionProgressBar.setValue(percent)

def updateUIchartValuesCompletion(self, key):
        self.ActivityText.append(str(key))

def updateUItestStrategyComboBox(self):
        comboName = str(self.TestStrategyComboBox.currentText())
        row = self.lastStrategyAvailableCellClicked
        self.StrategyAvailableTable.setItem(row, 0, QtGui.QTableWidgetItem(str(comboName)))

def updateUIstockBought(self, buy_notice):
        self.ActivityText.append(buy_notice)

def updateUIstockSold(self, sold_notice):
        self.ActivityText.append(sold_notice)


def strategy_available_cell_clicked(self, row, column):
        self.lastStrategyAvailableCellClicked = row
        self.updateUIstartingStrategyValues()

def marketCellClicked(self, row, column):
        self.lastMarketSelected = row

def updateUImarketBackTestComboBox(self):
        comboName = str(self.MarketBackTestComboBox.currentText())
        row = self.lastStrategyAvailableCellClicked
        self.BackTestingTable.setItem(row, 0, QtGui.QTableWidgetItem(str(comboName)))

def updateUIcandlestickComboBox(self):
        comboName = str(self.CandlestickComboBox.currentText())
        row = self.lastStrategyAvailableCellClicked
        self.BackTestingTable.setItem(row, 1, QtGui.QTableWidgetItem(str(comboName)))

def updateUIdaysComboBox(self):
        comboName = str(self.DaysComboBox.currentText())
        row = self.lastStrategyAvailableCellClicked
        self.BackTestingTable.setItem(row, 2, QtGui.QTableWidgetItem(str(comboName)))

