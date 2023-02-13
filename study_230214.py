# 2023.02.14
# 백준 알고리즘

# ===================================================================

"""
빠른 A+B

본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다.
    입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

    C++을 사용하고 있고 cin/cout을 사용하고자 한다면,
    cin.tie(NULL)과 sync_with_stdio(false)를 둘 다 적용해 주고,
    # endl 대신 개행문자를 쓰자. 단, 이렇게 하면 더 이상 scanf/printf/puts/getchar/putchar 등
    C의 입출력 방식을 사용하면 안 된다.

    Java를 사용하고 있다면, Scanner와 System.out.println 대신
    BufferedReader와 BufferedWriter를 사용할 수 있다.
    BufferedWriter.flush는 맨 마지막에 한 번만 하면 된다.

    Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
    단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우
    .rstrip()을 추가로 해 주는 것이 좋다.

입력 : 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다.
        다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.
출력 : 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.
===================================================================
import sys

T = int(sys.stdin.readline().rstrip())

answer = []
for i in range(T):
    num = sys.stdin.readline().rstrip().split()
    answer.append(int(num[0]) + int(num[1]))

for j in range(T):
    print(answer[j])
"""

# ===================================================================

"""
A + B - 7

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
        각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
출력 : 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다.
        테스트 케이스 번호는 1부터 시작한다.
===================================================================
T = int(input())

num = []
for i in range(T):
    inp = input().split()
    num.append(int(inp[0]) + int(inp[1]))

for j in range(T):
    print("Case #" + str(j+1) + ": " + str(num[j]))
"""

# ===================================================================

"""
A + B - 8

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
        각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
출력 : 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다.
        x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
===================================================================
T = int(input())

num = []
for i in range(T):
    inp = input().split()
    num.append([inp[0], inp[1], int(inp[0]) + int(inp[1])])

for j in range(T):
    print("Case #" + str(j+1) + ": " + str(num[j][0]) + " + " + str(num[j][1]) + " = " + str(num[j][2]))
"""