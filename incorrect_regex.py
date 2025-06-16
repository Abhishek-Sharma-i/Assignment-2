from io import StringIO
import sys
import re

sys.stdin = StringIO("2\n.\\+\n.+\n")

T = int(input())
for _ in range(T):
    pattern = input()
    try:
        re.compile(pattern)
        print(True)
    except re.error:
        print(False)