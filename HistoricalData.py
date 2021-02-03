import argparse
import datetime
import collections
import inspect

import logging
import time
import os.path

import pandas as pd

from ibapi import wrapper
from ibapi import utils
from ibapi.client import EClient
from ibapi.utils import iswrapper

from ibapi.common import *
from ibapi.order_condition import *
from ibapi.contract import *
from ibapi.order import *
from ibapi.order_state import *
from ibapi.execution import Execution
from ibapi.execution import ExecutionFilter
from ibapi.commission_report import CommissionReport
from ibapi.ticktype import *
from ibapi.tag_value import TagValue

from ibapi.account_summary_tags import *

from ContractSamples import ContractSamples
from OrderSamples import OrderSamples
from AvailableAlgoParams import AvailableAlgoParams
from ScannerSubscriptionSamples import ScannerSubscriptionSamples
from FaAllocationSamples import FaAllocationSamples
from ibapi.scanner import ScanData


class TestClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)


class TestWrapper(wrapper.EWrapper):
    def __init__(self):
        wrapper.EWrapper.__init__(self)


class TestApp(TestWrapper, TestClient):
    def __init__(self):
        TestWrapper.__init__(self)
        TestClient.__init__(self, wrapper=self)

    def error(self, reqid, errorcode, errorstring):
        print("Error: ", reqid, " ", errorcode, " ", errorstring)

    def historicalData(self, reqid: int, bar: BarData):
        print("HistoricalData. ReqId:", reqid, "BarData.", bar)

    def historicalDataUpdate(self, reqid: int, bar: BarData):
        print("HistoricalDataUpdate. ReqId:", reqid, "BarData.", bar)

    def historicalDataEnd(self, reqid: int, start: str, end: str):
        print("HistoricalDataEnd. ReqId:", reqid, "from", start, "to", end)
        print("Finished")

    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)

        logging.debug("setting nextValidOrderId: %d", orderId)
        self.nextValidOrderId = orderId
        print("NextValidId:", orderId)

    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        super().contractDetails(reqId, contractDetails)
        printinstance(contractDetails)
        self.reqContractDetails(10004, ContractSamples.NewsFeedForQuery())

    def contractDetailsEnd(self, reqId: int):
        super().contractDetailsEnd(reqId)
        print("ContractDetailsEnd. ReqId:", reqId)

def main():
    app = TestApp()
    app.connect("127.0.0.1", 7497, clientId=1)
    print(app.isConnected())
    time.sleep(1)

    contract = Contract()

    contract.secType = "CASH"
    contract.symbol = "AUD"
    contract.currency = "USD"
    contract.exchange = "IDEALPRO"

    querytime = (datetime.datetime.today() - datetime.timedelta(days=180)).strftime("%Y%m%d %H:%M:%S")

    app.reqHistoricalData(4002, contract, querytime, "1 Y", "1 day", "MIDPOINT", 1, 1, False, [])

    app.run()

    app.disconnect()

if __name__ == "__main__":
    main()