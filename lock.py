from threading import Thread, Lock

# 共有変数n
n = 0

# スレッド１が実行する関数
def func1():
    global n
    global lock
    
    for i in range(1000000):
        # ロックを獲得(Lock)
        lock.acquire()
        
        # 危険区域
        n = n + 1

        # ロックを解放(Unlock)
        lock.release()

# スレッド２が実行する関数（func1と同じ）
def func2():
    global n
    global lock
    
    for i in range(1000000):
        lock.acquire()
        n = n + 1
        lock.release()

# ロック（大域変数）を作成
lock = Lock()

t1 = Thread(target=func1)
t2 = Thread(target=func2)

t1.start()
t2.start()

t1.join()
t2.join()
    
print(n)
