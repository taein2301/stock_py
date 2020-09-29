#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import kiwoom
import sys
import time
from PyQt5.QtWidgets import *


def main():
    app = QApplication(sys.argv)
    kiwoom_main =kiwoom.Kiwoom()

    while "true":

        if kiwoom_main.check_login() == 1:
            # time.sleep(2)
            # TODO : 내 잔고 체크
            kiwoom_main.get_serverInfo()
            kiwoom_main.get_myinfo()
            ##kiwoom_main.tr_balance()
            # TODO : 매수
            # TODO : 매도
        else:
            print("로그인 안된 상태 로그인시도")
            kiwoom_main.login()

        time.sleep(3)

    app.exec_()


if __name__ == '__main__':
    main()


