# withを使ったファイルの操作

wname = "amenimo2.txt"
data = """
ミンナニデクノボートヨバレ
ホメラレモセズ
クニモサレズ
サウイフモノニ
ワタシハナリタイ
"""

with open(wname,"x") as file:
    file.write(data)
