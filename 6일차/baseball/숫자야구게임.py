'''
[3, 5, 7] = [5, 3, 7]

위치도 같고 값도 같으면 strike
위치가 다르고 값이 존재하면 ball
없으면 out
3 strike가 나오거나 7번 해도 안되면, 정답을 출력하고 종료

누적해서 나중에 전체 몇 번 게임을 했고 몇 번 이겼다가 통계로 나와야 함
'''

# 한 판
import random

class gameData:
    STRIKE = 1
    BALL = 2
    OUT = 3
    def __init__(self):
        self.computer = [random.randint(1,9) for i in range(3)]
        print(f"computer: {self.computer}")
        self.result = []
        self.point = list()
        for i in range(3):
            self.point.append(int(input("1~9사이 입력: ")))
        print(self.point)
        self.winner = self.score()   # 함수 호출
        
    def score(self):
        # strike
        if self.computer == self.point:
            return self.STRIKE
        # ball
        elif 1 < len(list(set(self.computer) & set(self.point))) < 3:
            return self.BALL        
        # out
        elif len(list(set(self.computer) & set(self.point))) == 0:
            return self.OUT

        # out
        if self.computer not in self.point:
            return self.OUT
        
    def output(self):
        words = ["", "S", "B", "O"]
        print(words[self.winner])
        self.result.append(words[self.winner])
        # print(self.result)
            
if __name__ == "__main__":
    game = gameData()
    game.output()