# 파일 입출력 ==> open(), close()
# open(): 파일 개방 ==> 파일을 파일객체화
# close(): 파일 객체 해제

f = open("python.txt", "r+") # r 은 읽기, r+는 일고쓰기 가능 모드
strdata = f.read() # 텍스트 파일에 작성된 모든 내용을 읽어서 문자열 객체로 생성
print(strdata)
print( f.tell()) # 현재 파일포인터 위치를 반환
#strdata = f.readline() # 텍스트파일에 첫번째 한 줄만 읽어서 문자열 객체 생성
# f.seek(0,0) #파일포인터 맨위로 초기화
# print( f.tell() )
# strdata = f.readlines() # 각 라인의 텍스트를 리스트의 항목으로 넣어서 리스트로 반환
# print(strdata)
f.write("\ntest")
print(strdata)

f.close() # 파일 객체 메모리 해제, 프로그램이 종료되면 적어줄 필요는 없음