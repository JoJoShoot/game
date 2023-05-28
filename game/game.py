from flask import Flask, request, render_template
import pymongo
import os

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["game"]
collection = db["game"]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/query')
def query():
    tags = request.args.get("tags", "").split(",")
    query = {"tags": {"$in": tags}}
    count = collection.count_documents(query)

    return str(count)


def export_to_txt(tags):
    # 以tags值命名文件名
    filename = "_".join(tags) + ".txt"

    # 指定完整的文件路径
    file_path = os.path.join(app.root_path, "static", "downloads", filename)

    with open(file_path, "w") as file:
        count = 0
        page_size = 10000
        query = {"tags": {"$in": tags}}

        for result in collection.find(query, {"mobile": 1}).batch_size(page_size):
            mobile = result['mobile']
            file.write(mobile + "\n")
            count += 1

        print(f"导出 {count} 条数据到 {file_path}")

    return file_path


@app.route('/download')
def download():
    tags = request.args.get("tags", "").split(",")
    file_path = export_to_txt(tags)

    if os.path.exists(file_path):
        return file_path

    return ""


if __name__ == '__main__':
    if not os.path.exists(os.path.join(app.root_path, "static", "downloads")):
        os.makedirs(os.path.join(app.root_path, "static", "downloads"))

    app.run(debug=True)
