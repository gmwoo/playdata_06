from 숫자야구게임 import gameData    # from 파일명 import 함수, 변수, 클래스 등

class GameManager:
    gameList = list()  # 앞으로 하는 게임은 여기에 저장하려 함
    def __init__(self):
        print("게임을 시작하지")
        
    def gameStart(self):
        while True:
            game = gameData()
            game.output()
            self.gameList.append(game)
            if len(self.gameList) > 7 and self.gameList.count('O')>3:
                print(self.gameList)
                return
    
    # 그 동안 했던 게임의 히스토리를 모두 출력
    def gameOutput(self):
        for game in self.gameList:
            game.output()
            
if __name__ == "__main__":
    mgr = GameManager()
    mgr.gameStart()
    mgr.gameOutput()