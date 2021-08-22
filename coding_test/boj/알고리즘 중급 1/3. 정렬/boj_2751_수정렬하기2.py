#
# 첫째 줄에 수의 개수 N이 주어짐 (1<=N<=1_000_000)
# 둘째 줄부터 N개의 줄에는 수가 주어짐
# 이 수는 절대값이 1_000_000 보다 작거나 같음
# 수는 중복 X
# 이 숫자들을 오름차순으로 정렬한 결과를 한줄에 하나씩 출력
#
import sys

#cases = int(input())
cases = int(sys.stdin.readline())
num=[]
for _ in range(cases):
    #num.append(int(input()))
    num.append(int(sys.stdin.readline()))

for i in sorted(num):
    print(i)