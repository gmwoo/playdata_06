from pay import Pay
class PayManager:
    payList = []
    def __init__(self):
        self.payList.append(Pay("A", 30, 20000))
        self.payList.append(Pay("B", 40, 30000))
        self.payList.append(Pay("C", 20, 10000))
        self.payList.append(Pay("D", 15, 20000))
        self.payList.append(Pay("E", 25, 30000))
    
    def append(self):
        pay = Pay()
        pay.name = input("이름: ")
        pay.work_time = int(input("일 한 시간: "))
        pay.per_pay = int(input("시간 당 급여액: "))
        pay.calculate()
        self.payList.append(pay)

    def output(self):
        for pay in self.payList:
            pay.output()
        
    def menu(self):
        print("1. 추가")
        print("2. 출력")
        print("0. 종료")
    
    def start(self):
        while True:
            self.menu()
            sel = input("선택: ")
            if sel == "1":
                self.append()
            elif sel == "2":
                self.output()
            else:
                print("프로그램 종료")
                return

# 하나의 파일에 하나의 클래스를 만든다
# 다른 파일에 있을 때 모듈을 가져오려면 import 를 사용한다
# 외부 모듈 불러오기

if __name__ == "__main__":
    mgr = PayManager()
    mgr.start()