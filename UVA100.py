while True:
    a = list(map(int, input().split()))

    l = lambda x,y=1: l(x//2,y+1) if x%2==0 else l(3*x+1,y+1) if x>1 else y
    ans = [l(i) for i in range(min(a[0], a[1]), max(a[0], a[1]))]

    print(f"{str(a[0])} {str(a[1])} {str(max(ans))}")