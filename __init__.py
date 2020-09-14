#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kiwoom
import sys
from PyQt5.QtWidgets import *

def main():
    print("TEST")
    app = QApplication(sys.argv)
    kiwoomVal = kiwoom.Kiwoom()
    app.exec_()

if __name__ == '__main__':
    main()

