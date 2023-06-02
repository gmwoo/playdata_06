# 미터를 입력받아 km와 m 구하기
# 입력 예) 미터: 1234
# 출력 예) 1234m는 1km와 234m 입니다.

met = int(input("미터: "))
kilo_met = met // 1000
change_met = met & 1000
print(f"{met}m는 {kilo_met}km {change_met}m 입니다.")