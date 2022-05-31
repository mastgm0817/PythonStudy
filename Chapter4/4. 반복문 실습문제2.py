# 반복문 실습문제 4.3.3
# 병연은 대학교에 Lily라는 이름의 교환학생과 친해지게 되었다. 영어를 잘하지 못했던 병연은, Lily에게
# 한국어를 가르쳐 주기 위해 한국어 연습 프로그램을 만들게 되었다.

# -learning Korean-
# 1. 연습할 한국어가 담긴 리스트를 만든다.
# 2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다.
# 3. 프로그램 사용자는 단어를 그대로 입력하고
# 4. 맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료.

from tkinter import E


words_dictionary = {"apple": "사과", "banana": "바나나",
                    "chocolate": "초콜렛", "American": "미국인", "soccer": "축구"}


english = list(words_dictionary.keys())
korean = list(words_dictionary.values())
score = 0

for i in range(0, len(english) - 1):
    print(f"문제: {english[i]}")
    answer = input("정답은?>>>")
    if answer != korean[i]:
        print(f"전체문제는: {len(english)} 개")
        print(f"맞춘개수는: {score} 개")
        print(f"틀린개수는: {len(english) - score} 개")
        break
    else:
        score += 1
