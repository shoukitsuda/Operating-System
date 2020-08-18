from time import time

# 1億個のデータを持つリストを作成
data = list(range(100000000))

print('allocated')


# １回目（ページイン）
start = time()

# 先頭の2千万個のデータにアクセス
sum = 0
for i in range(20000000):
    sum += data[i]

print('1st: {:.1f} sec'.format(time() - start))


# ２回目（ページインなし）
start = time()

# 先頭の2千万個のデータにアクセス
sum = 0
for i in range(20000000):
    sum += data[i]

print('2nd: {:.1f} sec'.format(time() - start))
