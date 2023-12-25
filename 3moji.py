# coding: utf-8

from misskey import Misskey
from atproto import Client, models
import random
import os
import time

# coding:utf-8
hiragana = ['ぁ', 'あ', 'ぃ', 'い', 'ぅ', 'う', 'ぇ', 'え', 'ぉ', 'お', 'か', 'が', 'き', 'ぎ', 'く', 'ぐ', 'け', 'げ', 'こ', 'ご', 'さ', 'ざ', 'し', 'じ', 'す', 'ず', 'せ', 'ぜ', 'そ', 'ぞ', 'た', 'だ', 'ち', 'ぢ', 'っ', 'つ', 'づ', 'て', 'で', 'と', 'ど', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ば', 'ぱ', 'ひ', 'び', 'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ', 'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ', 'ま', 'み', 'む', 'め', 'も', 'ゃ', 'や', 'ゅ', 'ゆ', 'ょ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'ゎ', 'わ', 'ゐ', 'ゑ', 'を', 'ん','ー']

a3 = random.choice(hiragana)
b3 = random.choice(hiragana)
c3 = random.choice(hiragana)
post_text = a3 + b3 + c3
while True:
    try:
        misskey_address = os.environ.get("MISSKEY_SERVER_ADDRESS")
        misskey_token = os.environ.get("MISSKEY_TOKEN")
        moji3 = Misskey(misskey_address)
        moji3.token = misskey_token
        moji3.notes_create(text=post_text)
    except:
        print('Retry...')
        time.sleep(300)
    else:
        break

while True:
    try:
        # Bluesky
        bluesky = Client()
        bluesky.login(str(os.environ.get("BLUESKY_MAIL_ADDRESS")),str(os.environ.get("BLUESKY_PASSWORD")))
        bluesky.send_post(post_text)
    except:
        time.sleep(300)
    else:
        break
print(a3+b3+c3+'\n')
