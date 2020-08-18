from threading import Thread

# 共有変数n
n = 0

# スレッド１が実行する関数
def func1():
    # 大域変数nを使うことを宣言
    global n

    # nの値を1ずつ100万回増やす
    for i in range(1000000):
        # 危険区域
        n = n + 1

# スレッド２が実行する関数（func1と同じ）
def func2():
    global n

    for i in range(1000000):
        n = n + 1


# ２つのスレッドを生成
t1 = Thread(target=func1)
t2 = Thread(target=func2)

# ２つのスレッドの実行を開始
t1.start()
t2.start()

# ２つのスレッドの終了を待つ
t1.join()
t2.join()
    
# nの値を表示（期待する値は200万）
print(n)
