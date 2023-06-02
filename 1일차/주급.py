# 문제: 주급 계산하기, 근무시간(30), 시간당급여액(15000)

# Time = input("근무시간: ")
# money = input("시간당급여액: ")
# total = int(Time) * int(money)
# print("주급: ", total)

time, money = map(int, input('근무시간, 시간당급여액: ').split())
total = time * money
print("주급: ", total)
print("주급: " + str(total)) # , 대신 + 를 사용 가능
print(str.format("주급: %d " % total)) # 문자열과 숫자를 섞어서 출력할 때, 웹프로그램 또는 db에 데이터 읽고 쓸 때 많이 씀
print(f"주급은 {total}") # fstring 3.6부터 문자열 앞에 f를 씀, 대세
