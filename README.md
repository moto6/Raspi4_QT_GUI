# Raspi4_QT_GUI
  - 학습목표 : 이번강의에서는 Raspi4 PyQt4에서 
# 1. 이론강의
- 라즈베리파이 OS 설치방법 : 먼저 OS부터 Clean-install 부터 시작!
  - (추천)라즈비안 설치
    - 구글드라이브 링크에서 OS이미지를 다운받아 설치
      - [이미지 다운로드 링크 클릭!](https://drive.google.com/file/d/1r9MPasOY0LY0I5ysVBpq5TQ9AkNVXyyJ/view?usp=sharing)
    - balena-etcher 프로그램 사용해서 SD Card에 burn!
      - https://www.balena.io/etcher/
    - 성공적으로 작업이 완료되면 SD를 라즈베리파이에 장착하고 전원/주변기기들을 장착하고 Booting!
  - 라즈베리파이 OS 설치 (!!사용금지!)
    - (사용금지!) 업데이트된지 5일된 새로나온 OS, 호환성 보장X 
      - https://www.raspberrypi.org/downloads/
    - Raspberry Pi Imager for Windows <<- 링크 클릭!
    - Raspi4 8기가 버전 출시
      - https://www.youtube.com/watch?v=erC2Pu_Jw7o
    - 라즈베리파이 OS는 32비트, 최대 램은 4기가 까지 가능하지만, 문제 해결된 버전
    - 공식홈페이지 링크
      - https://www.raspberrypi.org/products/raspberry-pi-4-model-b/
  - 개발환경 구축 (라즈베리파이)
    ```
    sudo apt-get install update
    sudo apt-get install qtcreator qt5-default
    ```
  - 개발환경구축 HostPC
    ```
    pip install pyqt5
    pip install pyqt5-tools
    ```
  - 설치시 선택사항(OpenCV)
    ```
    pip install python-opencv
    ```
  - 참고링크
    - https://bigwavek.tistory.com/entry/python-PyQt5-%EB%B0%8F-%EC%8B%A4%ED%96%89%ED%8C%8C%EC%9D%BC-%EB%A7%8C%EB%93%A4%EA%B8%B0
  - 설치
    - Windosw Host PC : 아나콘다 설치

- 목차
  ```
  GUI
  1일차 : 
    PyQT 위젯
    시그널과 슬롯
  2일차 : 
    다이얼로그 다루기
    메인 윈도우 만들기
  3일차 : 
    QTableWidget
    데이터 파싱 및 그래프 출력
  4일차 :
    AWS와 DB 연동
    DB 데이터 관리 프로젝트 
  ```
# 2. 이것이 Cross-flatform GUI 의 장점이다!
  ## PC버전 PyQT5 진행 :  
   > https://github.com/d-h-k/Raspi4_QT_GUI/blob/master/PyQT5_PC.md
  ## 라즈베리파이4 PyQT5 : 
   > https://github.com/d-h-k/Raspi4_QT_GUI/blob/master/PyQT5_Rpi4.md
 ## 3) 
 - 스토리 : 큐티는 크로스플랫폼 GUI 프레임웍이라서 리눅스, 윈도우(심지어 맥도!) 돌아간다.
 - 그래서 PC에서 간단하고 빠르고 편하게 파이큐티를 배워보고
 - 라즈베리파이 4에서도 소스코드 옮겨서 (SMABA 사용) 또 돌려본다.
 - 미니프로젝트1 : 라즈베리파이에서 GUI 기능 테스트 프레임워크 제작 
   - 버튼1을 누르면 LED가 켜짐
   - 물리적 스위치를 누르면 GUI상의 스위치에 불이 들어옴
 - 미니프로젝트2 : 
 ## 4) 참조한 링크 밎 자료들 정리
   - 참고 링크 : https://forum.qt.io/topic/105817/qt-creator-on-raspberry-pi4-4gb-ram/3

# 메모
- 이거 왜적어놓은거지
  ```

  1. QtTableWidget
  2. SQLlight로 Query
  3. Matplot Library (그래프)


  1. Thread 예제
  2. OpenCV
  3. GPIO 컨트롤
  4. MySQL Query
  ```

# # Day1 Fisrt
  - 수업자료
  ```
  라즈베리파이 OS 설치방법 : 먼저 OS부터 Clean-install 부터 시작!

    (추천)라즈비안 설치
    구글드라이브 링크에서 OS이미지를 다운받아 설치
    이미지 다운로드 링크 클릭!
    balena-etcher 프로그램 사용해서 SD Card에 burn!
    https://www.balena.io/etcher/
    성공적으로 작업이 완료되면 SD를 라즈베리파이에 장착하고 전원/주변기기들을 장착하고 Booting!
    라즈베리파이 OS 설치 (!!사용금지!)
    (사용금지!) 업데이트된지 5일된 새로나온 OS, 호환성 보장X
    https://www.raspberrypi.org/downloads/
    Raspberry Pi Imager for Windows <<- 링크 클릭!
    Raspi4 8기가 버전 출시
    https://www.youtube.com/watch?v=erC2Pu_Jw7o
    라즈베리파이 OS는 32비트, 최대 램은 4기가 까지 가능하지만, 문제 해결된 버전
    공식홈페이지 링크
    https://www.raspberrypi.org/products/raspberry-pi-4-model-b/
  ```
  
    - 라즈베리파이 PyQt5 설치
      - sudo apt-get install python3-pyqt5
      - sudo apt-get install qttools5-dev-tools

    - 라즈베리파이에 PyQt5가 설치되어있는지 확인
      - python3
      - import PyQt5  

    - 라즈베리파이 OpenCV
      - sudo pip3 install opencv-contrib-python
      - sudo pip3 install opencv-python

    - 라즈베리파이 한글
      - sudo apt-get -y install ibus
      - sudo apt-get -y install ibus-hangul
      - sudo apt-get -y install fonts-unfonts-core


    - 기존 라즈비안 oS 다운로드 링크
      - https://drive.google.com/file/d/1r9MPasOY0LY0I5ysVBpq5TQ9AkNVXyyJ/view  

    - 수많은 PyQt 설치법들..
      - 아나콘다+파이참
        - 가상Python 환경(activate base) : 장점 ->> 여러가지 환경을 꾸며놓고 한PC에서 동시다발적인 프로젝트 진행이 가능하다. 
        - 단점 : 속도가 느려지고..... 배포가 불편하다.. 초보들에게 장애물로 작용한다..
      - pip설치, apt-get 설치(only ubuntu)
        - 저희가 진행한 것, 장점은 : Python을 설치할 수 있는 환경이라면(라즈베리파이, 비글본 블랙... ) 동일하게 설치가 가능하다
        - 단점으로는, 나중에 다른 개발환경을 구축하고자 할때, Ptqt버전이 3.XX 필수로 요구되는경우, 
          - ROS -> APP 파이큐티 3.XXX 을이용해서 제작.
        - 문제가 생기면 python 통째로 삭제 후 재설치
        - autoremove 명령어 활용 (라즈베리파이, 리눅스 기준)
- GPIO 파이썬 
  - https://gpiozero.readthedocs.io/en/stable/        
  - https://www.raspberrypi.org/documentation/usage/gpio/python/README.md

  # 3
  - 이후에 업데이트 상황이 있는지 체키라웃
  ```
  git pull
  ```


- 클래스의 장점에 관하여
  - 클래스 사용의 장점
    - (코드의)재사용성 : 다른이/ 다른 프로젝트에 쉽게 사용할 수 있도록 고려해서 만들어야 한다
    - 모듈화 프로그래밍 : 프로젝트에서 기능별로 구현해 하나로 모으는, 반대되는 개념은 스파게티 코드,짧은 개발시간에 거대한 프로그램 제작을 위해 필수다
    - 리소스를 절약할수 있다 : 재사용, 모듈화를 통해서 동일하거나 유사한 작업을 반복하지 않을수 있다.
    - 객체지향적으로 프로그래밍을 할 수 있다.
    
- 파이썬 설치 디렉토리
  - 여러분의 파이썬이 실제로 동작하는 위치에 대하여
    - 윈도우즈
      > C:\Users\<[username]>\AppData\Local\Programs\Python
    - 리눅스
      > tree -lR | grep 'python'
      > tree / -lR | grep 'python'
    - 나중에 파이썬관련 개발하다 보면 문제가 발생 : 
      - 인스톨 패키지가 꼬이거나 롤백해야 한다거나.... -> ROS 패키지 파이썬 문제
  - Why NOT using 듸자이너
    - 이건마치 여러분들이 바닐라자바스크립트/js를 배우는 이유
    - 기술 Only for 문제 해결
    - 초보자들 입장에서 마치 진입장벽

  - QT 설치 - qtquick , qtcreator
    ```
    sudo apt-get install pyqt5-dev-tools
    sudo apt-get install python3-pyqt5.qtquick
    sudo apt-get install qtcreator
    ```
  - QT 개발환경 
    - non-IDE : 텍스트 코딩만으로 UI 를 개발
    - QT Designer : UI 디자인 Tool -> 
    - QT Creater : Designer 업그레이드 버전
    - 이외에
      - QML 혹은 Python파일을 통해 UI 정보를 주고받는다.
  
  - Why?? 왜 첫날부터 디자이너 하지 왜 처음에는 그냥 non-IDE 방식으로 GUI 를 개발했나요? 
    - 기술은 불편함, 문제를 해결하기 위해서 존재한다. 
    - 불편함을 느끼지 못한다면 기술의 필요성을 
      - 예를들어 강력한 자동완성 기능이 있는 (VS Code / 파이참 ) 에디터를 사용할 경우 대부분의 사람들이 흥미를 잃어가고, 새로운 지식에 대하여 이해도도 떨어진다.
      - 위와 같은 이유로 처음 배울때에는 자동완성 기능이 없는 IDE/에디터가 더 좋은 선택이 될 수도 있다!!!

  - 포트폴리오에 대한 짧은 생각.. 
    - 포트폴리오는 대기업에서 보지 않는다 : 일부 정답 맞습니다. ->> 공채 입사전형에서는 보지 않았다.
      - 공채 입사전형이라도 자소서 쓰는데 [내 경험] =>> 객관화 된 자료로 정리해 놓으면 분명히 도움이 된다!
      - 기본적으로는 회사마다 다르다.
        - 현대자동차 : 공채 X ->> 탈 공채화가 가속화.. : 과거에는 회사별로 공채를 통해 입사했다면(신입사원 교육 -> 부서배치)
        - 앞으로는 주로 부서별로 채용을 하고, 자신들의 부서별 채용!! : 포폴이 도움이 될수 있다. 
      - 카카오, 네이버 -> 포트폴리오 봅니다!
      - 포폴이 갑자기 필요할때? -> 1주일만에 준비가 안됩니다.. 미리 만들어 놓으셔야 합니다.
      - 신입때 잘 만들어 놓으면.. 경력직 이직도 훨씬 준비가 수월해진다..
      - 중소기업도 포트폴리오 있으면 많이 보고 서류 합격률이 높다,
      - 자소이력 많이내서 많이 돌리고, 평균적인 서류 합격률을 높인다 => 포트폴리오.. 


# 4
## SAMBA(옵션..)
- 삼바 설치
```
sudo apt-get install -y samba samba-common-bin
```


- 삼바 계정과 패스워드 설정
```
sudo smbpasswd -a pi
```
패스워드는 raspberry

- 삼바 설정파일 변경을 위해
```
sudo nano /etc/samba/smb.conf
```

- 맨 아랫줄에 추가해줘야하는거
```
[pi]
comment = rpi samba server by girin
path = /home/pi
valid user = pi
writable = yes
read only = no
browseable = yes
```


- 삼바 재시작
```
sudo service smbd restart
```
- 아래 두개는 안되는거 (과거의 버전 혹은 데비안 배포판에 따라 다름..
```
sudo service samba restart
sudo /etc/init.d/samba restart
```

- 참고 링크 : https://fishpoint.tistory.com/1553

