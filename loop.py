from threading import Thread
from time import sleep

# スレッド数
n = 4

# 無限ループ
def loop():
    while True:
        pass
    
# スレッドのリスト
tlist = []

# n個のスレッドを生成
for i in range(n):
    t = Thread(target=loop)
    t.setDaemon(True)
    tlist.append(t)

# n個のスレッドの実行を開始
for t in tlist:
    t.start()

# 20秒待つ
sleep(20)
