# for a in range(1, 151):
#     print(a)
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 k=max(a,b,c,d)
#                 for e in range(k, 151):
#                     if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
#                         print(a,b,c,d,e)
#                         print(a+b+c+d+e)


s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end='')