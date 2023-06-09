# 사람의 개인정보를 만듦
class Person:
    # name = "홍길동"
    # age = 23
    # phone = []  # 클래스 정의할 때 딱 한 번 실행
    ######## 이 위치에 list나 dict 같은 객체를 선언할 경우 객체가 클래스 정의 시 딱 한 번만 만들어져서 공유되기 때문에 가급적 이 위치에 변수 만들지 말자
    
    def __init__(self, name="홍길동", age=20): 
        self.name=name
        self.age=age
        self.phone=[]
        print("생성자 호출")
    
    def output(self):
        # 반드시 self로 접근
        print(f"{self.name} {self.age}")
    
    
# 변수 생성은 생성자에서 하자    
    
p1 = Person()  # 객체 생성, 이 객체를 '인스턴스'라고도 부름
p1.phone.append("010-0000-0000")
print(p1.name)
print(p1.age)
print(p1.phone)

# 함수 밖에 변수를 선언했을 경우, 메모리가 클래스 지정할 때 하나만 만들어짐
p2 = Person()  
p2.phone.append("010-0000-2222")
p2.name = "임꺽정"  # 이 때, p2용의 name 속성을 만들어서 데이터 저장
print(p2.name)
print(p2.age)
print(p2.phone)
    
p1.output()
p2.output()

# 객체 생성 방법이 다양해짐
p3 = Person("김종국")
p4 = Person("유재석", 52)
p5 = Person(age=35)

p3.output()
p4.output()
p5.output()

