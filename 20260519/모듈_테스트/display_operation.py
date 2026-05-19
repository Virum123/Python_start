


def Display_On(): # 함수 정의
    print("💫번쩍✨")

#함수 정의가 동작하려면 함수 호출이 꼭 필요

# 현재 파일이 싫행 모듈일 경우 내부 특수 변수 __name__은 __main__ 을 가짐
# 해당 파일이 import 되는 모듈인 경우 __name__은 모듈명(파일명)을 갖는다
if __name__ == '__main__':
    print("__name__ : ", __name__) #shift tab 하면 전체 들여쓰기 가능
    Display_On() # 함수 호출