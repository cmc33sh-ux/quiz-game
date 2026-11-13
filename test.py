print ("Hello,Pythone!")

name = "철수"
score = 100
print(name)
print(score)

name = "철수"
score = 100
is_correct = True
print(type(name))
print(type(score))
print(type(is_correct))

score = 85
if score >= 90:
    print("A등급")
elif score >= 80:
    print("B등급")
else: 
    print("C등급")


answer=input("정답을 입력하세요:")
print("입력한 정답은", answer, "입니다.")

# 1. 문제 출력
print("대한민국의 수도는?")

# 2. 입력 받기
answer = input("정답: ")

# 3. 정답 확인 (참/거짓 조건문!)
if answer == "서울":
    print("정답입니다! ✅")
else:
    print("틀렸습니다! ❌")

print("대한민국의 수도는?")
answer = input("정답: ")
# 반복문 기초
for i in range(3):
    print(f"{i}번째 반복!")

question = [
     "대한민국의 수도는?",
     "가장 큰 행성은?",
     "물의 화학식은?",
]
print(question[0])
print(question[1])
print(question[2])

answers = ["서울", "목성", "H2O"]
for i in range(3):
    print(question[i])
    answer = input("정답: ")
    if answer == answers[i]:
        print("정답입니다! ✅")
    else:
        print("틀렸습니다! ❌")