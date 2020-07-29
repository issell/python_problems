"""

    < 학생 관리 프로그램 >

    step 1. 다음 학생들의 정보를 dictionary 에 저장하세요.
    key 는 학번입니다.

    학번          이름      평균      등급      연락처
    101         홍길동      88       B        010-2222-1231
    102         김길동      92       A        010-2231-1256
    103         김장미      47       F        010-2512-7754
    201         장아름      85       B        010-9966-3512
    202         최영수      74       C        010-1111-3864

    step 2. (1)의 딕셔너리에 학생 3명의 정보를 입력 받아 추가 저장합니다.
        - 학생의 이름, 국, 영, 수, 학년, 연락처를 입력 받습니다.

        - 학년은 학번의 가장 앞자리에 해당합니다.
          예를 들어 딕셔너리에 저장된 2학년 학생이 4명이라면, 다음 2학년 학생의 학번은 205가 되어야 합니다.

        - 평균은 국,영,수 의 평균을 계산하여 저장합니다.
            *사용자에게 입력 받지 않습니다.

        - 등급은 평균에 따른 A, B, C, D, F 중 하나로 저장합니다.
            *사용자에게 입력 받지 않습니다.
            90 점 이상 : A
            80점 이상 ~ 90점 미만 : B
            70점 이상 ~ 80점 미만 : C
            60점 이상 ~ 70점 미만 : D
            60점 미만 : F

    step 3. 사용자 메뉴를 출력합니다. (선택문제)
        1. 학번으로 검색
        2. 연락처 뒷번호로 검색
        3. 1등 학생 보기
        4. 모든 학생 보기
        0. 종료

        1. 학번으로 검색
            학번을 입력 받고 해당 학생의 모든 정보를 출력합니다.
            미등록 학번인 경우 '미등록 학번'을 출력합니다.

        2. 연락처 뒷번호로 검색
            연락처 뒷번호 4자리를 입력 받아 연락처가 일치하는
            '모든' 학생들의 이름, 학년, 연락처를 출력합니다.

        3. 1등 학생 보기
            평균을 가지고 1등 학생을 찾아 해당 학생의 학번, 이름, 평균 점수를 출력합니다.
            공동 1등인 경우 학년이 가장 높은 학생을,
            그 중 같은 학년에 공동 1등이 있다면 그 학생들 모두를 출력하세요.

        4. 모든 학생 보기
            현재 등록되어있는 모든 학생들의 모든 정보를 출력하세요.

"""