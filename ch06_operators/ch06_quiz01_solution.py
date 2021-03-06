"""

 1. 4자리 정수를 입력 받고 각 자릿수의 총합을 출력하세요.
   힌트)
      6432 = 2 + 3 + 4 + 6 = 15
      6432 % 10 --> 2
      6432 // 10 --> 643

      643 % 10 --> 3
      643 // 10 --> 64

      64 % 10 --> 4
      64 // 10 --> 6

      6 % 10 --> 6
      6 // 10
"""

# 방법1
num = int(input('4자리 정수 : '))
total = 0

total += num % 10
num //= 10
total += num % 10
num //= 10
total += num % 10
num //= 10
total += num % 10
num //= 10
print(f"각 자릿수 총합 : {total}")

# 방법2 - 람다식 사용
# from functools import reduce
# num = input('4자리 정수 : ')
# total = reduce(lambda x, y: int(x) + int(y), num)
# print(f"각 자릿수 총합 : {total}")

"""

 2. year 를 입력 받고 윤년이면 True 를, 평년이면 False 를 출력하세요.
   1) 400의 배수는 윤년
   2) (1) 에 해당하지 않는 100의 배수는 평년
   3) (2) 에 해당하지 않는 4의 배수는 윤년

   예) 윤년의 예 : 2020, 2016, 1600, 2000, 2004, 1212
       평년의 예 : 1300, 2100, 2013, 1500

"""
year = int(input('YEAR:'))
print(year % 400 == 0 or (year % 100 != 0 and year % 4 == 0))
