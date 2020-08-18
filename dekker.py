from threading import Thread

# 共有変数n
n = 0

# Dekkerのアルゴリズムで使う大域変数
turn = 1
c1 = 1
c2 = 1

# スレッド１が実行する関数
def func1():
    global n
    global turn, c1, c2
    
    for i in range(1000000):
        c1 = 0

        while c2 == 0:
            if turn == 2:
                c1 = 1
                while turn == 2:
                    pass
                c1 = 0
        
        # 危険区域
        n = n + 1

        c1 = 1
        turn = 2
        
# スレッド２が実行する関数
def func2():
    global n
    global turn, c1, c2
    
    for i in range(1000000):
        c2 = 0

        while c1 == 0:
            if turn == 1:
                c2 = 1
                while turn == 1:
                    pass
                c2 = 0
        
        # 危険区域
        n = n + 1

        c2 = 1
        turn = 1

t1 = Thread(target=func1)
t2 = Thread(target=func2)

t1.start()
t2.start()

t1.join()
t2.join()
    
print(n)
