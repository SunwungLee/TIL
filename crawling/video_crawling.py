import os
from pytube import YouTube
from moviepy.editor import *

# 폴더 이름 설정

# 유튜브 주소 입력 유효성 검사
while True:
    print("유튜브 주소를 입력하세요.")
    try:
        yt_input = input(" >>> ")
        print("유튜브 영상 불러오는 중...")
        yt = YouTube(yt_input)
        break
    except:
        print("유효하지 않은 주소입니다.\n")

# 바탕화면에 폴더 생성
forderPath = "./videos"
if not os.path.isdir(forderPath):
    os.makedirs(forderPath)

# mp4 확장자로 필터링
yt_streams = yt.streams.filter(file_extension='mp4').all()

# 다운 가능한 영상 화질 출력
print(f"\n제목 : {yt.title}\n")
for i in range(len(yt_streams)):
    print(f"{i + 1} 번 영상 화질 : {yt_streams[i].resolution}")

# 입력 유효성 검사
print("\n다운받을 영상의 번호를 입력해주세요.")
while True:
    try:
        num = int(input(" >>> ")) - 1
        if (0 <= num and num < len(yt_streams)):
            print("\n다운로드 중... \n잠시만 기다려주세요.\n")
            break
        else:
            print(f"\n1~{len(yt_streams)} 사이 번호를 입력해주세요.")
    except:
        print(f"\n1~{len(yt_streams)} 사이 번호를 입력해주세요.")

# 다운로드
yt_streams[num].download(forderPath)
print("\n다운로드가 완료되었습니다..")

os.startfile(forderPath)