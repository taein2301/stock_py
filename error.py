
def errorNo(errorCode):
    if errorCode == 0:
        return "Success"
    else:
        return "Fail"


'''
------------------------------------------------------------------------------------------------------------------------------------
OpenAPI는 함수에서 리턴값으로 함수성공여부를 판단할 수 있는데 0이면 함수호출 성공, 0보다 작은 값은 에러를 나타냅니다.
주요 에러코드는 -200번(시세과부하), -308번(주문전송 과부하)입니다.
------------------------------------------------------------------------------------------------------------------------------------
              0         // 정상처리
            -10        // 실패
            -11        // 조건번호 없슴                                                                
            -12        // 조건번호와 조건식 불일치                                                     
            -13        // 조건검색 조회요청 초과                                                       
          -100        // 사용자정보교환 실패                                                           
          -101        // 서버 접속 실패                                                                
          -102        // 버전처리 실패                                                                 
          -103        // 개인방화벽 실패                                                               
          -104        // 메모리 보호실패                                                               
          -105        // 함수입력값 오류                                                               
          -106        // 통신연결 종료                                                                 
          -107        // 보안모듈 오류                                                                 
          -108        // 공인인증 로그인 필요                                                          

          -200        // 시세조회 과부하                                                               
          -201        // 전문작성 초기화 실패.                                                         
          -202        // 전문작성 입력값 오류.                                                         
          -203        // 데이터 없음.                                                                  
          -204        // 조회가능한 종목수 초과. 한번에 조회 가능한 종목개수는 최대 100종목.           
          -205        // 데이터 수신 실패                                                              
          -206        // 조회가능한 FID수 초과. 한번에 조회 가능한 FID개수는 최대 100개.               
          -207        // 실시간 해제오류                                                               
          -209        // 시세조회제한                                                               

          -300        // 입력값 오류
          -301        // 계좌비밀번호 없음.                                                            
          -302        // 타인계좌 사용오류.                                                            
          -303        // 주문가격이 주문착오 금액기준 초과.                                                     
          -304        // 주문가격이 주문착오 금액기준 초과.                                                     
          -305        // 주문수량이 총발행주수의 1% 초과오류.                                          
          -306        // 주문수량은 총발행주수의 3% 초과오류.                                          
          -307        // 주문전송 실패                                                                 
          -308        // 주문전송 과부하                                                               
          -309        // 주문수량 300계약 초과.                                                        
          -310        // 주문수량 500계약 초과.                                                        
          -311        // 주문전송제한 과부하
          -340        // 계좌정보 없음.                                                                
          -500        // 종목코드 없음.                                                                
'''
