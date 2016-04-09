# -*- coding: utf-8 -*-
# def triangles():
#     arr = []
#     for x in range(10):
#         y = 0;
#         temp = []
#         while y <= x:
#             if y==0 or y == x:
#                 m = 1
#             else:
#                 m = arr[x-1][y-1] + arr[x-1][y]
#             temp.append(m);
#             y += 1
#         arr.append(temp)
#     return arr
def triangles():
    list = [1]
    yield list;
    while True:
        list = [1] + [list[n]+list[n+1] for n in range(len(list)-1)] + [1]
        yield list;

# 期待输出:
# [1] 0 0
# [1, 1]
# [1, 2, 1] 20=1 21=10+11 22=11+12
# [1, 3, 3, 1] x =3 y = 0-3
# [1, 4, 6, 4, 1] x = 4 y = 0 - 4 [4][1] = [3][0] + [3][1] [4][2](6) = [3][1]() +[3][2]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

##### github test #####
#brach master add $$####
