# 2023.02.06
# 백준 알고리즘

# ===================================================================

"""
Hello World

Hello World!를 출력하시오.
출력 : Hello World!를 출력하시오.
===================================================================
print("Hello World!")
"""
# ===================================================================

"""
A+B

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력 : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
출력 : 첫째 줄에 A+B를 출력한다.
===================================================================
inp = input()
print(int(inp[0])+int(inp[2]))
"""

# ===================================================================

"""
A-B

두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
입력 : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
출력 : 첫째 줄에 A-B를 출력한다.
===================================================================
inp = input()
print(int(inp[0])-int(inp[2]))
"""

# ===================================================================

"""
A×B

두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.
입력 : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
출력 : 첫째 줄에 A×B를 출력한다.

inp = input()
print(int(inp[0])*int(inp[2]))
"""

# ===================================================================

"""
A/B

두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.
입력 : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
출력 : 첫째 줄에 A/B를 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.
===================================================================
inp = input()
print(int(inp[0])/int(inp[2]))
"""

"""
사칙연산

두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
입력 : 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
출력 : 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
===================================================================
inp = input()

A = int(inp[0:inp.find(" ")])
B = int(inp[inp.find(" "):])

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
"""