import pymongo

# 连接到 MongoDB 数据库
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["game"]
collection = db["game"]

# 查询数据库中 tags 字段值为 "2694" 的所有记录
query = {"tags": "2694"}
results = collection.find(query)

# 将查询结果写入文本文件中，每条记录占一行
with open("output.txt", "w") as f:
    for result in results:
        f.write(str(result["mobile"]) + "\n")

print("Done writing output.txt")