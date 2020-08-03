"""
    < 무인 호텔 관리 프로그램 >
    1) 방 개수를 입력 받습니다.
    2) 방 개수와 같은 길이의 리스트를 생성합니다.
        5 개 --> [0,0,0,0,0]
        3 개 --> [0,0,0]
    3) 사용자 메뉴를 메시지로 보여주고 메뉴를 선택 받습니다.
        < 메뉴 >
        1. 체크인
        2. 체크아웃
        3. 현황 보기
        0. 종료하기

        1. 체크인
            방 호수(1번부터 시작)를 입력 받습니다.
            방이 이미 입실 중이면 "입실 중인 방은 체크인 하실 수 없습니다."를 출력하세요.
            빈 방인 경우 "입실 완료!"를 출력하고 메뉴로 돌아갑니다.
        2. 체크아웃
            방 호수(1번부터 시작)를 입력 받습니다.
            방이 빈 방이면 "빈 방은 체크아웃 하실 수 없습니다."를 출력하세요.
            체크인 상태인 경우 "퇴실 완료!"를 출력하고 메뉴로 돌아갑니다.
        3. '방호수 - 상태'를 출력합니다.
            출력 예)
                1호 : 빈 방
                2호 : 입실 중
                3호 : 입실 중
                4호 : 빈 방
                5호 : 빈 방
        0. 종료
            반복을 종료하고 '영업 종료' 를 출력합니다.
    4) 사용자가 메뉴에서 0을 입력할 때까지 (3) 과정을 진행합니다.

"""

# 전체 방 개수 : total
total = int(input('방 개수:'))

# 방법1. for 문으로 append()
# hotel = []
# for n in range(total):
#     hotel.append(0)

# 방법2. 특수 for 문으로 0을 total 개 채우기
hotel = [0 for n in range(total)]

menu = '''1. 체크인
2. 체크아웃
3. 현황 보기
0. 종료하기'''
while True:
    print(menu)
    select = input('선택:')
    if select == '1':
        """
        방 호수(1번부터 시작)를 입력 받습니다.
        방이 이미 입실 중이면 "입실 중인 방은 체크인 하실 수 없습니다."를 출력하세요.
        빈 방인 경우 "입실 완료!"를 출력하고 메뉴로 돌아갑니다.
        """
        num = int(input('체크인 하실 호수 : '))
        num -= 1
        if num < 0 or num >= total:
            print('잘못된 방 호수입니다. 메뉴로 돌아갑니다.')
            continue
        if hotel[num]:  # 0만 아니면 True 로 인식 (hotel[num] == 1)
            print('입실 중인 방은 체크인 하실 수 없습니다.')
            continue
        hotel[num] = 1
        print('입실 완료!')

    elif select == '2':
        """
        방 호수(1번부터 시작)를 입력 받습니다.
        방이 빈 방이면 "빈 방은 체크아웃 하실 수 없습니다."를 출력하세요.
        체크인 상태인 경우 "퇴실 완료!"를 출력하고 메뉴로 돌아갑니다.
        """
        num = int(input('체크아웃 하실 호수 : '))
        num -= 1
        if num < 0 or num >= total:
            print('잘못된 방 호수입니다. 메뉴로 돌아갑니다.')
            continue
        if hotel[num] != 1:  # 0만 아니면 True 로 인식 (hotel[num] == 1)
            print('빈 방은 체크인 하실 수 없습니다.')
            continue
        hotel[num] = 0
        print('퇴실 완료!')
    elif select == '3':
        s = '---- 객실 현황 ----\n'
        for i in range(total):
            # 방법1
            # if hotel[i]:  # hotel[i] != 0 ---> 입실 중이니?
            #     print(f'{i + 1}번 방 - 입실 중')
            # else:
            #     print(f'{i + 1}번 방 - 빈 방')

            # 방법2
            print(f'{i+1}번 방 - {"입실 중" if hotel[i] else "빈 방"}')

    elif select == '0':
        print('프로그램 종료!')
        break
    else:
        print('잘못된 입력! 다시 입력하세요.')