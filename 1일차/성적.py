# 문제

# 이름, 국어, 영어, 수학 입력 받아 총점과 평균 출력

Name = input("이름: ")
Korean = int(input("국어: "))
English = int(input("영어: "))
Math = int(input("수학: "))
Sum = Korean + English + Math

print(f"{Name}의 총점은 {Sum}이고 평균은 {Sum/3}입니다.")