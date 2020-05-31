# PyQT5 배우기 Windows PC 에서
  ## 목차 및 필수요소
  - 설치 간단하게 : 파이썬 최신으로 깔고
  ```
  pip install pyqt5
  pip install pyqt5-tools
  pip install python-opencv
  ```
  - 원문링크 : https://wikidocs.net/book/2165
    - 시작하기
    ```
    git clone https://github.com/d-h-k/Raspi4_QT_GUI.git

    ```
    - https://wikidocs.net/21873
  - 참고할만한 튜토리얼
    ```
    PyQt5 공식 문서 (http://pyqt.sourceforge.net/Docs/PyQt5/)
    pythonspot (https://pythonspot.com/gui/)
    zetcode (http://zetcode.com/gui/pyqt5/)
    opentutorials.org (https://opentutorials.org/module/544)
    tutorialspoint (https://www.tutorialspoint.com/pyqt/)
    udemy 강의1: Python Desktop Application Development with PyQt
    udemy 강의2: Create Simple GUI Applications with Python and Qt
    ```  
  - 목표 : 라즈베리파이의 이런저런 기능을 파이썬으로 돌리자
  - 실행가능한 방법 찾는중
    - 테스트중
    ```
    windows10, anaconda3 환경에서 설치했습니다.

    anaconda prompt 실행
    activate [환경이름]
    pip install pyqt5
    pip install pyqt5-tools
    

    C:\Users\[사용자명]\AppData\Local\Continuum\anaconda3\envs\[환경이름]\Library\bin\designer.exe
    실행
    ```  
    - 윈도우에서는 되지만 라즈에서 쓸수없는방법
    ```
    파이참 + 아나콘다
    ```
  ## Day1 
  ### QT Desiner 소개  
  - 환경설정 : 설치: 아나콘다, VSCODE
    - 아나콘다 네비게이터에서 vscode를 실행해야 함.
  - PyQT5(이하 큐티) 의 구성요소
    - Dialog Window : 실제 프로그램의 화면이 될 곳(GUI), 이 화면에 위젯들을 배치하여 프로그램을 구성
    - Widget Box : 위젯(프로그램에서 기능을 하는 버튼 등의 객체)들을 모아놓은 화면입니다. 이곳에서 원하는 위젯을 Dialog Window로 드래그하여 위젯을 추가할 수 있습니다.
    - Object Inspector : 위젯들의 종속관계를 조절하는 곳입니다. 이곳에서 위젯을 Container 안에 넣는 등의 작업을 할 수 있습니다. Container에 관련된 이야기는 추후에 다루도록 하겠습니다.
    - Property Editor : Property Editor란, 위젯들의 속성을 조절하는 화면입니다. 이 화면에 대한 자세한 설명은 다음장인 위젯에서 하도록 하겠습니다.
  - 큐티로 ui를 제작하는 방법
    - Qt Designer를 이용하여 프로그램의 ui를 제작할 때는 Widget Box에 있는 각종 위젯들을 Dialog화면으로 드래그한 후 배치
    - 이 위젯들의 속성은 Property Editor에서 조절할 수 있는데, 위젯들의 속성은 위젯부분에서 다루도록 
    - 만든 화면이 실제로 프로그램이 되었을 때, 어떻게 작동될 것인지 미리보기를 보고싶다면 Control(Command) + R을 눌러서 미리보기를 
    - Qt Designer의 UI는 저장버튼(Control + S / Command + S)를 누르면 저장을 할 수 있습니다.
    - 저장된 UI파일은 XML의 형식을 가지며, Python 코드에서 이 XML 파일을 Import한 후 위젯들에 기능을 할당해주면 실제로 기능을 가지고 작동하는 GUI프로그램이 되는 것입니다. 
    - 직접 XML형식의 ui파일을 수정하여 레이아웃을 수정할 수도 있습니다.
    - 여기서 XML이란 @@
  - UI와 Python 코드의 연결하는 법
    - 연결방법은 크게 두가지로 나뉩니다.
        - UI파일과 Python코드를 연결시키는데는 UI파일을 통채로 Python코드로 변환시킨 후 그 파일에 코드를 작성하는 방법, 
        - UI파일을 Python 코드에서 import하는 방법 이렇게 두가지가 있습니다.
    - UI파일을 통채로 Python코드로 변환시킨 후 코드를 작성하는 방법의 특징 : 
      - 터미널을 이용해야하는 불편함
      - UI를 수정했을 때 코드를 수정하기 어렵고 
      - 최악의 경우에는 코드 전체를 다시 작성해야 하는 부작용이 
      - 본 강의에서는 UI파일을 Python에 Import하여 사용하는 방법만을 소개하도록 하겠습니다.
    - UI파일을 Python에 Import하여 사용하는 방법
      - UI파일과 동일한 위치에 Python파일을 하나 만든 후, 아래의 코드를 그대로 복사/붙여넣기 합니다. 
      - 이때 중간에 있는 "UI파일이름.ui"는 자신이 가지고 있는 UI의 이름으로 수정해주셔야 합니다.
        ```py
        import sys
        from PyQt5.QtWidgets import *
        from PyQt5 import uic

        #UI파일 연결
        #단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
        form_class = uic.loadUiType("UI파일이름.ui")[0]

        #화면을 띄우는데 사용되는 Class 선언
        class WindowClass(QMainWindow, form_class) :
            def __init__(self) :
                super().__init__()
                self.setupUi(self)

        if __name__ == "__main__" :
            #QApplication : 프로그램을 실행시켜주는 클래스
            app = QApplication(sys.argv) 

            #WindowClass의 인스턴스 생성
            myWindow = WindowClass() 

            #프로그램 화면을 보여주는 코드
            myWindow.show()

            #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
            app.exec_()
        ```
        - 위의 코드를 실행시켰다면 성공적으로 Qt Designer를 이용하여 제작한 UI가 표시되는 것을 볼 수 있습니다. 이제 다음장에서 이 위젯들에 기능을 만들어주는 방법에 대해서 공부해보도록 하겠습니다.
  ### 위젯과 레이아웃
  - 위젯과 레이아웃 배우기 앞서 공통적으로 사용하는 기능 몇가지에 대하여 다룸
  - 위젯의 글자변경 : 위젯에 적힌 글자는 더블클릭해 변경
  - Property Editor의 속성 : 여기에 표시되는 요소들은 위젯에 따라 약간씩 차이가 있지만, 공통적으로 표시되는 요소들도 일부 존재합니다. 공통적으로 표시되는 요소들 중 많이, 그리고 자주 사용하는 속성들에 대해서 알아보겠습니다.
    - ObjectName : Python코드에서 사용될 위젯의 이름을 결정하는 역할을 합니다. 기억하기 쉬운 이름으로 정하는 것을 권장드리며, 서로 다른 위젯이 같은 ObjectName을 가질 수는 없습니다.
    - Gemometry : 위젯의 X,Y좌표(위치)와 가로길이(Width), 세로길이(Height)를 지정합니다. 마우스로 위젯을 끌어당겨서 조절할 수도 있지만, Property Editor에서 숫자로 조정해줄 수도 있습니다.
    - Palette : 위젯의 색상을 지정하는 Palette를 지정합니다. 기본값은 Inherited(시스템의 기본속성)을 사용합니다.
    - Font : 위젯에 글자가 있을 경우, 그 글자의 폰트와 크기를 지정합니다.
    - ToolTip : 위젯 위에 마우스를 올려놓았을 때, 이 위젯에 대한 힌트를 제공해주는 글자를 의미합니다. ToolTip을 설정하고 싶지 않은 경우 공백으로 설정하면 되며, ToolTip을 설정하고 싶다면 원하는 글자를 입력하면 됩니다.
    - ToolTipDuration : toolTip이 얼마나 오래 보여질지를 정합니다. 단위는 ms(millisecond)로, 1초동안 보이게 하려면 1000을 입력합니다. 기본값은 -1로, toolTip이 마우스가 올려져 있는 동안 항상 보여지게 합니다.


    - 시그널과 함수 : PyQt에서 위젯과 관련된 코드는 크게 시그널과 함수 이렇게 두가지로 분류됩니다. 시그널과 함수가 무엇인지 알아보도록 하겠습니다.
      - 시그널 : 
        -시그널이란 위젯의 상태가 바뀌었을 때, 특정 행동을 하게 하는 코드를 의미합니다. 
        - 버튼을 눌렸을 때 어떤 행동을 하게 하거나, 다이얼을 돌렸을 때 화면에 다른 값이 표시되게 하는 행동들은 모두 시그널을 이용합니다.
        - 시그널은 위젯마다 다르며, 하나의 위젯에 여러개의 시그널이 존재할 수 있습니다. 
        - 시그널은 반드시 화면을 표시하는 Class의 생성자부분에 입력되어야 하는데, 생성자부분은 바로 뒤에 나오는 위젯과 Python 코드의 연결부분에서 이야기 하도록 하겠습니다.
        - 시그널의 코드는 뒷부분에서 위젯들을 하나씩 소개할 때 구체적으로 소개하도록 하겠습니다.
      - 함수
        - 함수는 시그널과 다르게 위젯에 아무런 변화가 없더라도 실행될 수 있는 코드를 의미합니다. 
        - 함수는 보통 위젯의 값을 설정하거나, 위젯의 값을 가져오거나, 위젯의 속성을 변화시킬 때 사용됩니다. 
        - PyQt에서는 대부분의 위젯들에서 공통적으로 사용되는 함수들이 몇가지 있는데, 이 함수들에 대해서 간단하게 알아보도록 하겠습니다.
        - 주의할점은 모든 함수의 앞에는 self.ObjectName이 들어가야 합니다. 이때 ObjectName이란, Property Editor에서 지정한 위젯의 ObjectName을 의미합니다
        - 함수 설명을 위한 표
            |Method|설명|
            |---|---|
            |.move(x,y)|	위젯의 위치를 지정합니다. Parameter에는 이동할 위치의 x,y좌표가 들어갑니다.
            |.resize(width,height)|	위젯의 크기를 지정합니다. Parameter에는 위젯의 가로,세로 크기가 들어갑니다.
            |.text()|	위젯에 쓰여있는 글자를 가져옵니다.
            |.setText(String)|	위젯에 새롭게 글자를 작성합니다. Parameter에는 표시할 글자가 들어갑니다.
    
    - Python코드를 이용한 위젯의 동작
      -  Qt Designer를 이용하여 디자인한 UI파일과 Python코드를 연결하는지에 대해서 알아봤었습니다.(이전 장에서) 
      - 그때 언급한 코드만을 이용하면 화면이 보여지기만 하고 위젯들은 아무런 기능도 하지 않을 것입니다.
      - 이제 위젯이 변화(누르거나, 기능을 수행)했을때 기능수해을 윟 어떻게 해야할까요
        - 위젯을 동작시키기 위해서는 시그널을 사용해야 합니다.
        - 이때 시그널은 반드시 클래스의 생성자부분에 사용해야 합니다. 
        - 앞으로 2장-위젯 부분에서 "클래스의 생성자부분"이라는 단어는 모두 아래 코드의 "이 부분에 시그널을 입력해야합니다." 부분을 의미합니다.
        ```PY
        import sys
        from PyQt5.QtWidgets import *
        from PyQt5 import uic

        #UI파일 연결
        #단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
        form_class = uic.loadUiType("UI파일이름.ui")[0]

        #화면을 띄우는데 사용되는 Class 선언
        class WindowClass(QMainWindow, form_class) :
            def __init__(self) :
                super().__init__()
                self.setupUi(self)

                """
                ---------------------------------------------
                이 부분에 시그널을 입력해야 합니다.
                시그널이 작동할 때 실행될 기능은 보통 이 클래스의 멤버함수로 작성합니다.
                ---------------------------------------------
                """

        if __name__ == "__main__" :
            app = QApplication(sys.argv) 
            myWindow = WindowClass() 
            myWindow.show()
            app.exec_()
        ```
    - Import 오류시 대처방법
      - Python 코드의 에디터로 Visual Studio Code를 이용합니다. - Visual Studio Code를 이용하여 PyQt를 이용하다 보면 간혹 PyQt의 모듈이 Import 되지 않는 것을 볼 수 있습니다. 
      - 이런 에러가 발생할 때의 해결방법에 대해여 : https://wikidocs.net/35484
      - 이미 다운로드 받아진 예제코드들 
         - https://github.com/SebinLee/PyQt5forBeginner
         - https://doc.qt.io/qtforpython/PySide2/QtWidgets/QPushButton.html?highlight=qpushbutton
      - 여기부분 수정@@@@@@(실습관련)
      - 이번 페이지의 예제코드는 위의 링크에 있는 02.02 PushButton 폴더에 있습니다. 자유롭게 다운받아서 사용하실 수 있습니다. QPushButton의 보다 자세한 정보는 위의 링크에 있는 Documentation에서 찾으실 수 있습니다.



  ### 
  ### 
  ### 
  ### 
  ### 
  ### 
  ### 
  ### 
  ### 
  ### 
  ### 
  -   