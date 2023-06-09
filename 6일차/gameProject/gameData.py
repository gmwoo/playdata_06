# 한 게임 분의 코드
import random

class GameData:   # 클래스명은 가급적 첫 글자를 대문자로
    COMWIN = 1
    PERWIN = 2
    DRAW = 3
    
    def __init__(self):      # 생성자 만들기
        self.computer = random.randint(1,3)
        self.person = int(input("1. 가위, 2. 바위, 3. 보 "))
        self.winner = self.whoIsWinner()   # 함수 호출
        
    def whoIsWinner(self):   # gameinfo 라는 dict 타입 대신 self로
        if self.computer == self.person:
            return self.DRAW   # 비김
        
        if self.computer == 1 and self.person == 2:
            return self.PERWIN   # 사람이 이김
        if self.computer == 1 and self.person == 3:
            return self.COMWIN   # 컴퓨터가 이김
        
        if self.computer == 2 and self.person == 1:
            return self.COMWIN   # 컴퓨터가 이김
        if self.computer == 2 and self.person == 3:
            return self.PERWIN   # 사람이 이김
        
        if self.computer == 3 and self.person == 1:
            return self.PERWIN   # 사람이 이김
        if self.computer == 3 and self.person == 2:
            return self.COMWIN   # 컴퓨터가 이김
        
    def output(self):
        words = ["", "가위", "바위", "보"]
        words2 = ["", "컴퓨터승", "사람승", "무승부"]
        
        print(f"컴퓨터:{words[self.computer]}, 사람:{words[self.person]} {words2[self.winner]}")
            
if __name__ == "__main__":
    game = GameData()
    game.output()