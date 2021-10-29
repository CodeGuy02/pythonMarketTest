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

from market1 import market1

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
    connectedTomarket1 = False
    connectedTomarket2 = False
    connectedTomarket3 = False

def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Thread Test:
        #self.threadclass = ThreadClass()
        #self.threadclass.start()
        #self.connect(self.threadclass, QtCore.SIGNAL('WORK_01'), self.updateUIwork)

        # New Strategy Thread:
        self.StrategyThread = StrategyThread()
        self.StrategyThread.start()
        self.connect(self.StrategyThread, QtCore.SIGNAL('STRATEGY_TEST_COMPLETION'), self.updateUItestCompletion)
        self.connect(self.StrategyThread, QtCore.SIGNAL('CHART_VALUES_COMPLETION'), self.updateUIchartValuesCompletion)
        self.connect(self.StrategyThread, QtCore.SIGNAL('BOUGHT'), self.updateUIstockBought)
        self.connect(self.StrategyThread, QtCore.SIGNAL('SOLD'), self.updateUIstockSold)
        self.connect(self.StrategyThread, QtCore.SIGNAL('RESULTS'), self.updateUIresults)

        # Setup Menus:
        self.bar = self.menuBar()
        self.MarketsAvailableMenu = self.bar.addMenu("Markets Available")
        self.SetupMarketsMenu = self.bar.addMenu("Setup Markets")

        # Define our QAction items:
        self.connectmarket1 = self.MarketsAvailableMenu.addAction("Connect to Market 1")
        self.connectmarket2 = self.MarketsAvailableMenu.addAction("Connect to Market 2")
        self.connectmarket3 = self.MarketsAvailableMenu.addAction("Connect to Market 3")
        self.setupmarket1 = self.SetupMarketsMenu.addAction("Setup Market 1")
        self.setupmarket2 = self.SetupMarketsMenu.addAction("Setup Market 2")
        self.setupmarket3 = self.SetupMarketsMenu.addAction("Setup Market 3")

        self.connectmarket1.triggered.connect(self.connectToMarket1)
        self.connectmarket2.triggered.connect(self.connectToMarket2)
        self.connectmarket3.triggered.connect(self.connectToMarket3)

        # Setup Menus and Buttons:
        self.setupButtons()

        self.setupNewBotTable()
        self.NameComboBox.currentIndexChanged.connect(self.updateUInameComboBox)
        self.MarketComboBox.currentIndexChanged.connect(self.updateUImarketComboBox)
        self.FundsAsgnComboBox.currentIndexChanged.connect(self.updateUIfundsAsgnComboBox)
        self.LossThresholdComboBox.currentIndexChanged.connect(self.updateUIlossThresholdComboBox)
        self.StrategyComboBox.currentIndexChanged.connect(self.updateUIstrategyComboBox)

        self.TestStrategyComboBox.currentIndexChanged.connect(self.updateUItestStrategyComboBox)
        self.MarketBackTestComboBox.currentIndexChanged.connect(self.updateUImarketBackTestComboBox)
        self.CandlestickComboBox.currentIndexChanged.connect(self.updateUIcandlestickComboBox)
        self.DaysComboBox.currentIndexChanged.connect(self.updateUIdaysComboBox)
        #self.threadCreateNewBot = ThreadCreateNewBot()
        #self.threadCreateNewBot.setValuesFromUI(self.num_bot_slots_available,self.bot_slots_available,)
        #self.connect(self.threadCreateNewBot, QtCore.SIGNAL('CREATING_NEW_BOT'), self.updateUIcreate_new_bot)

        #self.bot1.getCurrentRecordDataFromFile()
        #self.bot2.getCurrentRecordDataFromFile()
        #self.bot3.getCurrentRecordDataFromFile()

        #self.loadBotData(self.bot1)
        #self.loadBotData(self.bot2)
        #self.loadBotData(self.bot3)
        self.BotsAvailableTable.cellClicked.connect(self.cell_was_clicked)
        self.StrategyAvailableTable.cellClicked.connect(self.strategy_available_cell_clicked)
        self.BackTestingTable.cellClicked.connect(self.strategy_available_cell_clicked)
        self.MarketTable.cellClicked.connect(self.marketCellClicked)
        self.MarketTableDefaultValues(' ')

        self.displaySystemStatus()



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

def generateGraphs(self):
        print('    ------ Generating Graphs --------------')
        if self.marketName == 'TD Ameritrade':
            plot_data = {}
            graphs_ohlc_data = self.TDAmeritrade_data
            for currencyPair, chartData in graphs_ohlc_data.iteritems():
                #print('currencyPair to graph = ' + str(currencyPair))
                fig = plt.figure()

                #fig.patch.set_facecolor('#260031') # Deep lavender ?
                fig.patch.set_facecolor('#000034')


                pltOHLC = fig.add_subplot(311) # Obtain subplot from fig

                pltOHLC.grid(True)
                pltOHLC.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode='expand', borderaxespad=0.)
                # new_market = str(goodVolume[1])
                new_market = str(currencyPair)
                new_ohlc = graphs_ohlc_data[new_market]

                #print('creating new plot for: ' + new_market)
                # ax = Axes.minorticks_on(Axes)
                if (self.days == '1 day') or (self.days == '2 days') or (self.days == '1 week'):
                    #print('_____using smaller bars...')
                    #candlestick_ohlc(pltOHLC, new_ohlc, width=0.0002, colorup='#baffc9', colordown='#ffb3ba')
                    candlestick_ohlc(pltOHLC, new_ohlc, width=0.0002, colorup='#aa2d7d', colordown='#611d6d')
                else:
                    print('_____using CHUNKY bars...')
                    candlestick_ohlc(pltOHLC, new_ohlc, width=0.2, colorup='#aa2d7d', colordown='#611d6d')

                for label in pltOHLC.xaxis.get_ticklabels():
                    label.set_rotation(0)

                # pltOHLC.xaxis.set_major_locator(mdates.DayLocator())
                pltOHLC.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
                # pltOHLC.set_xticks(ohlc[0][0], ohlc[(bar_count - 1)][0])

                #description = self.descriptionList[new_market]
                #pltOHLC.set_title(new_market + ' - ' + str(self.marketName) + ' - ' + str(description))
                pltOHLC.set_title(new_market + ' - ' + str(self.marketName))
                pltOHLC.set_xlabel('Date')
                pltOHLC.set_ylabel('Price')

                # print(graphs_ohlc_data[str(goodVolume[0])])
                bar_count = len(graphs_ohlc_data[new_market])
                #print('bar count for graph test = ' + str(bar_count))

                xmin = graphs_ohlc_data[new_market][0][0]
                xmax = graphs_ohlc_data[new_market][(bar_count - 1)][0]
                # xmin = 0
                # xmax = bar_count
                # append_day = time, stock_open, stock_high, stock_low, stock_close, stock_volume
