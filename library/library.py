#OS library (ファイルの中にどんなデータが保存されているかを呼び出す、表面的にのみ)

import os
pwd = os.getcwd()
files = os.listdir()

print(pwd)
print(files)
