import pymongo

# 连接到 MongoDB 数据库
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["game"]
collection = db["game"]

# 查询数据库中 tags 字段值为 "9845" 的所有记录
query = {"tags": "9845"}
count = 0

# 分页查询并将查询结果中的 mobile 列写入文本文件中
with open("9845.txt", "w") as f:
    for result in collection.find(query, {"mobile": 1}).batch_size(10000):
        mobile = result['mobile']
        f.write(mobile + "\n")
        count += 1
        if count % 10000 == 0:
            print(f"成功+{count}")