from os import *

# startと表示
print('---- start ----')

# 新しいプロセスを生成（プロセスIDを返す）
pid = fork()

# if文の範囲はカッコの代わりにインデントで指定
if pid == 0:
    # 子プロセスの処理
    # lsを実行
    execl('/bin/ls', 'ls')
else:
    # 親プロセスの処理
    # 子プロセスの終了を待つ
    wait()
    
    # endと表示
    print('---- end ----')
