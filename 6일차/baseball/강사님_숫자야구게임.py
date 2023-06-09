import random 
class BaseBallData:
    def __init__(self):
        self.computer = list() #컴퓨터가 생각한 숫자
        self.person = list()  #사람이 생각한 숫자 
        self.gameResult = list() #[0, 0, 0] 스트라이크숫자, 볼숫자 아웃숫자
        self.personList = list()
    
    def createComputer(self):
        cnt = 1  
        while cnt<=3:
            temp = random.randint(0, 9)
            if temp not in self.computer:
                self.computer.append(temp)
                cnt = cnt+1
                
    def createPerson(self):
        print("숫자 3개를 중복되지 않게 공백으로 나누어서 입력하세요")
        nums = input("0~9까지의 정수 세개 : ")
        nums = nums.split(" ") #-> list로 바뀐다 
        self.person=list()
        
        cnt = 1  
        while cnt<=3:
            temp = int(nums[cnt-1])
            if temp not in self.person:
                self.person.append(temp)
                cnt = cnt+1  
            else:
                print("이미 있는 숫자입니다")  
        self.personList.append( self.person )
                
    def process(self):
        result = [0,0,0]
        for i  in range(0, 3):
            if self.person[i] in self.computer:
                if self.person[i] == self.computer[i]:
                    result[0] += 1  #스트라이크
                else:  
                    result[1] += 1 #볼
            else:
                result[2]+=1  #아웃
        self.gameResult.append( result )
        print(f"스트라이크 :{result[0]} 볼:{result[1]} 아웃:{result[2]}")
        
        if result[0]==3:
            return True 
        else:
            return False 
        
    def start(self):
        #1.컴퓨터가 번호3개를 생각한다 
        self.createComputer()
        #2.사람이 숫자를 입력한다. - 3스트라이크가 되거나 7번을 기회를 다 써던가 
        cnt = 1 
        flag = False
        while not flag and  cnt<=7:
            self.createPerson() 
            flag = self.process() 
            cnt+=1
            
        if flag:
            print(f"성공 {cnt-1}만에 맞춤")
        else:
            print("실패")            
        
if __name__ == "__main__":
    b = BaseBallData()
    b.start()