T = int(input())

for _ in range(T):
    a, b = input().split()
    try:
        result = int(a) // int(b)
        print(result)
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)