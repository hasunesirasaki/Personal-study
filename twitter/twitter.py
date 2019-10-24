
CON_KEY    = ""
CON_SECRET = ""
ACC_TOKEN  = ""
ACC_SECRET = ""

import tweepy

auth = tweepy.OAuthHandler(CON_KEY,CON_SECRET)
auth.set_access_token(ACC_TOKEN,ACC_SECRET)
twitter = tweepy.API(auth)

#自分の情報の取得
me = twitter.me()
print(me.id) #アカウントのID番号
print(me.name) #設定した名前
print(me.screen_name) #アカウント名（ローマ字の奴）
print(me.created_at) #アカウントの作成日
print(me.description) #アカウントの説明
print(me.followers_count) #フォロワーの数
print(me.friends_count) #フォローしている人の数

#自分のタイムラインを取得
htl = twitter.home_timeline(count = 200)
newest = htl[0]
print(newest.user.name, ":\t", newest.text) #名前と発言

#自分の発言（User Timeline）
utl = twitter.user_timeline(count=200)
#print(utl[0],text) #最新の自分の発言

#for tweet in htl:
#    print(tweet.user.screen_name, "\t:", tweet.text)

#友達関係の収集
friends = twitter.friends(count=200)

for f in friends:
    print(f.id, f.screen_name, f.name)


#プログラムを使った投稿
##MSG = "PYTHONからのメッセージ"
#twitter.update_status(MSG)
#utl = twitter.user_timeline()
#print(utl[0].id,utl[0].text)

#写真付き投稿
#msg = "涼しさは伝わりそう"
#fname = "ice.jpg"
#twitter.update_with_media(fname,msg)

#ツイートを消す
MSG = "PYTHONからのメッセージ2"
twitter.update_status(MSG)
utl = twitter.user_timeline()
print(utl[0].id, utl[0].text)
print(utl[1].id, utl[1].text)

ID = (utl[1].id)
twitter.destroy_status(ID)
