# if문을 사용하여 로그인 시스템을 만들기

origin_pass = "1234"
input_pass = input("비밀번호를 입력해주세요 >>>")

if origin_pass == input_pass:
    print("로그인 성공")
elif input_pass == "":
    print("아무것도 입력하지 않으셨네요?")
else:
    print("비밀번호가 틀렸습니다.")
