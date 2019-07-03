# 試してみよう

import os
os.listdir()
os.getcwd()
os.mkdir("foo")
os.mkdir("foo/bar/")

#fooディレクトリができていることを確認
os.rmdir("foo/bar/")
os.rmdir("foo")
#makedirsを使用して一度に複数のでいぃれクトリを作成する
os.makedirs("hello/world")
os.removedirs("hello/world")
