T = int(input())
for i in range(1, T+1):
    A, B = map(int, input().split())
    C = A + B
    print(f"Case #{i}: {A} + {B} = {C}")