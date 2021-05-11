# YouTube crawling

---

---

[https://www.youtube.com/watch?v=INTDdN6p7SI](https://www.youtube.com/watch?v=INTDdN6p7SI)

# Background Knowledge

---

- URL

    ### What is URL (Uniform Resource Locator)?

    **네트워크 상에서 자원이 어디 있는지를 알려주기 위한 약속**

    [URL - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/URL)

    ### How can we get url from YouTube?

    - 일반적인 URL 가져오기 : **주소 표시줄** **URL** **복사,** 주로 **동영상 전체를 다운로드** 하기 위한 방법
    - 동영상 URL 가져오기 :  주로 **동영상의 특정 부분을 필터링해서 다운로드** 하기 위한 방법
        1. 유튜브 **동영상** 재생 **영역**에서 **마우스 오른쪽 버튼 클릭**
        2. **'동영상 URL 복사' 클릭**

            ![YouTube/Untitled.png](YouTube/Untitled.png)

- API

    API(Application Programming Interface)는
    **앱을 만들기 위해 참고할 수 있는 사이트**

    [API - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/API)

- 주소표시줄

    브라우저에서 
    **URL(Uniform Resource Locator)를 표현하는 공간**

    ![YouTube/Untitled%201.png](YouTube/Untitled%201.png)

    빨간 네모박스: 주소표시줄

- 비디오 ID

    비디오 ID는 유튜버로부터 업로드된 YouTube **동영상의 고유 ID**이다.

    예를 들면, 
    YouTube 페이지 URL (https://www.youtube.com/watch?v=MssCLewODGc)
    동영상의 URL (https://youtu.be/MssCLewODGc)

    즉, 이 비디오의 ID는 겹치는 부분인 **MssCLewODGc** 이다.

- 파일 이름 예외 사항(★★★)

    ![YouTube/_.png](YouTube/_.png)

    생성되는 파일명 또는 폴더명에 포함되지 않도록 유의하자

---

- os library

    Miscellaneous operating system interfaces
    기타 운영 체계에 대한 인터페이스

    [os - Miscellaneous operating system interfaces - Python 3.9.4 documentation](https://docs.python.org/3/library/os.html)

    os 라이브러리 참고 사이트

    [](https://rfriend.tistory.com/429)

    ---

    - 실습

        ```python
        '''
        os library 실습

        작성자: 이선웅
        작성일: 2021.04.22
        '''
        **import os

        UserName = "사용자 이름"
        FolderName = "폴더명"
        FolderPath = f"c:/{UserName}/{FolderName}"

        if not os.path.isdir(FolderPath): # 폴더 path가 없으면
            os.makedirs(FolderPath) # 새로 만들어라**
        ```

        ![YouTube/Untitled%202.png](YouTube/Untitled%202.png)

        실습 결과, 사용자 이름/폴더명 생성.

---

- 비디오 코덱

    [영상 코덱 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%EC%98%81%EC%83%81_%EC%BD%94%EB%8D%B1)

- Progressive

    [프로그레시브 다운로드 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%A0%88%EC%8B%9C%EB%B8%8C_%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C)

- FPS

    연속된 사진은 fps ( Frame Per Second ) 로 표현하고, 사진의 해상도는 흔히 p로 표현을 함. 

    ![YouTube/Untitled%203.png](YouTube/Untitled%203.png)

    - 종종 youtube 영상을 볼 때  처음 화면이 매우 뿌옇게 느껴질 때가 있다. 영상을 재생하면 처음엔 해상도가 자동으로 설정돼있는 경우가 대부분. 인터넷 환경이 안 좋다면 화질을 조금 낮추더라도 끊김없이 재생시키기 위함.
        1. 수동으로 화질을 선택 가능.
        2. 고화질, 높은fps의 영상일수록 더 좋은 사진을 초당 더 많이 송출 → data 소모.

[🔝 맨 위로 올라가기]()

# pytube

---

pytube 패키지는 YouTube 비디오를 다운로드 하기 위한 **가볍고 종속성이 없는 라이브러리**다.

- API 사이트

    [Quickstart - pytube 10.7.2 documentation](https://pytube.io/en/latest/user/quickstart.html)

- IDE별 설치 방법
    - Jupyter notebook

        ```python
        !pip install pytube
        ```

        ![YouTube/Untitled%204.png](YouTube/Untitled%204.png)

        실행 결과

    - PyCharm
        1. Project → Python Interpreter 

            ![YouTube/Untitled%205.png](YouTube/Untitled%205.png)

        2. file → Settings

            ![YouTube/Untitled%206.png](YouTube/Untitled%206.png)

        3.  + 모양 클릭

            ![YouTube/Untitled%207.png](YouTube/Untitled%207.png)

        4. pytube  검색 후 패키지 설치

            ![YouTube/Untitled%208.png](YouTube/Untitled%208.png)

- Structure

    ![YouTube/pytube_structure.png](YouTube/pytube_structure.png)

    [[파이썬 유튜브 동영상 다운로더] ( 3 ) pytube 라이브러리 사용법](https://blog.naver.com/PostView.nhn?blogId=skyshin0304&logNo=221620513883&parentCategoryNo=&categoryNo=31&viewDate=&isShowPopularPosts=true&from=search)

## pytube.YouTube

---

Downloading a video from YouTube with pytube is incredibly easy

```python
from pytube import YouTube
**# 강남스타일 : https://www.youtube.com/watch?v=9bZkp7q19f0
yt = YouTube("https://www.youtube.com/watch?v=9bZkp7q19f0")**
```

- Objects

    ```python
    # 상세 정보는 실습 코드에 명시
    title = yt.title
    length = yt.length
    rating = yt.rating
    age_restricted = yt.age_restricted
    author = yt.author
    thumbnail_url = yt.thumbnail_url
    views = yt.views
    description = yt.description.strip()
    ```

- Thumbnail

    **영화**나 **각종 안내**에 대한 **대표(으뜸)되는 이미지**

    [섬네일 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%EC%84%AC%EB%84%A4%EC%9D%BC)

    ```python
    import urllib.request
    print(yt.thumbnail_url)
    urllib.request.urlretrieve(yt.thumbnail_url, 'dynamite.jpg')
    ```

    [urllib.request - Extensible library for opening URLs - Python 3.9.4 documentation](https://docs.python.org/ko/3.10/library/urllib.request.html)

---

- 실습

    ```python
    '''
    pytube.YouTube를 사용해 영상 정보 및 썸네일 불러오기

    작성자: 이선웅
    작성일: 2021.04.22
    '''
    import os
    from pytube import YouTube
    import urllib.request
    yt = YouTube("https://www.youtube.com/watch?v=gdZLi9oWNZg")

    # information
    print("영상 제목:",yt.title)
    print("영상 길이:",yt.length, "초")
    print("영상 평점:",yt.rating)
    print("영상 제한:",yt.age_restricted)
    print("영상 게시자:",yt.author)
    print("영상 썸네일:",yt.thumbnail_url)
    print("영상 조회수:",yt.views)
    print("영상 설명글:",yt.description.strip())

    # thumbnail
    print("영상 썸네일: ", yt.thumbnail_url)
    urllib.request.urlretrieve(yt.thumbnail_url, 'dynamite.jpg')
    ```

    - 결과

        ```
        영상 제목: BTS (방탄소년단) 'Dynamite' Official MV
        영상 길이: 223 초
        영상 평점: 4.7888842
        영상 제한: False
        영상 게시자: HYBE LABELS
        영상 썸네일: https://i.ytimg.com/vi/gdZLi9oWNZg/maxresdefault.jpg?v=5f3f4882
        영상 조회수: 1024068180
        영상 설명글: BTS (방탄소년단) 'Dynamite' Official MV

        Credits:
        Director: Yong Seok Choi (Lumpens)
        Assistant Director: Jihye Yoon (Lumpens)

        Director of Photography: Hyunwoo Nam (GDW)
        B Camera Operator: Eumko
        Focus Puller: Sangwoo Yun, Youngwoo Lee
        2nd AC: Eunki Kim
        3rd AC: Kyuwon Seo
        DIT: Eunil Lee

        Gaffer: Song Hyunsuk
        Lighting Crew: Choi Jung Hyun, Hwang Uigyu, Kim Hyun Ju, Park Cheonil, Park Yeonghwan, Yeom Jaehyeok

        Jimmy Jib Operator: Youngjung Kim
        Jimmy Jib Assistant: Hyun in Kim, Sung Hoon Kim

        Art Director: Bona Kim, Jinsil Park (MU:E)
        Assistant Art Team: Yeri Kang (MU:E)
        Art-team Manager: ilho Heo (MU:E)

        Producer: Emma Sungeun Kim (GE Production)
        Location Manager: Ji Hoon Han

        VFX STUDIO: PLASTIC BEACH
        VFX Supervisor: Ohzeon
        VFX Assistant Supervisor: Jojeem
        VFX Project Manager: Chanyoung Song, Jieun Jeong
        VFX Producer: Kyutae Jang
        3D Artist: Kwangwon Lee, Doyeon Kim, Jeonghwa Lee, Jiwon Jeon
        2D Artist: Gihoon Jang, Hyunjun Lee

        Visual Creative: Nu Kim, Sabinne Cheon, Lee Sun Kyoung, Kim Ga Eun, Jung Su Jung
        Brand Experience Design: Kris Seongmin Gim, Hyeri Lee 
        Performance Directing: Son Sung Deuk, Lee Ga Hun, Lee Byung Eun, Hyewon Park
        Artist Management: Kim Shin Gyu, Kim Su Bin, Kim Dae Young, Park Jun Tae, An Da Sol, Ahn Jong Hun, Yun Tae Woong, Lee Seung Byeong, Lee Jung Min

        Big Hit Entertainment. Rights are reserved selectively in the video. Unauthorized reproduction is a violation of applicable laws. Manufactured by Big Hit Entertainment, Seoul, Korea.

        Connect with BTS: 
        https://ibighit.com/bts 
        http://twitter.com/BTS_bighit
        http://twitter.com/BTS_twt 
        http://www.facebook.com/bangtan.official 
        https://www.youtube.com/user/BANGTANTV 
        http://instagram.com/BTS.bighitofficial 
        https://channels.vlive.tv/FE619 
        https://www.tiktok.com/@bts_official_bighit
        https://weverse.onelink.me/qt3S/94808190
        https://www.weibo.com/BTSbighit
        https://www.weibo.com/BTSmembers 
        http://i.youku.com/btsofficial 
        http://btsblog.ibighit.com

        #BTS #방탄소년단 #BTS_Dynamite #Dynamite #MV

        영상 썸네일: https://i.ytimg.com/vi/gdZLi9oWNZg/maxresdefault.jpg?v=5f3f4882
        ```

        ![YouTube/dynamite.jpg](YouTube/dynamite.jpg)

        dynamite.jpg

## pytube.YouTube.stream

---

스트리밍(streaming)은 주로 **소리(음악)나 동영상 등의 멀티미디어 파일을 전송하고 재생하는 방식**의 하나이다.

보통 파일은 내려받고 난 뒤에 열리는 작업을 하지만, 동영상과 같이 크기가 큰 파일을 재생할 때에는 내려 받는 데에 시간이 오래 걸릴 수 있다. 

**파일을 다운로드하는 것과 더불어 재생을 함으로써 기다리는 시간을 크게 줄일 수** 있다.

[스트리밍 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%EC%8A%A4%ED%8A%B8%EB%A6%AC%EB%B0%8D)

- 정보 확인

    stream 안에는 **영상이 아닌 것도 포함!**

    ```python
    print("stream 객체 전체보기 :")
    yt_streams_list = yt.streams
    for i in range(len(yt_streams_list)):
        print(i, ":",yt_streams_list[i])
    ```

    - 결과

        ```python
        stream 객체 전체보기 :
        0 : <Stream: itag="18" mime_type="video/mp4" res="360p" fps="24fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">
        1 : <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="24fps" vcodec="avc1.640028" progressive="False" type="video">
        2 : <Stream: itag="248" mime_type="video/webm" res="1080p" fps="24fps" vcodec="vp9" progressive="False" type="video">
        3 : <Stream: itag="399" mime_type="video/mp4" res="1080p" fps="24fps" vcodec="av01.0.08M.08" progressive="False" type="video">
        4 : <Stream: itag="136" mime_type="video/mp4" res="720p" fps="24fps" vcodec="avc1.4d401f" progressive="False" type="video">
        5 : <Stream: itag="247" mime_type="video/webm" res="720p" fps="24fps" vcodec="vp9" progressive="False" type="video">
        6 : <Stream: itag="398" mime_type="video/mp4" res="720p" fps="24fps" vcodec="av01.0.05M.08" progressive="False" type="video">
        7 : <Stream: itag="135" mime_type="video/mp4" res="480p" fps="24fps" vcodec="avc1.4d401e" progressive="False" type="video">
        8 : <Stream: itag="244" mime_type="video/webm" res="480p" fps="24fps" vcodec="vp9" progressive="False" type="video">
        9 : <Stream: itag="397" mime_type="video/mp4" res="480p" fps="24fps" vcodec="av01.0.04M.08" progressive="False" type="video">
        10 : <Stream: itag="134" mime_type="video/mp4" res="360p" fps="24fps" vcodec="avc1.4d401e" progressive="False" type="video">
        11 : <Stream: itag="243" mime_type="video/webm" res="360p" fps="24fps" vcodec="vp9" progressive="False" type="video">
        12 : <Stream: itag="396" mime_type="video/mp4" res="360p" fps="24fps" vcodec="av01.0.01M.08" progressive="False" type="video">
        13 : <Stream: itag="133" mime_type="video/mp4" res="240p" fps="24fps" vcodec="avc1.4d4015" progressive="False" type="video">
        14 : <Stream: itag="242" mime_type="video/webm" res="240p" fps="24fps" vcodec="vp9" progressive="False" type="video">
        15 : <Stream: itag="395" mime_type="video/mp4" res="240p" fps="24fps" vcodec="av01.0.00M.08" progressive="False" type="video">
        16 : <Stream: itag="160" mime_type="video/mp4" res="144p" fps="24fps" vcodec="avc1.4d400c" progressive="False" type="video">
        17 : <Stream: itag="278" mime_type="video/webm" res="144p" fps="24fps" vcodec="vp9" progressive="False" type="video">
        18 : <Stream: itag="394" mime_type="video/mp4" res="144p" fps="24fps" vcodec="av01.0.00M.08" progressive="False" type="video">
        19 : <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">
        20 : <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">
        21 : <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">
        22 : <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">
        ```

        ### 총 23개 스트림

        - mp4 : 13개
        - webm : 6개
        - 오디오 : 4개

        ---

        - itag : 태그(위치), id의 역할, 다른 영상과 구분하는 역할을 함
        - mime_type : 확장자, 동영상 타입을 뜻함
        - res : 해상도(144, 260, 360...1080)
        - fps : frame per second(초당 프레임(액자, 장면) 갯수)
        - vcodec : 비디오 코덱
        - acodec : 오디오 코덱
        - progressive : 진보된, 화질 개선
        - type : 비디오/오디오 타입
- 기본 다운로드

    ```python
    yt = YouTube("https://www.youtube.com/watch?v=gdZLi9oWNZg")
    stream = yt.streams.first()
    stream.download()
    ```

    - 결과

        ```python
        'C:\\Users\\User\\Desktop\\python\\4_youtube_crawling\\BTS (방탄소년단) Dynamite Official MV.mp4'
        ```

        ![YouTube/Untitled%209.png](YouTube/Untitled%209.png)

        생성된 동영상 파일 확인

- 옵션 선택 다운로드
    - Stream Query

        화질, 포맷, 오디오/비디오 코덱별로 나뉘어진 여러 개의 링크들 묶음 중에서 사용하고자 하는 하나의 링크를 선택

        [파이썬을 이용해서 유튜브 플레이리스트 동영상을 받아보기 1 - PyTube 사용해보기](https://seolin.tistory.com/93)

        - Adaptive(DASH)

            상황에 맞춰 자동으로 화질을 변경하여 유저가 스스로 새로고침을 하는 수고를 하지 않도록 하는 기능이 있다. 이를 가능하게 하기 위해선, 여러 개의 화질 버전으로 가지고 있어야 하며, 중간에 화질 변경이 되어도 끊김 없이 시청할 수 있도록 각 Stream을 chunk라는 단위로 분할해서 또 가지고 있어야 한다. 

            이런 기술을 DASH(Dynamic Adaptive Streaming over HTTP)라고 한다. 이 기술은 **비디오/오디오의 분리와 합성을 지원**합니다.

            유튜브에서는 음성과 영상을 따로 **분리된 채로 가지고 있다가**, 스트리밍할 때에 이 두 가지를 **하나로 합쳐서 서비스**하는 것

            ```python
            from pytube import YouTube
            yt = YouTube("https://www.youtube.com/watch?v=gdZLi9oWNZg")

            print(yt.streams.filter(adaptive=True))
            ```

            - 결과

                ```
                [<Stream: itag="137" mime_type="video/mp4" res="1080p" fps="24fps" vcodec="avc1.640028" progressive="False" type="video">, 
                <Stream: itag="248" mime_type="video/webm" res="1080p" fps="24fps" vcodec="vp9" progressive="False" type="video">,
                <Stream: itag="399" mime_type="video/mp4" res="1080p" fps="24fps" vcodec="av01.0.08M.08" progressive="False" type="video">, 
                <Stream: itag="136" mime_type="video/mp4" res="720p" fps="24fps" vcodec="avc1.4d401f" progressive="False" type="video">,
                <Stream: itag="247" mime_type="video/webm" res="720p" fps="24fps" vcodec="vp9" progressive="False" type="video">, 
                <Stream: itag="398" mime_type="video/mp4" res="720p" fps="24fps" vcodec="av01.0.05M.08" progressive="False" type="video">, 
                <Stream: itag="135" mime_type="video/mp4" res="480p" fps="24fps" vcodec="avc1.4d401e" progressive="False" type="video">, 
                <Stream: itag="244" mime_type="video/webm" res="480p" fps="24fps" vcodec="vp9" progressive="False" type="video">, 
                <Stream: itag="397" mime_type="video/mp4" res="480p" fps="24fps" vcodec="av01.0.04M.08" progressive="False" type="video">, 
                <Stream: itag="134" mime_type="video/mp4" res="360p" fps="24fps" vcodec="avc1.4d401e" progressive="False" type="video">, 
                <Stream: itag="243" mime_type="video/webm" res="360p" fps="24fps" vcodec="vp9" progressive="False" type="video">, 
                <Stream: itag="396" mime_type="video/mp4" res="360p" fps="24fps" vcodec="av01.0.01M.08" progressive="False" type="video">, 
                <Stream: itag="133" mime_type="video/mp4" res="240p" fps="24fps" vcodec="avc1.4d4015" progressive="False" type="video">, 
                <Stream: itag="242" mime_type="video/webm" res="240p" fps="24fps" vcodec="vp9" progressive="False" type="video">, 
                <Stream: itag="395" mime_type="video/mp4" res="240p" fps="24fps" vcodec="av01.0.00M.08" progressive="False" type="video">, 
                <Stream: itag="160" mime_type="video/mp4" res="144p" fps="24fps" vcodec="avc1.4d400c" progressive="False" type="video">, 
                <Stream: itag="278" mime_type="video/webm" res="144p" fps="24fps" vcodec="vp9" progressive="False" type="video">, 
                <Stream: itag="394" mime_type="video/mp4" res="144p" fps="24fps" vcodec="av01.0.00M.08" progressive="False" type="video">, 
                <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">, 
                <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">, 
                <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">, 
                <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]
                ```

        - Progressive

            **DASH 관련 Stream을 제거한 옵션**이 Progressive 이다.

            하지만, Progressive 옵션으로 Streams를 조회할 경우에 얻을 수 있는 최대 해상도는 **720p**.

            ```python
            from pytube import YouTube
            yt = YouTube("https://www.youtube.com/watch?v=gdZLi9oWNZg")

            print(yt.streams.filter(progressive=True))
            ```

            - 결과

                ```
                [<Stream: itag="18" mime_type="video/mp4" res="360p" fps="24fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">]
                ```

    - itag

        itag를 이용해 특정 stream만 선택 가능

        - 가져오고 싶은 영상의 itag 확인하기

            ```python
            from pytube import YouTube
            yt = YouTube("https://www.youtube.com/watch?v=gdZLi9oWNZg")

            print(yt.streams) # print함수를 통해서 어떤 stream이 있는지 확인합니다.
            ```

        - itag를 통해서 스트림 가져오기

            위의 코드를 통해서 어떤 stream이 있는지 확인했고 그 중에서 18번 stream을 선택했습니다.

            ```python
            yt.streams.get_by_itag("18") 
            ```

            - 전체 코드

                ```python
                from pytube import YouTube

                yt = YouTube("https://www.youtube.com/watch?v=gdZLi9oWNZg")
                print(yt.streams.get_by_itag("18"))
                ```

        - 스트림 다운로드 받기

            ```python
            stream = yt.streams.get_by_itag("18")
            stream.download()
            ```

            `get_by_itag("18")` 의 **18**은 itag번호 입니다. 원하시는 stream의  itag 번호를 넣어주시면 됩니다.

            - 전체코드

                ```python
                from pytube import YouTube

                yt = YouTube("https://www.youtube.com/watch?v=gdZLi9oWNZg")
                stream = yt.streams.get_by_itag("18")
                stream.download()
                ```

    - audio only
        - 오디오만 가지고 있는  stream의 itag 번호를 확인.

            ```python
            from pytube import YouTube
            yt = YouTube("https://www.youtube.com/watch?v=gdZLi9oWNZg")

            print("오디오만 가지고 있는 stream을 확인: \n",yt.streams.filter(only_audio=True))
            ```

            - 결과

                ```
                [<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">, <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]
                ```

        - itag 를 이용해서 오디오만 가지고 있는 stream 을 다운로드

            ```python
            stream = yt.streams.get_by_itag('140')
            stream.download('c:')
            ```

---

- 실습

    Q. 원하는 영상을 원하는 화질로 평소에 자주 사용하는 폴더에 다운로드 받아보자.

    - 코드

        ```python
        '''
        원하는 영상을 원하는 화질로 다운로드 받자.

        작성자: 이선웅
        작성일: 2021.04.23
        '''
        import os
        from pytube import YouTube

        UserName = "사용자 이름"
        FolderName = "폴더명"
        FolderPath = f"c:/{UserName}/{FolderName}"

        if not os.path.isdir(FolderPath): 
            #os.mkdirs(FolderPath)
            os.makedirs(FolderPath)
            
        # Youtube URL
        yt = YouTube("https://www.youtube.com/watch?v=gdZLi9oWNZg")

        # mp4 확장자로 필터링
        yt_streams = yt.streams.filter(progressive=True, file_extension='mp4')

        print("title:", yt.title)
        for i in  range(len(yt.streams)):
            print(f"{i}번 영상 화질 :{yt.streams[i].resolution}")
        num = int(input("다운받을 영상의 번호를 입력해주세요: "))
        yt.streams[num].download(FolderPath)
        ```

    - 결과

        ```
        title: BTS (방탄소년단) 'Dynamite' Official MV
        0번 영상 화질 :360p
        1번 영상 화질 :1080p
        2번 영상 화질 :1080p
        3번 영상 화질 :1080p
        4번 영상 화질 :720p
        5번 영상 화질 :720p
        6번 영상 화질 :720p
        7번 영상 화질 :480p
        8번 영상 화질 :480p
        9번 영상 화질 :480p
        10번 영상 화질 :360p
        11번 영상 화질 :360p
        12번 영상 화질 :360p
        13번 영상 화질 :240p
        14번 영상 화질 :240p
        15번 영상 화질 :240p
        16번 영상 화질 :144p
        17번 영상 화질 :144p
        18번 영상 화질 :144p
        19번 영상 화질 :None
        20번 영상 화질 :None
        21번 영상 화질 :None
        22번 영상 화질 :None
        다운받을 영상의 번호를 입력해주세요: 0
        'c:/사용자 이름/폴더명\\BTS (방탄소년단) Dynamite Official MV.mp4'
        ```

        ![YouTube/Untitled%2010.png](YouTube/Untitled%2010.png)

        동영상 생성 결과

## pytube.YouTube.captions

---

- 언어별 자막 Key

    ```python
    yt = YouTube("https://www.youtube.com/watch?v=gdZLi9oWNZg")
    print(yt.captions)
    ```

    - 결과

        ```
        {'zh': <Caption lang="Chinese" code="zh">, 'en': <Caption lang="English" code="en">, 'ja': <Caption lang="Japanese" code="ja">, 'ko': <Caption lang="Korean" code="ko">, 'es': <Caption lang="Spanish" code="es">}
        ```

- 자막 가져오기

    ```python
    # 신버전 코드
    caption = yt.captions["ko"]
    print(caption.generate_srt_captions())
    ```

    - 결과

        ```
        ```
        1
        00:00:23,999 --> 00:00:27,812
        오늘밤 난 별들 속에 있으니

        2
        00:00:27,812 --> 00:00:32,729
        내 안의 불꽃들로 이밤을 찬란히 밝히는걸 지켜봐

        3
        00:00:32,729 --> 00:00:37,137
        아침에 일어나 신발 신고 우유 한 잔, 이제 시작해볼까

        4
        00:00:37,137 --> 00:00:41,345
        킹콩 드럼을 연주해, 구르는 돌처럼 거침 없이

        5
        00:00:41,345 --> 00:00:42,446
        집으로 걸어 가며 노래해

        6
        00:00:42,446 --> 00:00:45,535
        높이 뛰어 올라 마치 LeBron 처럼

        7
        00:00:45,535 --> 00:00:49,488
        딩동, 전화 줘 아이스티 한 잔과 탁구 한 판

        8
        00:00:49,488 --> 00:00:53,612
        점점 뜨거워지는 분위기 울리는 베이스 들리니 난 준비됐어

        9
        00:00:53,612 --> 00:00:57,865
        인생은 꿀처럼 달콤해 이 비트는 부티가 나지

        10
        00:00:57,865 --> 00:01:01,474
        디스코 파티, 난 좋아 준비 됐어

        11
        00:01:01,474 --> 00:01:05,989
        난 다이아몬드 빛나는 거 알잖아

        12
        00:01:05,989 --> 00:01:09,813
        오늘밤 난 별들 속에 있으니

        13
        00:01:09,813 --> 00:01:14,742
        내 안의 불꽃들로 이밤을 찬란히 밝히는걸 지켜봐

        14
        00:01:14,742 --> 00:01:18,738
        펑크와 소울로 이 도시를 밝혀

        15
        00:01:18,738 --> 00:01:23,464
        빛으로 물들일거야 다이너마이트처럼

        16
        00:01:23,464 --> 00:01:27,379
        친구도 불러 여기 모여봐 오고 싶은 사람 누구든지

        17
        00:01:27,379 --> 00:01:31,904
        좋아 말은 됐어, 이제 정신 없이 흔들어

        18
        00:01:31,904 --> 00:01:33,524
        낮에도 밤에도 하늘은 눈부셔

        19
        00:01:33,524 --> 00:01:35,515
        그러니 우린 아침이 올 때까지 춤을 춰

        20
        00:01:35,515 --> 00:01:40,003
        신사숙녀 여러분, 고민은 내게 맡기고 집중하시죠

        21
        00:01:40,003 --> 00:01:41,499
        점점 뜨거워지는 분위기

        22
        00:01:41,499 --> 00:01:44,134
        울리는 베이스 들리니 난 준비됐어

        23
        00:01:44,134 --> 00:01:48,580
        인생은 꿀처럼 달콤해 이 비트는 부티가 나지

        24
        00:01:48,580 --> 00:01:52,190
        디스코 파티, 난 좋아 준비 됐어

        25
        00:01:52,190 --> 00:01:56,751
        난 다이아몬드 빛나는 거 알잖아

        26
        00:01:56,751 --> 00:02:00,437
        오늘밤 난 별들 속에 있으니

        27
        00:02:00,437 --> 00:02:05,283
        내 안의 불꽃들로 이밤을 찬란히 밝히는걸 지켜봐

        28
        00:02:05,283 --> 00:02:09,537
        펑크와 소울로 이 도시를 밝혀

        29
        00:02:09,537 --> 00:02:13,633
        빛으로 물들일거야 다이너마이트처럼

        30
        00:02:13,633 --> 00:02:22,057
        Dynnnnnanana, 인생은 다이너마이트

        31
        00:02:22,057 --> 00:02:25,773
        펑크와 소울로 난 온 도시를 반짝여

        32
        00:02:25,773 --> 00:02:30,314
        빛으로 물들일거야 다이너마이트처럼

        33
        00:02:30,314 --> 00:02:36,819
        Dynnnnnanana eh

        34
        00:02:36,819 --> 00:02:38,919
        환하게 불을 밝힐거야 다이너마이트처럼

        35
        00:02:38,919 --> 00:02:45,311
        Dynnnnnanana eh

        36
        00:02:45,311 --> 00:02:47,024
        환하게 불을 밝힐거야 다이너마이트처럼

        37
        00:02:47,024 --> 00:02:50,979
        오늘밤 난 별들 속에 있으니

        38
        00:02:50,979 --> 00:02:55,721
        내 안의 불꽃들로 이밤을 찬란히 밝히는걸 지켜봐

        39
        00:02:55,721 --> 00:02:59,567
        펑크와 소울로 이 도시를 밝혀

        40
        00:02:59,567 --> 00:03:04,383
        빛으로 물들일거야 다이너마이트처럼

        41
        00:03:04,383 --> 00:03:07,770
        오늘밤 난 별들 속에 있으니

        42
        00:03:07,770 --> 00:03:12,641
        내 안의 불꽃들로 이밤을 찬란히 밝히는걸 지켜봐

        43
        00:03:12,641 --> 00:03:16,657
        펑크와 소울로 이 도시를 밝혀

        44
        00:03:16,657 --> 00:03:21,045
        빛으로 물들일거야 다이너마이트처럼

        45
        00:03:21,045 --> 00:03:29,519
        Dynnnnnanana, 인생은 다이너마이트

        46
        00:03:29,519 --> 00:03:33,624
        펑크와 소울로 난 온 도시를 반짝여

        47
        00:03:33,624 --> 00:03:37,766
        빛으로 물들일거야 다이너마이트처럼
        ```
        ```

    - 구 버전 코드(결과값은 같다)

        ```python
        # 구 버전 코드
        caption = yt.captions.get_by_language_code("ko")
        print(caption.generate_srt_captions())
        ```

        ![YouTube/__.png](YouTube/__.png)

        deprecated : 비추천 / 앞으로 이 명령어 없어지는 명령어

---

- 실습

[🔝 맨 위로 올라가기]()

# moviepy

---

MoviePy란 python을 이용한 Video Processing에 최적화된 library. 한 줄 코드로 직관적이면서도, 빠르게 비디오 및 오디오의 합성이나 애니메이션, GIF 파일 생성 등이 가능.

- **Why do we use moviepy?**
    - 복잡한 방식으로 처리하거나 구성해야 할 동영상이 많은 경우
    - 웹 서버(Django, Flask 등)에서 비디오 또는 GIF 생성을 자동화려고하는 경우
    - 제목 삽입, 개체 추적, 장면 잘라내기, 엔딩 크레딧 만들기, 자막 등과 같은 지루한 작업을 자동화 하고 싶을 경우
    - 기존 비디오 편집기가 할 수 없는 작업을 수행하기 위해 고유한 비디오 효과를 코딩하려고 하는 경우
    - 다른 파이썬 라이브러리( Matplotlib, Mayavi. Gizeh, scilit-imges...)에서 생성된 이미지에서 애니메이션을 만들고자하는 경우
- **⚠️ moviepy가 최상의 솔루션이 아닌 경우.**
    1. 프레임 별 비디오 분석만 수행하면 되는 경우. ( 얼굴 감지 또는 기타 기능) 라이브러리와 연계해서 **MoviePy**로 작업할 수 있지만 실제로는 **imageio, OpenCV, SimpleCV**를 사용.
    2. 비디오 파일만 변환하거나 일련의 이미지 파일을 동영상으로 변환하려는 경우.

[Moviepy를 이용한 비디오 처리](https://chacha95.github.io/2019-10-24-Movipy/)

- API 사이트

    [moviepy](https://pypi.org/project/moviepy/)

- IDE별 설치 방법
    - Jupyter notebook

        ```python
        !pip install moviepy
        ```

        ![YouTube/Untitled%2011.png](YouTube/Untitled%2011.png)

        다운로드 결과 창

    - PyCham
        - file → Settings

            ![YouTube/Untitled%2012.png](YouTube/Untitled%2012.png)

        - Project → Python Interpreter

            ![YouTube/Untitled%2013.png](YouTube/Untitled%2013.png)

        - + 클릭

            ![YouTube/Untitled%2014.png](YouTube/Untitled%2014.png)

        - moviepy 검색 → moviepy  선택 → install package

            ![YouTube/Untitled%2015.png](YouTube/Untitled%2015.png)

## moviepy.editor

---

기본 단위는 clips로 불리며, 크게 AudioClips, VideoClips, AudioFileClip, VideoFileClip 클래스로 구성됩니다.

**AudioFileclip**과 **VideoFileClip**이 주로 사용됩니다.

- VideoFileClip을 이용해 동영상 자르기

    VideoClip이 기본 Class 이다. 
    하지만 좀 더 user-friendly한 classes로 **VideoFileClip**이나 **ImageClip**이 있습니다.

    - 실습

        **[20/21 PL 29R] 토트넘 vs S.햄튼 H/L**
        https://www.youtube.com/watch?v=51j4Ht814ms

        골 취소장면: 9분~10분 / 540 ~ 600
        패널티 하이라이트: 11분31초 ~ 12분 17초 / 691 ~ 737

        - 코드

            ```python
            '''
            어제밤 있었던 토트넘 경기에서 흥민이형 골장면을 편집해보자.

            작성자: 이선웅
            작성일: 2021.04.22
            '''
            import os
            from pytube import YouTube
            from moviepy.editor import *

            # 폴더 설정
            folderName  = "YouTube_Download"
            path = 'C:/Users/User/Desktop/python/4_youtube_crawling'
            folderPath = f"{path}/{folderName}"  

            # 유튜브 제목에서 다운로드 된 영상 이름 추출
            print("편집할 영상을 선택해주세요.")

            # 디랙토리 보기
            _directory = os.listdir(folderPath)
            for i in range(len(_directory)) :
                print(f"{i+1} 번 : {_directory[i]}")

            # 파일 선택하기
            while True : 
                try : 
                    select = int(input("\n번호를 입력해주세요. "))-1
                    if (0 <= select and select < len(_directory)) :
                        print(f"\n{_directory[i]} 를 선택하셨습니다.");break
                    else : print(f"1~{len(_directory)} 사이 번호를 입력해주세요.")
                except :
                    print(f"1~{len(_directory)} 사이 번호를 입력해주세요.")
                    
            selected_file = f"{folderPath}/{_directory[select]}"

            print("영상을 편집합니다. ")
            print("\n※입력값은 초단위로 입력바람. 1분30초 => 90")
            m_start = int(input("시작 시간 :"))
            m_end = int(input("끝나는 시간 :"))
            m_name = input("\n 저장할 이름을 입력해주세요.(확장자 생략)")

            # 다운로드 된 파일에서 특정 구간 추출 및 저장
            videoclip = VideoFileClip(selected_file)
            videoclip = videoclip.subclip(m_start,m_end)

            videoclip.write_videofile(f"{folderPath}/{m_name}.mp4")

            # 폴더 열기
            os.startfile(folderPath)
            ```

        - 결과

            ```
            편집할 영상을 선택해주세요.
            1 번 : [2021 PL 29R] 토트넘 vs S햄튼 HL.mp4

            번호를 입력해주세요. 1

            [2021 PL 29R] 토트넘 vs S햄튼 HL.mp4 를 선택하셨습니다.
            영상을 편집합니다. 

            ※입력값은 초단위로 입력바람. 1분30초 => 90
            시작 시간 :691
            끝나는 시간 :737

             저장할 이름을 입력해주세요.(확장자 생략)흥민이형_골장면_및_반응
            chunk:   0%|                                                                        | 0/1015 [00:00<?, ?it/s, now=None]
            Moviepy - Building video C:/Users/User/Desktop/python/4_youtube_crawling/YouTube_Download/흥민이형_골장면_및_반응.mp4.
            MoviePy - Writing audio in 흥민이형_골장면_및_반응TEMP_MPY_wvf_snd.mp3
            t:   0%|                                                                            | 0/1379 [00:00<?, ?it/s, now=None]
            MoviePy - Done.
            Moviepy - Writing video C:/Users/User/Desktop/python/4_youtube_crawling/YouTube_Download/흥민이형_골장면_및_반응.mp4

                                                                                                                                   
            Moviepy - Done !
            Moviepy - video ready C:/Users/User/Desktop/python/4_youtube_crawling/YouTube_Download/흥민이형_골장면_및_반응.mp4
            ```

            [https://youtu.be/967s5F6CDYY](https://youtu.be/967s5F6CDYY)

            결과 동영상

---

- 실습

    itsub의 YouTube 최근 영상을 각 timestamp별 영상 자르기 + 각 영역별 파일명
    [url] [https://youtu.be/MssCLewODGc](https://youtu.be/MssCLewODGc)

    [https://www.youtube.com/watch?v=MssCLewODGc](https://www.youtube.com/watch?v=MssCLewODGc)

    - 코드

        ```python
        '''
        유튜브에서 영상을 다운받고,
        각 timestamp별로 따로 및 영역별 파일명으로 저장

        작성자: 이선웅
        작성일: 2021.04.22
        '''
        import os
        from pytube import YouTube
        from moviepy.editor import *

        def remove_punctuation(name):
            name = name.replace("?","")
            name = name.replace(".","")
            name = name.replace(",","")
            name = name.replace("/","")
            name = name.replace(":","")
            name = name.replace(";","")
            name = name.replace("|","")
            name = name.replace("<","")
            name = name.replace(">","")
            return name

        # 폴더 이름 설정
        folderName  = "SunwungLee_YouTube_crawling"

        # 바탕화면에 폴더 생성
        path = 'C:/Users/User/Desktop/python/4_youtube_crawling'
        folderPath = f"{path}/{folderName}"  
        if not os.path.isdir(folderPath): os.makedirs(folderPath)

        yt = YouTube('https://youtu.be/MssCLewODGc')
        yt_streams = yt.streams.filter(progressive=True, file_extension='mp4').all()

        for i in range(len(yt_streams)) : 
            print(f"{i+1} 번 영상 화질 : {yt_streams[i].resolution}")

        # 입력 유효성 검사 
        print("\n다운받을 영상의 번호를 입력해주세요.")
        while True : 
            try : 
                num=int(input(" >>> "))-1
                if (0 <= num and num < len(yt_streams)) :
                    print("\n다운로드 중... \n잠시만 기다려주세요.\n");break
                else : print(f"\n1~{len(yt_streams)} 사이 번호를 입력해주세요.")
            except :
                print(f"\n1~{len(yt_streams)} 사이 번호를 입력해주세요.")
            
        # 다운로드    
        yt_streams[num].download(folderPath)
        print("다운로드가 완료되었습니다..")
        yt_streams[num].on_complete(folderPath)

        #
        # 원본 영상 제목 : 노트20보다 더 좋은기능 있는데 80만원 싸다!? 보급형 스마트폰 전쟁. 갤럭시 A32 사용기!
        # 온점, 물음표와 같은 예외사항들은 자동으로 제거되서 저장
        # 저장후, 물음표와 온점을 제거하는 정규식을 가져야 한다.
        #
        name = yt.title  # 애플이 이럴리가 없는데;; 믿기지않는 혜자 구성? 새로운 아이패드 프로 5세대, 아이맥 M1, 에어태그 발표 총정리!
        name = remove_punctuation(name) + ".mp4"
        #print(name)
        selected_file = f"{folderPath}/{name}"
        #print(selected_file)

        print("영상을 편집합니다.")

        Timestamps = ["00:00", "00:13", "00:44", "03:14", "07:18", "11:38", "12:38"]
        tname = ["이... 이름이", "오프닝", "AirTag", "iMac with M1", "iPad Pro 5th", "이번 이벤트의 소감은"]

        sec = []
        for t in Timestamps:
            minute = t[0:2]
            conv_sec = int(minute) * 60
            ori_sec = int(t[3:])
            sec.append(conv_sec + ori_sec)

        for s in range(len(sec)-1):
            videoclip = VideoFileClip(selected_file)
            videoclip = videoclip.subclip(sec[s], sec[s+1])
            videoclip.write_videofile(f"{folderPath}/{tname[s]}.mp4")

        # 폴더 열기
        os.startfile(folderPath)
        ```

    - 결과

        ```
        1 번 영상 화질 : 360p
        2 번 영상 화질 : 720p

        다운받을 영상의 번호를 입력해주세요.
         >>> 2

        다운로드 중... 
        잠시만 기다려주세요.

        다운로드가 완료되었습니다..
        애플이 이럴리가 없는데 믿기지않는 혜자 구성 새로운 아이패드 프로 5세대 아이맥 M1 에어태그 발표 총정리!.mp4
        C:/Users/User/Desktop/python/4_youtube_crawling/SunwungLee_YouTube_crawling/애플이 이럴리가 없는데 믿기지않는 혜자 구성 새로운 아이패드 프로 5세대 아이맥 M1 에어태그 발표 총정리!.mp4
        영상을 편집합니다.

        Moviepy - Building video C:/Users/User/Desktop/python/4_youtube_crawling/SunwungLee_YouTube_crawling/이... 이름이.mp4.
        MoviePy - Writing audio in 이... 이름이TEMP_MPY_wvf_snd.mp3
        chunk:   1%|▍                                                                | 2/287 [00:00<01:03,  4.48it/s, now=None]
        chunk:  14%|█████████▏                                                      | 41/287 [00:00<00:38,  6.37it/s, now=None]
        chunk:  46%|█████████████████████████████▏                                 | 133/287 [00:00<00:16,  9.07it/s, now=None]
        chunk:  76%|████████████████████████████████████████████████               | 219/287 [00:00<00:05, 12.90it/s, now=None]
        chunk:   2%|█▎                                                             | 27/1324 [00:52<04:24,  4.91it/s, now=None]
        t:   0%|                                                                             | 0/390 [00:00<?, ?it/s, now=None]
        MoviePy - Done.
        Moviepy - Writing video C:/Users/User/Desktop/python/4_youtube_crawling/SunwungLee_YouTube_crawling/이... 이름이.mp4
        ...
        ... # 중간 생략
        ...
        Moviepy - Done !
        Moviepy - video ready C:/Users/User/Desktop/python/4_youtube_crawling/SunwungLee_YouTube_crawling/이번 이벤트의 소감은.mp4
        ```

        ![YouTube/Untitled%2016.png](YouTube/Untitled%2016.png)

        timestamp로 분할된 동영상

[🔝 맨 위로 올라가기]()

# Comments Crawling

---

## 1. YouTube Data API

---

- 1.1 Google API project 생성
    1. Google 계정 로그인
    2. [https://console.cloud.google.com/apis/dashboard](https://console.cloud.google.com/apis/dashboard) 접속
    3. API 프로젝트  생성
        1. 프로젝트 선택 콤보박스

            ![YouTube/Untitled%2017.png](YouTube/Untitled%2017.png)

        2. 새 프로젝트 만들기

            ![YouTube/Untitled%2018.png](YouTube/Untitled%2018.png)

- 1.2 YouTube Data API Activation

    생성된 프로젝트 왼쪽 라이브러리

    1. 라이브러리 검색 화면 이동

        ![YouTube/Untitled%2019.png](YouTube/Untitled%2019.png)

    2. YouTube Data API v3

        ![YouTube/Untitled%2020.png](YouTube/Untitled%2020.png)

    3. 사용
- 1.3 API Key Generation

    API 활성화 화면에서 API 키를 발급. 
    -사용하려는 API
    - API 호출 플랫폼
    - 목적 데이터를 설정
    - 사용자 인증 정보를 추가

    1. 사용자 인정 정보 만들기

        ![YouTube/Untitled%2021.png](YouTube/Untitled%2021.png)

    2. YouTube Data API v3 선택

        ![YouTube/Untitled%2022.png](YouTube/Untitled%2022.png)

    3. 사용

        ![YouTube/Untitled%2023.png](YouTube/Untitled%2023.png)

---

- IDE별 설치 방법
    - Jupyter notebook

        ```python
        !pip install google-api-python-client
        ```

    - PyCharm(NOT YET)

---

- 실습

    ---

    **사용한 YouTube 영상 링크**

    [https://www.youtube.com/watch?v=MssCLewODGc](https://www.youtube.com/watch?v=MssCLewODGc)

    ---

    댓글을 어떤 형식으로 받아오는지 알아보자.

    - 코드

        ```python
        '''
        itsub의 최근 영상에서 댓글들을 크롤링해보자.

        작성자: 이선웅
        작성일: 2021.04.22
        '''
        import pandas # excel로 저장하기 위함.
        from googleapiclient.discovery import build

        comments = list()
        # api-key: AIzaSyAgS28-GeJXqElqenMFVTO89lsdM3My2WE
        api_obj = build('youtube', 'v3', developerKey="AIzaSyAgS28-GeJXqElqenMFVTO89lsdM3My2WE")

        # https://youtu.be/MssCLewODGc
        response = api_obj.commentThreads().list(part='snippet,replies', videoId="MssCLewODGc", maxResults=100).execute()
        print(response)
        ```

    - 결과

        ```
        {'kind': 'youtube#commentThreadListResponse',
         'etag': 'dnyjkyEfLr8NcHT6MJlBEbkS8Mg',
         'pageInfo': {'totalResults': 18, 'resultsPerPage': 100},
         'items': [{'kind': 'youtube#commentThread',
           'etag': '3p974WGi1kspal5jMjYi86IXDmE',
           'id': 'UgxOxKt1tTTXsHPbQLV4AaABAg',
           'snippet': {'videoId': 'MssCLewODGc',
            'topLevelComment': {'kind': 'youtube#comment',
             'etag': 'fv_5VrWP7su3yfsHjwzcYcCaNfc',
             'id': 'UgxOxKt1tTTXsHPbQLV4AaABAg',
             'snippet': {'videoId': 'MssCLewODGc',
              'textDisplay': 'ㅋㅋㅋㅋㅋㅋ애미시스틐ㅋㅋ',
              'textOriginal': 'ㅋㅋㅋㅋㅋㅋ애미시스틐ㅋㅋ',
              'authorDisplayName': '주머니괴물',
              'authorProfileImageUrl': 'https://yt3.ggpht.com/ytc/AAUvwnheeiFUI9FiI1vH5b-Mtxutw_YdNfWwRhAJ5Lxjmg=s48-c-k-c0xffffffff-no-rj-mo',
              'authorChannelUrl': 'http://www.youtube.com/channel/UCxeHnUWAdi5iCh2CSV7K43w',
              'authorChannelId': {'value': 'UCxeHnUWAdi5iCh2CSV7K43w'},
              'canRate': True,
              'viewerRating': 'none',
              'likeCount': 1,
              'publishedAt': '2021-04-21T04:00:41Z',
              'updatedAt': '2021-04-21T04:00:41Z'}},
            'canReply': True,
            'totalReplyCount': 0,
            'isPublic': True}},
          {'kind': 'youtube#commentThread',
           'etag': 'RZv-h38_OQpeLA-6NgRMJjejeCY',
           'id': 'UgweLse6U1m8B4M76eJ4AaABAg',
           'snippet': {'videoId': 'MssCLewODGc',
            'topLevelComment': {'kind': 'youtube#comment',
             'etag': 'rfv1Eee26flW6HYgOOUOR5QPnlA',
             'id': 'UgweLse6U1m8B4M76eJ4AaABAg',
             'snippet': {'videoId': 'MssCLewODGc',
              'textDisplay': '2',
              'textOriginal': '2',
              'authorDisplayName': 'AGIS3678',
              'authorProfileImageUrl': 'https://yt3.ggpht.com/ytc/AAUvwngu7nBu9SIxFPyofxqbjjjkpLzW5xlWaXEh_Uezgw=s48-c-k-c0xffffffff-no-rj-mo',
              'authorChannelUrl': 'http://www.youtube.com/channel/UCILAPy802zjTPt77sLeLe5w',
              'authorChannelId': {'value': 'UCILAPy802zjTPt77sLeLe5w'},
              'canRate': True,
              'viewerRating': 'none',
              'likeCount': 0,
              'publishedAt': '2021-04-21T04:00:40Z',
              'updatedAt': '2021-04-21T04:00:40Z'}},
            'canReply': True,
            'totalReplyCount': 0,
            'isPublic': True}}
        ...
        ... # 중략
        ...
        ```

    ---

    모든 댓글들의 정보 중에서
    - 아이디
    - 댓글
    - 좋아요 수
    - 날짜
    만 골라서 excel에 저장하자.

    - 코드

        ```python
        '''
        itsub의 최근 영상에서 댓글들을 크롤링하여 엑셀파일로 저장해보자.

        작성자: 이선웅
        작성일: 2021.04.22
        '''
        import pandas
        from googleapiclient.discovery import build
         
        # 나의 고유 api 키
        api_key = 'AIzaSyAgS28-GeJXqElqenMFVTO89lsdM3My2WE'
        video_id = 'MssCLewODGc'

        # 저장할 comments 리스트
        comments = list()
        api_obj = build('youtube', 'v3', developerKey=api_key)
        response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, maxResults=100).execute()
         
        while response:
            for item in response['items']: # items 중에서
                comment = item['snippet']['topLevelComment']['snippet']
                comments.append([comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'], comment['likeCount']])
        				# 선택적으로 append
         
                if item['snippet']['totalReplyCount'] > 0:
                    for reply_item in item['replies']['comments']:
                        reply = reply_item['snippet']
                        comments.append([reply['textDisplay'], reply['authorDisplayName'], reply['publishedAt'], reply['likeCount']])
        	  # 댓글들 페이지 업데이트하며 불러옴
            if 'nextPageToken' in response:
                response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, pageToken=response['nextPageToken'], maxResults=100).execute()
            e

        df = pandas.DataFrame(comments)
        df.to_excel('results.xlsx', header=['comment', 'author', 'date', 'num_likes'], index=None)
        ```

    - 결과

        [results.xlsx](YouTube/results.xlsx)

## 2. Python Selenium

---

- 밑의 노션 링크 참조해서 mini project와 함께 사용법 이해

    [YouTube에서 itsub잇섭 영상 크롤링](https://www.notion.so/YouTube-itsub-8c0a911162dc429e97e0482260a64803)

[🔝 맨 위로 올라가기]()