from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from error import *

class Kiwoom(QAxWidget):

    def __init__(self):
        super().__init__()
        print("kiwoom Class init")
        self.login_event_loop = None
        self.tr_event_loop = None

        self.get_ocx_instance()
        self.reg_slot()

    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def reg_slot(self):
        self.OnEventConnect.connect(self.login_slot)
        self.OnReceiveTrData.connect(self.trdata_slot)
        self.OnReceiveRealData.connect(self.trdata_slot)
        self.OnReceiveMsg.connect(self.trdata_slot)
        self.OnReceiveChejanData.connect(self.trdata_slot)


    def login_slot(self, errCode):
        # TODO : ERROR 처리
        print(errCode)
        if errCode == 0:
            print("로그인 성공")
        else:
            print("로그인 실패")

        self.login_event_loop.exit()

    def trdata_slot(self, sScrNo,  sRQName,  sTrCode, sRecordName,  sPrevNext):
        print("trdata_slot %s"%sRQName)

        if sRQName == "계좌평가잔고내역요청":
            count = self.dynamicCall("GetDataCount(QString)", ["계좌평가잔고개별합산"])
            for i in range(0, count):
                종목명 = self.dynamicCall("CommGetData(QString, QString, QString, int, QString)", sTrCode, "", sRQName, i, "종목명")
            print("종목명 %s"%종목명)

        else:
            deposit = self.dynamicCall("GetCommData(1,2,3,4)",sTrCode,sRecordName,0,"예수금")
            print("deposit %s"%int(deposit))
        '''
        BSTR strTrCode,   // TR 이름
        BSTR strRecordName,   // 레코드이름
        long nIndex,      // TR반복부
        BSTR strItemName) // TR에서 얻어오려는 출력항목이름")
        '''
        self.tr_event_loop.exit()

    ##############################################
    # Function
    ##############################################

    def login(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def check_login(self):
        ret = self.dynamicCall("GetConnectState()")
        return ret

    def get_serverInfo(self):
        print("get_serverInfo")
        ret = self.dynamicCall("GetLoginInfo(String)", "GetServerGubun")
        print(ret)
        ret = self.dynamicCall("GetLoginInfo(String)", "USER_NAME")
        print(ret)

    def tr_balance(self):
        self.dynamicCall("SetInputValue(QString, QString)", "계좌번호", self.accnum)
        self.dynamicCall("SetInputValue(QString, QString)", "조회구분", 2)
        ret = self.dynamicCall("CommRqData(QString, QString, int, QString)", "계좌평가잔고내역요청", "opw00018", 0, "100")
        self.tr_event_loop = QEventLoop()
        self.tr_event_loop.exec_()

    def get_myinfo(self):
        accnum_list=self.dynamicCall("GetLoginInfo(String)", "ACCLIST")
        self.accnum=accnum_list.split(";")[0]
        print(self.accnum)


    def detail_account(self):
        self.dynamicCall("SetInputValue(String,String","계좌번호",self.accnum)
        self.dynamicCall("SetInputValue(String,String","비밀번호","0000")
        self.dynamicCall("SetInputValue(String,String","비밀번호입력매체구분","00")
        self.dynamicCall("SetInputValue(String,String","조회구분","2")
        self.dynamicCall("CommRqData(,,,)","REQ_JKLEE", "opw00001"	,  "0"	,  "100")
        self.tr_event_loop = QEventLoop()
        self.tr_event_loop.exec_()



#print(kiwoom_main.dynamicCall("GetBranchCodeName()"))
#print(kiwoom_main.dynamicCall("GetCodeListByMarket(0)", 10))
