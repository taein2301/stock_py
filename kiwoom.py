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
        self.event_slot()
        self.signal_login_comConnect()
        self.get_myinfo()
        self.detail_account()

    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def event_slot(self):
        self.OnEventConnect.connect(self.login_slot)
        self.OnReceiveTrData.connect(self.trdata_slot)

    def login_slot(self, errCode):
        print(errCode)
        self.login_event_loop.exit()

    def signal_login_comConnect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def get_myinfo(self):
        accnum_list=self.dynamicCall("GetLoginInfo(String)", "ACCLIST")
        self.accnum=accnum_list.split(";")[0]
        print(self.accnum)

    def detail_account(self):
        self.dynamicCall("SetInputValue(String,String","계좌번호",self.accnum)
        self.dynamicCall("SetInputValue(String,String","비밀번호","0000")
        self.dynamicCall("SetInputValue(String,String","비밀번호입력매체구분","00")
        self.dynamicCall("SetInputValue(String,String","조회구분","2")
        self.dynamicCall("CommRqData(1,2,3,4)","REQ_JKLEE", "opw00001"	,  "0"	,  "100");
        print("detail_acc")
        self.tr_event_loop = QEventLoop()
        self.tr_event_loop.exec_()



    def trdata_slot(self, sScrNo,  sRQName,  sTrCode, sRecordName,  sPrevNext):
        print("trdata_slot %s"%sRQName)
        #print("SEQNO %s SRQName %s Code %s RecordName %s Next %s"%sScrNo,sRQName,sTrCode,sRecordName,sPrevNext)

        deposit = self.dynamicCall("GetCommData(1,2,3,4)",sTrCode,sRecordName,0,"예수금")
        print("deposit %s"%int(deposit))
        '''
        BSTR strTrCode,   // TR 이름
        BSTR strRecordName,   // 레코드이름
        long nIndex,      // TR반복부
        BSTR strItemName) // TR에서 얻어오려는 출력항목이름")
        '''
        self.tr_event_loop.exit()


