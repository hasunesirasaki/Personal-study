#画像ファイルの表示

from IPython.display import Image, display_jpeg
import requests
URL = "http://www.teu.ac.jp/common/images/mainimgs/mainimgs_gaiyou.jpg"
FNAME = "gakuen.jpg"
r = requests.get(URL)
display_jpeg(Image(r.content))
open(FNAME,"wb").write(r.content)

#im = Image.open("gakuen.jpg")
#im.show()
