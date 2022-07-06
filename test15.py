#那些詞出現最多，做出文字雲


import sqlite3
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import jieba
from collections import Counter

db = sqlite3.connect("nkustnews.db")
data=list()
sql = "SELECT title FROM news;"
rows = db.execute(sql)
# 1. 抓資料
for row in rows:
    # 2. 全部變成一個字串 .0. 幹嘛先轉串列
    data.append(row[0])
#print(len(data)) #570
# 2. 全部變成一個字串
data = ";".join(data)
#print(len(data))

# 3. 去掉不好的符號
# 4. 斷詞=>結疤?
jieba.load_userdict("dict.txt")
# res = jieba.cut(data)
# res = [w for w in res]
# print(res)

#去掉不要的東西
with open('stopwords.txt', 'rt', encoding='utf-8') as fp:
    stopwords = [word.strip() for word in fp.readlines()]

keyterms = [keyterm for keyterm in jieba.cut(data) 
            if keyterm not in stopwords
               and keyterm.strip()!=""
               and keyterm.strip()!=","]

# print(keyterms)

# 5. 處理切出來的結果

text = ",".join(keyterms)
mask = np.array(Image.open('cloud.jpg'))
wordcloud = WordCloud(background_color="white",
                      width=1000, height=860, 
                      margin=2, font_path="simhei.ttf", 
                      mask=mask).generate(text)

plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()