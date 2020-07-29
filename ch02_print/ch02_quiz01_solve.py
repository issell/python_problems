"""

 1. 반지름 9인 원의 넓이를 print()를 사용하여 출력하세요.
    출력은 다음과 같아야 합니다.
    출력)
        반지름 '9'인 원의 넓이는 '254.34'입니다.
    hint)
        9**2 은 9의 2승을 의미합니다.
        원주율은 3.14로 계산하세요.
        문장 안에 외따옴표(')가 있습니다.
        f-string, % operator, format() 을 활용해보세요.

"""
print(f"반지름 '9'인 원의 넓이는 '{9 ** 2 * 3.14}'입니다.")
print(f'반지름 \'9\'인 원의 넓이는 \'{9 ** 2 * 3.14}\'입니다.')
print('반지름 \'%d\'인 원의 넓이는 \'%.2lf\'입니다.' % (9, 9**2*3.14))
print("반지름 '{0}'인 원의 넓이는 '{1:.2f}'입니다.".format(9, 9**2*3.14))


"""
 2. base, height 가 있습니다. 해당 정보를 활용하여 삼각형이었을 경우의 넓이, 사각형이었을 경우의 둘레를 출력하세요.
    소숫점 3자리까지만 출력하세요.
"""
base = 10.512
height = 25.533
print(f'삼각형 넓이 : {base * height / 2:.3f}')
print(f'사각형 둘레 : {(base + height) * 2:.3f}')