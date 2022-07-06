import sqlite3
db = sqlite3.connect("nkustnews.db")
#欄位有: id title content date url
#sql = "SELECT id,title FROM news WHERE id<30 ORDER BY id desc;"

#小測驗 出現北科、雲科、屏東科大..個多少次 (用串列、迴圈去跑 解答在下面)
# my_dict={}
# sql1 = "SELECT count(*) FROM news WHERE `content` LIKE '%北科%';"

# rows = db.execute(sql1)
# # 資料庫讀資料預設沒有照順序
# for row in rows:
#     my_dict['北科']=row[0]

# sql2 = "SELECT count(*) FROM news WHERE `content` LIKE '%雲科%';"

# rows = db.execute(sql2)
# for row in rows:
#     my_dict['雲科']=row[0]

# sql3 = "SELECT count(*) FROM news WHERE `content` LIKE '%高科%';"

# rows = db.execute(sql3)
# for row in rows:
#     my_dict['高科']=row[0]

# sql4 = "SELECT count(*) FROM news WHERE `content` LIKE '%中科%';"

# rows = db.execute(sql2)
# for row in rows:
#     my_dict['中科']=row[0]

# print(my_dict)

my_dict={}
schools=['台科','北科','雲科','屏科','中科']
for school in schools:
    sql = "SELECT count(*) FROM news WHERE `content` LIKE '%{}%';".format(school)
    rows = db.execute(sql)

    for row in rows:
        #print(school,":",row[0],"次")
        print("{}:{}次".format(school,row[0]))



