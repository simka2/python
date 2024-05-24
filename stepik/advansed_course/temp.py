import timeit

# s = """
# n, m = 2000, 2000
# c=n+m
# """
# t1 = timeit.timeit(stmt=s, number=1) / 1


n,m = [int(i) for i in input().split()]

mat=[[None for _ in range(m)] for _ in range(n)]

cnt=1
for k in range(n+m):
    for i in range(0 if k<=n else k-n-1,k if k<=n else n):
        for j in range(m-1 if k>=m else k, k-n if k>=n else -1, -1 ):
            print(f"{k=}  {i=}  {j=}")
            mat[i][j]=cnt
            cnt+=1

for r in mat:
    for c in r:
        print(str(c).ljust(3), end=" ")
    print()

n, m = [int(i) for i in input().split()]

mat = [[None for _ in range(m)] for _ in range(n)]

cnt = 1
for k in range(n + m):
    for i in range(0 if k <= n else k - n - 1, k + 1 if k < n else n):
        for j in range(m - 1 if k >= m else k, k - n if k >= n else -1, -1):
            mat[i][j] = cnt
            cnt += 1

for r in mat:
    for c in r:
        print(str(c).ljust(3), end=" ")
    print()



