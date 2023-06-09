from gameData import GameData    # from 파일명 import 함수, 변수, 클래스 등

class GameManager:
    gameList = list()  # 앞으로 하는 게임은 여기에 저장하려 함
    def __init__(self):
        print("게임을 시작하지")
        
    def gameStart(self):
        while True:
            game = GameData()
            game.output()
            self.gameList.append(game)
            again = input("계속 할텨? ")
            if again != "Y" and again != "y":
                return
    
    # 그 동안 했던 게임의 히스토리를 모두 출력
    def gameOutput(self):
        for game in self.gameList:
            game.output()
            
    def gameStatics(self):
        statics = [0, 0, 0, 0]
        for game in self.gameList:
            # 컴퓨터가 이기면 statics의 1번방 증가, 사람이 이기면 2번방 증가, 비기면 3번방 증가
            statics[game.winner] +=1
            statics[0] += 1
        print(f"갯수 - 컴퓨터승 : {statics[1]}, 사람승수: {statics[2]}, 무승부: {statics[3]}")
        print("--- 각 승률 ---")       
        print(f"컴퓨터승 : {statics[1]/statics[0]}")
        print(f"사람승수: {statics[2]/statics[0]}")
        print(f"무승부: {statics[3]/statics[0]}")
            
if __name__ == "__main__":
    mgr = GameManager()
    mgr.gameStart()
    mgr.gameOutput()
    mgr.gameStatics()